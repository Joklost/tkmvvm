import abc
import mvvm
import model
from typing import Union


class ViewModel(mvvm.NotifyPropertyChanged, abc.ABC):
    # used to store current selection in a listbox widget
    current_selection = ()

    def on_property_changed(self, property_name: str):
        self._property_changed(property_name)

    def __init__(self, model_: Union[None, model.Model]):
        self.model = model_
