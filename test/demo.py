import tkinter
import tkinter.ttk

import models.test
import viewmodels.test
import views.test


def main():
    model = models.test.TestModel()
    vm = viewmodels.test.TestViewModel(model)
    root = tkinter.Tk()
    view = views.test.TestView(root, vm)
    root.resizable(False, False)
    root.withdraw()

    root.mainloop()


if __name__ == '__main__':
    main()
