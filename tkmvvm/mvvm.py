import abc


class NotifyPropertyChanged(abc.ABC):
    @abc.abstractmethod
    def on_property_changed(self, property_name: str):
        return

    def _property_changed(self, property_name: str = None):
        """
        Tell the view that property_name has changed.

        :param property_name: if None, update all properties
        """

        single = ViewCollection()
        if property_name is None:
            self._all_properties_changed()
            return

        for view in single.views:
            if property_name in view.properties:
                view.property_changed(property_name)

    @staticmethod
    def _all_properties_changed():
        """
        Tell the view that all properties have changed.
        """
        single = ViewCollection()
        for view in single.views:
            for prop in view.properties:
                view.property_changed(prop)


# noinspection PyArgumentList
class Singleton(object):
    """
    A generic base class to derive any singleton class from.
    """
    __instance = None

    def __new__(cls, *arguments, **keyword_arguments):
        """
        Override the __new__ method, such that it is a singleton.
        """
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            cls.__instance.__init__(*arguments, **keyword_arguments)
        return cls.__instance


class ViewCollection(Singleton):
    instance = None
    views = []

    def __init__(self):
        pass

    def add(self, view):
        self.views.append(view)