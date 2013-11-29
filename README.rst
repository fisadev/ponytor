Ponytor
=======

A small command line utility and python lib to run automated things when files change 


Installation
============

.. code-block:: bash

    sudo pip install ponytor


Usage - as command line tool
============================

Syntax:

.. code-block:: bash

    ponytor PATH_TO_WATCH COMMAND_TO_RUN

Example: this will run the working_on_this.py file each time it's changed (saved), printing the date of the run.

.. code-block:: bash

    ponytor working_on_this.py "echo `date` && python working_on_this.py"


Usage - as a python lib
=======================

The usage is really simple:

.. code-block:: python

    from ponytor import monitor

    monitor('/path/to/monitor.txt', function_to_run_on_change)

Example: the same as the command line tool usage example

.. code-block:: python

    from os import system
    from ponytor import monitor

    def my_callback():
        system('echo `date`')
        system('python working_on_this.py')

    monitor('working_on_this.py', my_callback)

Or, a simpler way:

.. code-block:: python

    from os import system
    from ponytor import monitor, build_command_callback

    monitor('working_on_this.py', 
            build_command_callback('echo `date` && python working_on_this.py')

