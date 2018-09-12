bvp Solver Module
=================

.. module:: beluga.bvpsol
.. module:: beluga.bvpsol.algorithms

Introduction
------------

This modules solves :eq:`boundarydifferentialequation` of the form

.. math::
    \begin{aligned}
        \dot{\mathbf{x}} &= \mathbf{f}(t,\mathbf{x},\mathbf{p}) \\
        \dot{\mathbf{q}} &= \mathbf{g}(t,\mathbf{x},\mathbf{p}) \\
        \mathbf{\Phi}(t_0, t_f, \mathbf{x}_0, \mathbf{x}_f, \mathbf{q}_0, \mathbf{q}_f) &= 0 \\
    \end{aligned}
    :label: boundarydifferentialequation

from :math:`t_0` to :math:`t_f`.

Shooting Methods
----------------

Collocation Methods
-------------------

Base Class Reference
--------------------
.. autoclass:: BaseAlgorithm

.. autoclass:: Shooting
    :members: solve

.. autoclass:: Collocation
    :members: __new__, solve
