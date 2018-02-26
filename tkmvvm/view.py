import abc
import tkinter
import tkinter.ttk
import viewmodel
import mvvm

_widgets = {
}


class View(abc.ABC):
    context = None

    def __init__(self, parent: tkinter.Tk, context: viewmodel.ViewModel):
        self.parent = parent
        self.context = context
        view = mvvm.ViewCollection()
        view.add(self)
        self.properties = {}

    @staticmethod
    def center_window(window, window_width: int, window_height: int):
        """
        Center window in the screen with size window_width x window_height
        """
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def property_changed(self, property_name: str):
        """
        This will re-read the given property in the view.
        :param property_name: Property to re-read.
        """

        if property_name not in self.properties:
            raise ValueError('Property not found: {}'.format(property_name))

        for widget in self.properties[property_name]:

            if isinstance(widget, tkinter.Entry) or isinstance(widget, tkinter.ttk.Entry):
                # insert the new value in the entry
                widget.delete(0, tkinter.END)
                widget.insert(0, getattr(self.context, property_name))

            elif isinstance(widget, tkinter.Checkbutton):
                # check/uncheck the check button then run it's requisite function
                if getattr(self.context, property_name):
                    widget.select()
                else:
                    widget.deselect()

            elif isinstance(widget, tkinter.ttk.Checkbutton):
                # check/uncheck the check button
                widget.invoke()

            elif isinstance(widget, tkinter.Label) or isinstance(widget, tkinter.ttk.Label):
                # set the label text
                widget.config(
                    text=str(getattr(self.context, property_name))
                )

            elif isinstance(widget, tkinter.Listbox):
                # add all items to listbox
                widget.delete(0, tkinter.END)

                for i, item in enumerate(getattr(self.context, property_name)):
                    widget.insert(i, str(item))

            elif isinstance(widget, tkinter.Button) or isinstance(widget, tkinter.ttk.Button):
                # set the button text
                widget.config(
                    text=str(getattr(self.context, property_name))
                )

    def bind_data(self, widget: tkinter.Widget, property_name: str):
        """
        This method binds a function to a widgets and sets the callback
        function. For things which are sensible this is a 2-way binding.
        (Anything editable, i.e. not a Label)
        :param widget: tkinter.Widget object
        :param property_name: Property to bind
        """

        # unpythonic code, used for generic data binding as there are different
        # behaviours for different widgets

        if isinstance(widget, tkinter.Entry) or isinstance(widget, tkinter.ttk.Entry):
            # bind any key press to setting the contents of the widgets to the property
            widget.bind(
                "<KeyRelease>",
                lambda event: setattr(
                    self.context,
                    property_name,
                    event.widget.get()
                )
            )
            # insert the value in the entry
            val = getattr(self.context, property_name)
            if val:
                widget.delete(0, tkinter.END)
                widget.insert(0, val)

        if isinstance(widget, tkinter.Checkbutton) or isinstance(widget, tkinter.ttk.Checkbutton):
            # a binary value has to be bound to this, calls not on the value
            widget.bind(
                "<Button-1>",
                lambda event: setattr(
                    self.context,
                    property_name,
                    (not getattr(self.context, property_name))
                )
            )

        if isinstance(widget, tkinter.Label) or isinstance(widget, tkinter.ttk.Label):
            # sets the label text to be the property
            val = getattr(self.context, property_name)
            widget.config(text=str(val))

        if isinstance(widget, tkinter.Listbox):
            # add all items to listbox
            widget.delete(0, tkinter.END)
            for i, item in enumerate(getattr(self.context, property_name)):
                widget.insert(i, str(item))

        if isinstance(widget, tkinter.Button) or isinstance(widget, tkinter.ttk.Button):
            # sets the button text to be the property
            widget.config(text=str(getattr(self.context, property_name)))

        # add the widgets to the properties list
        if property_name not in self.properties:
            self.properties[property_name] = []
        self.properties[property_name].append(widget)
