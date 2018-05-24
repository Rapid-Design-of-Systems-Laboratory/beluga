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
    :members: __call__

.. autoclass:: ivp
    :members:

.. autoclass:: sol
    :members:

.. autoclass:: trajectory
    :members: __call__

.. autofunction:: reconstruct

.. autofunction:: integrate_quads
