# beluga <img align="right" src="https://raw.githubusercontent.com/msparapa/beluga/master/rdsl.png">

[![Build Status](https://travis-ci.org/msparapa/beluga.svg?branch=master)](https://travis-ci.org/msparapa/beluga)

## Cloning in Github Desktop

If you already have Github installed on your computer, you need to go into preferences and add a new account. If this is the first time you installed Github, it should ask you for the login information when you first start it. Use the following information:

    URL: https://github.com/
    Username : Your account username
    Password : Your account password

This will allow you to view all the repositories you have been given access to.
Go to File -> Clone Repository and you should see "beluga" in the list of repositories to be cloned.

Alternatively, clone using the command line with

    git clone https://github.com/Rapid-Design-of-Systems-Laboratory/beluga

## Setting up the Python development environment

  1. Install [anaconda](https://www.continuum.io/downloads/ "Download Anaconda") with Python 3.x
  2. Run the following commands in command line in the folder where you cloned the code
  
    conda update conda
    conda update --all
    python setup.py develop

  In case you want to switch to another version of the code in a separate folder, run the following commands to "uninstall" the current version and switch to the new codebase. You do not have to worry about this part if you intend to work with only one version of the code at any time.
  
    python setup.py develop --uninstall
    cd your_new_code_folder
    python setup.py develop
    beluga --config

  Enter all the information that is requested.

  3. Get a text editor or development environment of your choice. My favorite is [Atom](http://atom.io). Some of the recommended addons for Atom are: TODO-show, minimap, linter, linter-pep8, minimap-linter, highlight-selected, minimap-highlight-selected and many more.  [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/). is another editor you may want to check out.

  4. Start coding!

## Running a test problem

Open a terminal window and navigate to the folder where you installed beluga. Type the following commands to run the Brachistochrone problem

    cd examples/brachistochrone
    beluga brachisto.py

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

## Coding new features

1. Start a new issue: (!) Issues on GitHub

    a. `git pull` Make sure you have the latest copy of **master**.
    
    b. `git checkout -b I# master` Create the **I#** branch locally based upon the **master** branch.
    
    c. `git push -u origin I#` Create the branch on the server.
    
2. Write code and push commits:

    a. Each commit message should begin with `Ref ##` to reference the issue number (i.e. `Ref #1` to reference issue #1)

    b. `git push` Push latest commits to the server.
    
3. End a task: (from **master**)

    a. `git checkout master` Set **master** as the working branch locally.
    
    b. `git branch -D I#` Delete **I#** locally. You no longer need it because everything is pushed to the server.
    
    c. `git merge --no-ff origin/I#` Merge the task into **master** and preserving branch history. All changes in **master** will show up as a single commit keeping the log simpler. The complete commit history will be preserved in **I#**.
    
    d. `git push` Push any changes to **master** to the server.
    
    e. `git push origin :I#` Delete **I#** from the server. It will still remain in the history along with every individual commit to it that was pushed, but it won't be cluttering up the workspace.

## Running unit tests

To run unit tests, do

    pytest

in the root directory. Some examples take quite some time to run. Run a faster version by

    pytest beluga/

or running the `run_tests_lite.sh` shell script.
