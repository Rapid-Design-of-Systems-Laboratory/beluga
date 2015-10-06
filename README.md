# beluga

## Cloning in Github Desktop

If you already have Github installed on your computer, you need to go into preferences and add a new Enterprise account. If this is the first time you installed Github, it should ask you for the login information when you first start it. 
Use the following information:

    URL: https://github.rcac.purdue.edu/
    Username : Your purdue account username
    Password : Your purdue account password

This will allow you to view all the repositories you have been given access to. 
Go to File -> Clone Repository and you should see "beluga" in the list of repositories to be cloned.

## Setting up the Python development environment
### Mac OSX
  1. Install [anaconda]((https://www.continuum.io/downloads "Download Anaconda") with Python 3.x
  2. Run the following commands in command line
  <pre>
    conda update conda
    conda update --all
    conda install accelerate iopro
    pip install pystache dill multiprocessing_on_dill
  </pre>

  3. Open ~/.bash_profile in a text editor
  <pre>
    export PYTHONPATH="/Users/tantony/dev/beluga:$PYTHON_PATH"
  </pre>
  The path in the above command should point to wherever you have installed beluga.
  
### Windows
    setx PYTHONPATH "E:\\Blah\\Foo\\mjgrant-beluga"
### Linux 
  
## Running a test problem
   
Open a terminal window and navigate to the folder where you installed beluga. Type the following commands to run the Brachistochrone problem

    cd examples
    python brachisto.py
    
The program will prompt you to enter the root directory of the solver. Press enter if the option shown is correct. The solver will proceed to solve the Brachistochrone problem.

## Running unit tests

Note: As of now, it is required that at least one test problem be run before the unit tests start working. This is something to be fixed.

Run the shell script "run_tests.sh" to run all the unit tests in the software package.
