import abc
import tkinter
from mvvm import ViewCollection

_widgets = {
}


class View(abc.ABC):
    context = None
    style = None

    def __init__(self):
        view = ViewCollection()
        view.add(self)
        self.properties = {}

    def property_changed(self, property_name: str):
        """
        This will re-read the given property in the view.
        :param property_name: Property to re-read.
        """
        if isinstance(self.properties[property_name], tkinter.Entry):
            # insert the new value in the entry
            self.properties[property_name].delete(0, tkinter.END)
            self.properties[property_name].insert(
                0, getattr(self.context, property_name)
            )

        elif isinstance(self.properties[property_name], tkinter.Checkbutton):
            # check/uncheck the check button then run it's requisite function
            if getattr(self.context, property_name):
                self.properties[property_name].select()
            else:
                self.properties[property_name].deselect()

        elif isinstance(self.properties[property_name], tkinter.Label):
            # set the label text
            self.properties[property_name].config(
                text=str(getattr(self.context, property_name))
            )

        elif isinstance(self.properties[property_name], tkinter.Listbox):
            # add all items to listbox
            self.properties[property_name].delete(0, tkinter.END)

            for i, item in enumerate(getattr(self.context, property_name)):
                self.properties[property_name].insert(i, str(item))

    def bind_data(self, widget: tkinter.Widget, property_name: str):
        """
        This method binds a function to a widget and sets the callback
        function. For things which are sensible this is a 2-way binding.
        (Anything editable, i.e. not a Label)
        :param widget: tkinter.Widget object
        :param property_name: Property to bind
        """

        # unpythonic code, used for generic data binding as there are different
        # behaviours for different widgets

        if isinstance(widget, tkinter.Entry):
            # bind any key press to setting the contents of the widget to the property
            widget.bind(
                "<KeyRelease>",
                lambda event: setattr(
                    self.context,
                    property_name,
                    event.widget.get()
                )
            )

        if isinstance(widget, tkinter.Checkbutton):
            # a binary value has to be bound to this, calls not on the value
            widget.bind(
                "<Button-1>",
                lambda event: setattr(
                    self.context,
                    property_name,
                    (not getattr(self.context, property_name))
                )
            )

        if isinstance(widget, tkinter.Label):
            # sets the label text to be the property
            widget.config(text=str(getattr(self.context, property_name)))

        if isinstance(widget, tkinter.Listbox):
            # add all items to listbox
            widget.delete(0, tkinter.END)
            for i, item in enumerate(getattr(self.context, property_name)):
                widget.insert(i, str(item))

        # add the widget to the properties list
        self.properties[property_name] = widget
