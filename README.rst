tkmvvm
------

MVVM implementation for the Tkinter GUI Python package.

Supports generating interfaces from XML files.

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

Currently Supported Widgets
^^^^^^^^^^^^^^^^^^^^^^^^^^^
These are the widgets with support for either 1-way or 2-way data-binding (depending on the widget).

* Entry
* Button
* Listbox
* Checkbutton (not working as intended)
* Label

TODO:
^^^^
* Add "state"-binding to widgets to control state from program
* Implement data-binding for more widgets (rest of Tk, and all of ttk)
