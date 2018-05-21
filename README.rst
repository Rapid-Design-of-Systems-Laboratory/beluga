beluga
======

.. image:: https://raw.githubusercontent.com/msparapa/beluga/master/rdsl.png

Build Status
.. image:: https://travis-ci.org/msparapa/beluga.svg?branch=master

https://travis-ci.org/msparapa/beluga

Running a test problem
----------------------

Open a terminal window and navigate to the folder where you installed beluga. Type the following commands to run the Brachistochrone problem

    cd examples/brachistochrone
    beluga brachisto.py

The solver will proceed to solve the Brachistochrone problem.

A note about logging
--------------------

A logging system has been added to the solver. It is recommended that this is used instead of "print" statements in your code. Use statements such as :

    logging.debug('This is a random debug statement: '+some_variable)
    logging.info('Info message about status of something')
    logging.warning('Some warning message')
    logging.error('Some error message')

This allows you suppress or display only certain kind of messages. You will no longer have to worry about stray print messages. This also allows the creation of a logfile. The logfile is created in the current directory by default and is named `beluga.log`. This can be changed using the configuration tool.

Run the command `beluga -h` in order to see the command line arguments used to control this behavior. For example:

    beluga -lINFO -dALL brachisto   # log any messages higher then INFO
                                    # and display all messages
    beluga -d0 brachisto            # display all messages (including debug)
    beluga -q brachisto             # Quiet mode -- no console output
    beluga -q --nolog brachisto     # Quiet mode and logging suppressed

The default logging level is "error" and display level is "info". The logging levels in increasing order of priority are: debug, info, error, warning and critical. The level you specify in your commandline is the minimum priority level to display/log. Any messages with lower priority levels are suppressed.



Find more information about logging and logging levels here:
http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python
https://docs.python.org/3/howto/logging.html
