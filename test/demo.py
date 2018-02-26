import tkinter
import tkinter.ttk
import string
import random



from context import tkmvvm


class TestModel(tkmvvm.model.Model):
    # properties can be stored either in the Model, or on the ViewModel
    entry_data = "A quick brown fox jumps over the lazy dog"
    toggle = False
    items = []


class TestViewModel(tkmvvm.viewmodel.ViewModel):
    # this property is stored in the ViewModel
    _iterator = 0

    def __init__(self, model: tkmvvm.model.Model):
        super(TestViewModel, self).__init__(model)

    #######################################################
    @property
    def iterator(self):
        return self._iterator

    @iterator.setter
    def iterator(self, value):
        self._iterator = value
        self.on_property_changed("iterator")

    #######################################################

    #######################################################
    @property
    def entry_data(self):
        return self.model.entry_data

    @entry_data.setter
    def entry_data(self, value):
        self.model.entry_data = value
        self.on_property_changed('entry_data')

    #######################################################

    #######################################################
    def iterate_iterator(self):
        self.iterator = self.iterator + 1

    def reset_entry(self):
        # this will call the setter for entry_data, and in turn update the View
        self.entry_data = ""

    #######################################################


class TestView(tkmvvm.view.View):
    def __init__(self, parent: tkinter.Tk, context: tkmvvm.viewmodel.ViewModel):
        super().__init__(parent, context)

        # ('clam', 'alt', 'default', 'classic')
        self.style = tkinter.ttk.Style()
        self.style.theme_use('clam')

        self.window = tkinter.Toplevel(self.parent)
        self.window.title('KCDMods')
        self.window.protocol('WM_DELETE_WINDOW', self.window.quit)
        self.center_window(self.window, 605, 400)
        self.border = tkinter.Frame(self.window, relief='flat', borderwidth=20)

        self.widgets()

    def widgets(self):
        #######################################################
        self.iterator2_btn = tkinter.Button(
            self.window,
            text="++",
            command=self.context.iterate_iterator
        )
        self.iterator2_btn.grid(row=0, column=0, columnspan=2, sticky=tkinter.W + tkinter.E)
        #######################################################
        self.iterator1_btn = tkinter.ttk.Button(
            self.window,
            text="++",
            command=self.context.iterate_iterator
        )
        self.bind_data(self.iterator1_btn, 'iterator')
        self.iterator1_btn.grid(row=0, column=2, columnspan=2, sticky=tkinter.W + tkinter.E)
        #######################################################
        self.iterator_lbl = tkinter.ttk.Label(self.window)
        self.iterator_lbl.grid(row=0, column=4, columnspan=2, sticky=tkinter.W + tkinter.E)
        self.bind_data(self.iterator_lbl, 'iterator')
        #######################################################
        self.reset_entry_btn = tkinter.ttk.Button(
            self.window,
            text="Reset Entry -->",
            command=self.context.reset_entry
        )
        self.reset_entry_btn.grid(row=1, column=0, columnspan=2, sticky=tkinter.W + tkinter.E)
        #######################################################
        self.entry_entry = tkinter.ttk.Entry(self.window)
        self.bind_data(self.entry_entry, 'entry_data')
        self.entry_entry.grid(row=1, column=2, columnspan=2, sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)
        #######################################################
        self.entry_data_lbl = tkinter.ttk.Label(self.window)
        self.bind_data(self.entry_data_lbl, 'entry_data')
        self.entry_data_lbl.grid(row=1, column=4, columnspan=2, sticky=tkinter.W + tkinter.E)
        #######################################################
        # listbox
        self.data_listbox = tkinter.Listbox(self.window, width=100)
        self.data_listbox.grid(row=2, column=0, columnspan=6, rowspan=4, sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)
        # self.bind_data(self.installed_listbox, 'installed_listbox')
        #######################################################

def main():
    model = TestModel()
    vm = TestViewModel(model)
    root = tkinter.Tk()
    view = TestView(root, vm)
    root.resizable(False, False)
    root.withdraw()

    root.mainloop()


if __name__ == '__main__':
    main()
