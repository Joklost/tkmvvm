import tkinter
from context import tkmvvm


class CalculatorView(tkmvvm.view.View):
    def __init__(self, parent: tkinter.Tk, context: tkmvvm.viewmodel.ViewModel, height: int, width: int, debug: bool = True):
        super().__init__(parent, context, height, width)
        self.window = tkinter.Toplevel(self.parent)
        self.center_window(self.window)

        # enable quitting when pressing the exit button
        self.window.protocol('WM_DELETE_WINDOW', self.window.quit)

        if debug:
            self.reload_btn = tkinter.Button(
                self.window,
                text='Reload View',
                command=self.reload_xml,
                width=20
            )
            self.reload_btn.grid(row=0)

    def reload_xml(self):
        for widget in self.widgets:
            widget.grid_forget()

        self.load_xml('view.xml')
