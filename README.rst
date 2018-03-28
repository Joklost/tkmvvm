tkmvvm
------

MVVM implementation for the Tkinter GUI Python package.

Supports generating interfaces from XML files.

Sample
^^^^^^

**The View in XML**

.. code:: xml

    <Window xmlns="https://jonaskloster.dk/xml/tkmvvm"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/Joklost/tkmvvm/master/tkmvvm/schema/tkmvvm.xsd"
        height="230" width="150" title="Calculator">
        
        <Entry grid-sticky="nesw" 
               grid-row="0" 
               grid-column="0" 
               grid-columnspan="4" 
               state="readonly" 
               text-binding="{{computation}}" 
               justify="right"/>

        <Button width="2" 
                grid-sticky="nesw" 
                grid-row="1" 
                grid-column="1"
                command="{clear}" 
                text="C"/>
    </Window>

Binding and command attributes attempt to match to a method from the ViewModel. 

The :code:`text-binding="{{computation}}"` attribute will create a 2-way binding with the :code:`computation` property, and the :code:`command="{clear}"` attribute means that the :code:`clear` method will be invoked when this button is clicked.

**The ViewModel**

.. code:: python

    class CalculatorViewModel(ViewModel):
        _entry = ""
        _computation = ""

        def __init__(self):
            super(CalculatorViewModel, self).__init__(None)
    
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
            
        def clear(self):
            self.entry = ""
            self.computation = ""

Adding a Model to the ViewModel is not strictly necessary. The calculator for example has no data to store, which is why no Model is given. Calling the :code:`on_property_changed('computation')` method will force the View to update anything bound to the 'computation' property, and calling the method without any parameters will force the View to update all data bindings.

**The View class**

.. code:: python

    class CalculatorView(View):
        def __init__(self, parent: tkinter.Tk, context: tkmvvm.viewmodel.ViewModel, height: int, width: int):
            super().__init__(parent, context, height, width)
            self.window = tkinter.Toplevel(self.parent)
            self.center_window(self.window)

            # enable quitting when pressing the exit button
            self.window.protocol('WM_DELETE_WINDOW', self.window.quit)

Currently, a View class is needed in order to load a View from XML, but in the future, this will not be needed.

**The Model**

.. code:: python

    class CalculatorModel(Model):
        computation = 0
        computation_history = []
        
The Model is used when you have some data that you want to store, and the Model class will support serialization and deserialization in the future.

**Combining Everything**

.. code:: python

    def main():
        view_model = CalculatorViewModel()
        root = Tk()
        root.withdraw()
        view = CalculatorView(root, view_model, 600, 400)

        view.load_xml('view.xml')
        view.resizeable(False, False)
        view.mainloop()


    if __name__ == '__main__':
        main()
        
You can find the complete Calculator sample in the samples folder.

Currently Supported Widgets
^^^^^^^^^^^^^^^^^^^^^^^^^^^
These are the widgets with support for either 1-way or 2-way data binding (depending on the widget).

* Entry
* Button
* Listbox
* Checkbutton (not working as intended)
* Label

TODO:
^^^^
* Add "state"-binding to widgets to control state from program
* Implement data-binding for more widgets (rest of Tk, and all of ttk)
* Remove the need to creating a View class, when defining the view using XML
* Add serialization and deserialization to Models.
