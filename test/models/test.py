from context import tkmvvm


class TestModel(tkmvvm.model.Model):
    # properties can be stored either in the Model, or on the ViewModel
    entry_data = "A quick brown fox jumps over the lazy dog"
    toggle = False
    items = []
