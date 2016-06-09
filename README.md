# beluga

## Cloning in Github Desktop

If you already have Github installed on your computer, you need to go into preferences and add a new Enterprise account. If this is the first time you installed Github, it should ask you for the login information when you first start it. Click "Add Github Enterprise" and use the following information:

    URL: https://github.rcac.purdue.edu/
    Username : Your Purdue account username
    Password : Your Purdue account password

This will allow you to view all the repositories you have been given access to.
Go to File -> Clone Repository and you should see "beluga" in the list of repositories to be cloned.

## Setting up the Python development environment

  1. Install [anaconda](https://www.continuum.io/downloads/ "Download Anaconda") with Python 3.x
  2. Run the following commands in command line in the folder where you cloned the code
  <pre>
    conda update conda
    conda update --all
    python setup.py develop
  </pre>

  In case you want to switch to another version of the code in a separate folder, run the following commands to "uninstall" the current version and switch to the new codebase. You do not have to worry about this part if you intend to work with only one version of the code at any time.
  <pre>
  python setup.py develop --uninstall
  cd your_new_code_folder
  python setup.py develop
  beluga --config
  </pre>

  Enter all the information that is requested.

  3. Get a text editor or development environment of your choice. My favorite is [Atom](http://atom.io). Some of the recommended addons for Atom are: TODO-show, minimap, linter, linter-pep8, minimap-linter, highlight-selected, minimap-highlight-selected and many more.  [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/). is another editor you may want to check out.

  4. Start coding!

## Running a test problem

Open a terminal window and navigate to the folder where you installed beluga. Type the following commands to run the Brachistochrone problem

    cd examples/brachistochrone
    beluga brachisto

The solver will proceed to solve the Brachistochrone problem.

### A note about logging
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

## Running unit tests

*Note: As of now, it is required that you run the configurtion tool before the unit tests start working. This is something to be fixed.*

Run the shell script "run_tests.sh" to run all the unit tests in the software package.
