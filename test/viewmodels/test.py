from context import tkmvvm


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
    @property
    def toggle(self):
        return self.model.toggle

    @toggle.setter
    def toggle(self, value):
        print('pis')
        self.model.toggle = value
        self.on_property_changed('toggle')

    #######################################################

    #######################################################
    @property
    def items(self):
        return self.model.items

    @items.setter
    def items(self, value):
        self.model.items = value
        self.on_property_changed('items')

    def items_append(self, value):
        self.model.items.append(value)
        self.on_property_changed('items')

    #######################################################

    #######################################################
    def iterate_iterator(self):
        self.iterator = self.iterator + 1

    def reset_entry(self):
        # this will call the setter for entry_data, and in turn update the View
        self.entry_data = ""

    def add_listbox_entry(self):
        self.items_append("A quick brown fox jumps over the lazy dog")

    def remove_listbox_entry(self):
        if not self.current_selection:
            return

        self.items = [item for i, item in enumerate(self.model.items) if i not in self.current_selection]
        self.current_selection = ()

    #######################################################

