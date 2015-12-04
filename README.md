**WARNING: DEPRECATED**

A more up-to-date version of this library is included in the server repository


Scripting API
=============

This will be the main way for interacting with the individual nodes. This
library will also create a uniform interface/method for logging events and
interacting with the database.


Usage
-----

A simple example for what working with a node will look like:

    from haapi import NodeConnection
    with NodeConnection("name") as n:
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


Running Tests
-------------

To run the tests, use the following command:

    $ python -m unittest discover tests

Alternatively, if you want to use pytest:

    $ pip install pytest
    $ py.test tests


