import tkinter
from context import tkmvvm


class CalculatorView(tkmvvm.view.View):
    def __init__(self, parent: tkinter.Tk, context: tkmvvm.viewmodel.ViewModel, height: int, width: int):
        super().__init__(parent, context, height, width)
        self.window = tkinter.Toplevel(self.parent)
        self.center_window(self.window)

        # enable quitting when pressing the exit button
        self.window.protocol('WM_DELETE_WINDOW', self.window.quit)
