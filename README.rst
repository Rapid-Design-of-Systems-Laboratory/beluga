beluga
======

.. image:: https://cdn.jsdelivr.net/gh/Rapid-Design-of-Systems-Laboratory/beluga@master/rdsl.png
    :align: right

.. _GitHub: https://github.com/Rapid-Design-of-Systems-Laboratory/beluga/releases

.. _PyPI: https://pypi.org/project/beluga/

.. _Documentation: http://beluga.readthedocs.io/en/latest/?badge=latest

.. _contributing: https://github.com/Rapid-Design-of-Systems-Laboratory/beluga/blob/master/CONTRIBUTING.md

+---------------+-----------------+----------------+------------+
| Linux         | Windows         | Documentation_ | Coverage   |
+===============+=================+================+============+
| |travisbadge| | |appveyorbadge| |    |docs|      | |coverage| |
+---------------+-----------------+----------------+------------+

.. |travisbadge| image:: https://travis-ci.org/Rapid-Design-of-Systems-Laboratory/beluga.svg?branch=master
    :target: https://travis-ci.org/Rapid-Design-of-Systems-Laboratory/beluga

.. |appveyorbadge| image:: https://ci.appveyor.com/api/projects/status/page1k2q2yeqbyty?svg=true
    :target: https://ci.appveyor.com/project/msparapa/beluga/branch/master

.. |docs| image:: https://readthedocs.org/projects/beluga/badge/?version=latest
    :target: Documentation_

.. |coverage| image:: https://cdn.jsdelivr.net/gh/Rapid-Design-of-Systems-Laboratory/beluga@master/coverage.svg
    :target: https://github.com/Rapid-Design-of-Systems-Laboratory/beluga

Installation
============

Installation using pip
----------------------

If you already have Python 3+ installed along with pip, then do::

    $ pip install beluga

This installs the latest version-controlled distribution of beluga from PyPI_. Examples in this GitHub repo are updated frequently to reflect changes in beluga and as such may not be compatible with the versions on PyPI_. Source code is included with each release, so check under releases on GitHub_ for examples compatible with older versions of beluga. Old examples are also included in the tarballs on PyPI_ and GitHub_ under releases, but are not included in the wheels.

Installation using binaries
---------------------------

Binary files are located on PyPI_ and GitHub_ under releases.

GitHub Version
--------------

See contributing_ for more information on installing the latest version from GitHub, reporting issues, and other information on development.

Running a test problem
======================

Open a terminal window and navigate to the folder where you installed beluga. Type the following commands to run the Brachistochrone problem::

    $ cd examples/2-brachistochrone
    $ python brachisto.py

The solver will proceed to solve the Brachistochrone problem.
