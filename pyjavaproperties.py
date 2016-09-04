# -*- coding: utf-8 *-*

import os
from pyjavaproperties import Properties

APP_PROP_FILE = './config/application.properties'


class MyAppProperties(object):
    """
    Object to manage application.properties as python object properties.

    the properties that are in the APP_PROP_FILE file are assigned to
    MyAppProperties object,  to be accessible in the instance of it.
     When we assigned new properties to instanced object, they are written
    to the APP_PROP_FILE file.
    """

    def __init__(self):
        # Open and load the file. For each file property,
        # we assign it as the property of the object instance
        with open(APP_PROP_FILE, "r") as app_property_file:
            app_properties = Properties()
            app_properties.load(app_property_file)

            for property, value in app_properties.items():
                setattr(self, property, value)

    def __setattr__(self, name, value):
        # For each property assigned to the instance object, we write it to the
        #file, If it doesn't exist we add it.
        app_properties = Properties()
        with open(APP_PROP_FILE, "r") as app_property_file:
            app_properties.load(app_property_file)
            current_properties = app_properties.propertyNames()

        if name not in current_properties or value != app_properties.get(name):
            with open(APP_PROP_FILE, "w") as app_property_file:
                app_properties[name] = value
                app_properties.store(app_property_file)

        super(MyAppProperties, self).__setattr__(name, value)


if __name__ == '__main__':
    my_app_properties  = MyAppProperties()

    # List all object methods.
    print dir(my_app_properties)

    # Edit an existent property. (Verify file change)
    setattr(my_app_properties, "databus.sessionTimeout", "55000")
    print getattr(my_app_properties, "databus.sessionTimeout")

    # Add a new property (non-existent)
    my_app_properties.path_to_some_place = os.path.join(
        "path", "to", "some", "place")
    print my_app_properties.path_to_some_place

    # Add a property with doths. Use the python buildin.
    # setattr y getattr
    setattr(my_app_properties, "other.property.with.point",
            "Awesome!! Another property like Java shit.")
    print getattr(my_app_properties, "other.property.with.point")

    # List  all object mehtods to verify wich ones were added.
    print dir(my_app_properties)
