from context import tkmvvm
from typing import Union


class CalculatorViewModel(tkmvvm.viewmodel.ViewModel):
    _entry = ""
    _computation = ""

    def __init__(self, model: Union[None, tkmvvm.model.Model]):
        super(CalculatorViewModel, self).__init__(model)

    @property
    def entry(self):
        return self._entry

    @entry.setter
    def entry(self, value):
        _entry = value
        self.on_property_changed('entry')

    @property
    def computation(self):
        return self._computation

    @computation.setter
    def computation(self, value):
        _computation = value
        self.on_property_changed('computation')

    def clear_entry(self):
        pass

    def clear(self):
        pass

    def remove_char(self):
        pass

    def divide(self):
        pass

    def seven(self):
        pass

    def eight(self):
        pass

    def nine(self):
        pass

    def multiply(self):
        pass

    def four(self):
        pass

    def five(self):
        pass

    def six(self):
        pass

    def subtract(self):
        pass

    def one(self):
        pass

    def two(self):
        pass

    def three(self):
        pass

    def plus(self):
        pass

    def zero(self):
        pass

    def comma(self):
        pass

    def equal(self):
        pass
