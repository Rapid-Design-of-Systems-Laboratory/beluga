bvp Solver Module
=================

.. module:: beluga.bvpsol

Introduction
------------

This modules solves :eq:`boundarydifferentialequation` of the form

.. math::
    \begin{aligned}
        \dot{\mathbf{x}} &= \mathbf{f}(\mathbf{x},\mathbf{p}) \\
        \dot{\mathbf{q}} &= \mathbf{g}(\mathbf{x},\mathbf{p}) \\
        \mathbf{\Phi}(\mathbf{x}_0, \mathbf{q}_0, \mathbf{x}_f, \mathbf{q}_f, \mathbf{p}, \mathbf{\lambda}) &= 0 \\
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
    :members: solve

.. autoclass:: Pseudospectral
    :members: solve
