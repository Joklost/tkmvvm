from context import tkmvvm
from typing import Union


class CalculatorViewModel(tkmvvm.viewmodel.ViewModel):
    def __init__(self, model: Union[None, tkmvvm.model.Model]):
        super(CalculatorViewModel, self).__init__(model)
