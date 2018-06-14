ivp Solver Module
=================

.. module:: beluga.ivpsol

Introduction
------------

This modules solves :eq:`ordinarydifferentialequation` of the form

.. math::
    \begin{aligned}
        \dot{x} &= f(t,\mathbf{x}, \mathbf{p}) \\
        \dot{q} &= g(t,\mathbf{x}, \mathbf{p}) \\
        \mathbf{x}(t_0) &= \mathbf{x}_0
    \end{aligned}
    :label: ordinarydifferentialequation

from :math:`t_0` to :math:`t_f`.

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
