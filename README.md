# beluga

## Cloning in Github Desktop

If you already have Github installed on your computer, you need to go into preferences and add a new Enterprise account. If this is the first time you installed Github, it should ask you for the login information when you first start it. Click "Add Github Enterprise" and use the following information:

    URL: https://github.rcac.purdue.edu/
    Username : Your purdue account username
    Password : Your purdue account password

This will allow you to view all the repositories you have been given access to.
Go to File -> Clone Repository and you should see "beluga" in the list of repositories to be cloned.

## Setting up the Python development environment
### Mac OSX
  1. Install [anaconda](https://www.continuum.io/downloads/ "Download Anaconda") with Python 3.x
  2. Run the following commands in command line in the folder where you cloned the code
  <pre>
    conda update conda
    conda update --all
    conda env create -f beluga-dev.yml
    source activate beluga-dev
    python setup.py develop
  </pre>

  In case you want to switch to another version of the code in a separate folder, run the following commands to "uninstall" the current version and switch to the new codebase. You do not have to worry about this part if you intend to work with only one version of the code at any time.
  <pre>
  python setup.py develop --uninstall
  cd your_new_code_folder
  python setup.py develop
  </pre>


  3. Get a text editor or development environment of your choice. My favorite is [Atom](http://atom.io). Others recommend [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/).

  4. Start coding!

### Windows
I don't know lol!

### Linux

## Running a test problem

Open a terminal window and navigate to the folder where you installed beluga. Type the following commands to run the Brachistochrone problem

    cd examples/brachistochrone
    python brachisto.py

The program will prompt you to enter the root directory of the solver. Press enter if the option shown is correct. The solver will proceed to solve the Brachistochrone problem.

## Running unit tests

*Note: As of now, it is required that at least one test problem be run before the unit tests start working. This is something to be fixed.*

Run the shell script "run_tests.sh" to run all the unit tests in the software package.
