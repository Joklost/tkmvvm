from context import tkmvvm
from typing import Union
import ast

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
        self._entry = value
        self.on_property_changed('entry')

    @property
    def computation(self):
        return self._computation

    @computation.setter
    def computation(self, value):
        self._computation = value
        self.on_property_changed('computation')

    def clear_entry(self):
        self.entry = ""

    def clear(self):
        self.entry = ""
        self.computation = ""

    def remove_char(self):
        self.entry = self.entry[:-1]
        if self.entry[-1] == ' ':
            self.entry = self.entry[:-1]

    def divide(self):
        self.entry += ' / '

    def seven(self):
        self.entry += '7'

    def eight(self):
        self.entry += '8'

    def nine(self):
        self.entry += '9'

    def multiply(self):
        self.entry += ' * '

    def four(self):
        self.entry += '4'

    def five(self):
        self.entry += '5'

    def six(self):
        self.entry += '6'

    def subtract(self):
        self.entry += ' - '

    def one(self):
        self.entry += '1'

    def two(self):
        self.entry += '2'

    def three(self):
        self.entry += '3'

    def plus(self):
        self.entry += ' + '

    def zero(self):
        self.entry += '0'

    def dot(self):
        self.entry += '.'

    def equal(self):
        # eval should be "safe" here, as long as the Entry widget bound to self.entry
        # is 'readonly' or 'disabled'!
        try:
            self.computation = eval(self.entry)
        except SyntaxError:
            self.computation = 'Syntax error!'
