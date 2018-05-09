.. _atom link: http://atom.io

Installation
============

Cloning in Github Desktop
-------------------------

If you already have Github installed on your computer, you need to go into preferences and add a new account. If this is the first time you installed Github, it should ask you for the login information when you first start it. Use the following information::

    URL: https://github.com/
    Username : Your account username
    Password : Your account password

This will allow you to view all the repositories you have been given access to.
Go to File -> Clone Repository and you should see "beluga" in the list of repositories to be cloned.

Alternatively, clone using the command line with::

    git clone https://github.com/Rapid-Design-of-Systems-Laboratory/beluga

Setting up the Python development environment
---------------------------------------------

1. Install `anaconda <https://www.continuum.io/downloads/>`_ with Python 3.x

2. Run the following commands in command line in the folder where you cloned the code

::

    conda update conda
    conda update --all
    python setup.py develop

In case you want to switch to another version of the code in a separate folder, run the following commands to "uninstall" the current version and switch to the new codebase. You do not have to worry about this part if you intend to work with only one version of the code at any time::

    python setup.py develop --uninstall
    cd your_new_code_folder
    python setup.py develop
    beluga --config

Enter all the information that is requested.

3. Get a text editor or development environment of your choice. My favorite is `Atom <http://atom.io>`_. Some of the recommended addons for Atom are: TODO-show, minimap, linter, linter-pep8, minimap-linter, highlight-selected, minimap-highlight-selected and many more.  `PyCharm Community Edition <https://www.jetbrains.com/pycharm/download/>`_. is another editor you may want to check out.

4. Start coding!

