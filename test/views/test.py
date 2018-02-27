import tkinter
import tkinter.ttk
from context import tkmvvm

STICKY = tkinter.E + tkinter.N + tkinter.S + tkinter.W


class TestView(tkmvvm.view.View):
    def __init__(self, parent: tkinter.Tk, context: tkmvvm.viewmodel.ViewModel):
        super().__init__(parent, context)

        # ('clam', 'alt', 'default', 'classic')
        self.style = tkinter.ttk.Style()
        self.style.theme_use('clam')

        self.window = tkinter.Toplevel(self.parent)
        self.window.title('MVVM Demo')
        self.window.protocol('WM_DELETE_WINDOW', self.window.quit)
        self.center_window(self.window, 605, 400)
        self.border = tkinter.Frame(self.window, relief='flat', borderwidth=20)

        #######################################################
        self.iterator2_btn = tkinter.Button(
            self.window,
            text="++",
            command=self.context.iterate_iterator
        )
        self.iterator2_btn.grid(row=0, column=0, columnspan=2, sticky=STICKY)
        #######################################################
        self.iterator1_btn = tkinter.ttk.Button(
            self.window,
            text="++",
            command=self.context.iterate_iterator
        )
        self.bind_data(self.iterator1_btn, 'iterator')
        self.iterator1_btn.grid(row=0, column=2, columnspan=2, sticky=STICKY)
        #######################################################
        self.iterator_lbl = tkinter.ttk.Label(self.window)
        self.iterator_lbl.grid(row=0, column=4, columnspan=2, sticky=STICKY)
        self.bind_data(self.iterator_lbl, 'iterator')
        #######################################################
        self.reset_entry_btn = tkinter.ttk.Button(
            self.window,
            text="Reset Entry -->",
            command=self.context.reset_entry
        )
        self.reset_entry_btn.grid(row=1, column=0, columnspan=2, sticky=STICKY)
        #######################################################
        self.entry_entry = tkinter.ttk.Entry(self.window)
        self.bind_data(self.entry_entry, 'entry_data')
        self.entry_entry.grid(row=1, column=2, columnspan=2, sticky=STICKY)
        #######################################################
        self.entry_data_lbl = tkinter.ttk.Label(self.window)
        self.bind_data(self.entry_data_lbl, 'entry_data')
        self.entry_data_lbl.grid(row=1, column=4, columnspan=2, sticky=STICKY)
        #######################################################
        # listbox 1
        self.data1_listbox = tkinter.Listbox(self.window, width=62, selectmode=tkinter.MULTIPLE)
        self.data1_listbox.grid(row=2, column=0, columnspan=4, rowspan=4, sticky=STICKY)
        self.bind_data(self.data1_listbox, 'items')
        #######################################################
        self.add_listbox_entry1_btn = tkinter.ttk.Button(
            self.window,
            text="<-- Add Item",
            command=self.context.add_listbox_entry
        )
        self.add_listbox_entry1_btn.grid(row=2, column=4, columnspan=2, rowspan=2, sticky=STICKY)
        #######################################################
        self.add_listbox_entry1_btn = tkinter.ttk.Button(
            self.window,
            text="<-- Remove Item",
            command=self.context.remove_listbox_entry
        )
        self.add_listbox_entry1_btn.grid(row=4, column=4, columnspan=2, rowspan=2, sticky=STICKY)
        #######################################################
        # listbox 2
        self.data2_listbox = tkinter.Listbox(self.window, width=62, selectmode=tkinter.EXTENDED, height=2)
        self.data2_listbox.grid(row=6, column=0, columnspan=4, rowspan=1, sticky=STICKY)
        self.bind_data(self.data2_listbox, 'items')
        #######################################################
        self.add_listbox_entry2_btn = tkinter.ttk.Button(
            self.window,
            text="<-- Add Item",
            command=self.context.add_listbox_entry
        )
        self.add_listbox_entry2_btn.grid(row=6, column=4, columnspan=2, rowspan=1, sticky=STICKY)
        #######################################################
        self.checkerbutton1 = tkinter.ttk.Checkbutton(
            self.window
        )
        self.bind_data(self.checkerbutton1, 'toggle')
        self.checkerbutton1.grid(row=7, column=0, sticky=STICKY)
        #######################################################
        self.checkerbutton2 = tkinter.Checkbutton(
            self.window
        )
        self.bind_data(self.checkerbutton2, 'toggle')
        self.checkerbutton2.grid(row=7, column=1, sticky=STICKY)
        #######################################################
        self.checkerbutton_lbl = tkinter.ttk.Label(self.window)
        self.bind_data(self.checkerbutton_lbl, 'toggle')
        self.checkerbutton_lbl.grid(row=7, column=2, columnspan=1, sticky=STICKY)

    def mainloop(self):
        self.parent.mainloop()

    def resizeable(self, width: bool, height: bool):
        self.parent.resizable(width, height)
