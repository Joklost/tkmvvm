import abc
import mvvm
import model


class ViewModel(mvvm.NotifyPropertyChanged, abc.ABC):
    def on_property_changed(self, property_name: str):
        self._property_changed(property_name)

    def __init__(self, model: model.Model):
        self.model = model
