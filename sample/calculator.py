import tkinter

from viewmodels.calculator import CalculatorViewModel
from views.calculator import CalculatorView


def main():
    view_model = CalculatorViewModel(None)
    root = tkinter.Tk()
    root.withdraw()

    view = CalculatorView(root, view_model, 600, 400)
    view.load_xml('view.xml')
    view.resizeable(False, False)
    # view.mainloop()


if __name__ == '__main__':
    main()
