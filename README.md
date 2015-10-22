Scripting API
=============

This will be the main way for interacting with the individual nodes. This
library will also create a uniform interface/method for logging events and
interacting with the database.


Usage
-----

A simple example for what working with a node will look like:

    with open_node("name") as n:
        n.set("on", 1)

All logging (both event and error logging) will take place behind the scenes.


Development
-----------

To do development work on this library, all libraries needed can be managed
with virtualenv. To create a new virtual environment for this project, use the
following commands from this directory:

    $ virtualenv ./
    $ source bin/activate
    $ pip install -r package_list.txt



