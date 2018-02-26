from context import tkmvvm


class TestViewModel(tkmvvm.viewmodel.ViewModel):
    def __init__(self):
        super(TestViewModel, self).__init__()



vm = TestViewModel()


def main():
    print("Test")


if __name__ == '__main__':
    main()
