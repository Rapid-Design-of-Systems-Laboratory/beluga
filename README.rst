beluga
======

+---------------+-----------------+---------------+------------+
| Linux         | Windows         | Documentation | Coverage   |
+===============+=================+===============+============+
| |travisbadge| | |appveyorbadge| | |docs|        | |coverage| |
+---------------+-----------------+---------------+------------+

.. |travisbadge| image:: https://travis-ci.org/Rapid-Design-of-Systems-Laboratory/beluga.svg?branch=master
    :target: https://travis-ci.org/Rapid-Design-of-Systems-Laboratory/beluga

.. |appveyorbadge| image:: https://ci.appveyor.com/api/projects/status/page1k2q2yeqbyty?svg=true
    :target: https://ci.appveyor.com/project/msparapa/beluga/branch/master

.. |docs| image:: https://readthedocs.org/projects/beluga/badge/?version=latest
    :target: https://beluga.readthedocs.io/en/latest/?badge=latest

.. |logo| image:: https://raw.githubusercontent.com/msparapa/Rapid-Design-of-Systems-Laboratory/master/rdsl.png
    :align: right

.. |coverage| image:: https://rawgit.com/Rapid-Design-of-Systems-Laboratory/beluga/master/coverage.svg
    :target: https://github.com/Rapid-Design-of-Systems-Laboratory/beluga

Installation
------------

Installation using pip
----------------------

If you already have Python 3+ installed along with pip, then do::

    $ pip install beluga

Installation using binaries
---------------------------

Binary files are located on `PyPI <https://pypi.org/project/beluga/#history>`_ and `GitHub <https://github.com/Rapid-Design-of-Systems-Laboratory/beluga/releases>`_.


Running a test problem
----------------------

Open a terminal window and navigate to the folder where you installed beluga. Type the following commands to run the Brachistochrone problem::

    $ cd examples/brachistochrone
    $ python brachisto.py

The solver will proceed to solve the Brachistochrone problem.
