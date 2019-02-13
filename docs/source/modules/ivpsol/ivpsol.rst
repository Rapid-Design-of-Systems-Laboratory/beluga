ivp Solver Module
=================

.. module:: beluga.ivpsol

Introduction
------------

This modules solves :eq:`ordinarydifferentialequation` of the form

.. math::
    \begin{aligned}
        \dot{x} &= f(\mathbf{x}, \mathbf{p}) \\
        \dot{q} &= h(\mathbf{x}, \mathbf{p}) \\
        \mathbf{x}(\tau_0) &= \mathbf{x}_0
    \end{aligned}
    :label: ordinarydifferentialequation

from :math:`t_0` to :math:`t_f`.

Integration Programs
--------------------

The ivpsol module serves as a common interface to various integration programs as well as an ivp solver included with
beluga. The following link contains a list of integration methods available in beluga.

.. toctree::
    :maxdepth: 2

    integrationmethods.rst

Base Class Reference
--------------------
.. autoclass:: Algorithm
    :members:

.. autoclass:: Propagator
    :members: __new__, __call__

.. autoclass:: Trajectory
    :members: __new__, __call__, set_interpolate_function

.. autofunction:: reconstruct

.. autofunction:: integrate_quads

.. autoclass:: Flow
    :members: __new__, __call__

.. autoclass:: TimeStepper

.. autoclass:: RKMK
    :members: __new__, __call__

.. autoclass:: Method
    :members: __new__
