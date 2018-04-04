ivp Solver Module
=================

.. module:: beluga.ivpsol

Introduction
------------

This modules solves :eq:`ordinarydifferentialequation` of the form

.. math::
    \begin{aligned}
        \dot{x} &= f(t,x,p) \\
        \dot{q} &= g(t,\mathbf{x},p)
    \end{aligned}
    :label: ordinarydifferentialequation

from :math:`t_0` to :math:`t_f`.

Base Class Reference
--------------------
.. autoclass:: Algorithm
    :members:

.. autoclass:: Collocation
    :members:

.. autoclass:: Propagator
    :members:

.. autoclass:: ivp
    :members:

.. autoclass:: sol
    :members:
