import tkinter
import tkinter.ttk

import models.test
import viewmodels.test
import views.test


def main():
    model = models.test.TestModel()
    vm = viewmodels.test.TestViewModel(model)
    root = tkinter.Tk()
    root.withdraw()

    view = views.test.TestView(root, vm, 600, 400)
    view.resizeable(False, False)
    view.mainloop()


if __name__ == '__main__':
    main()
