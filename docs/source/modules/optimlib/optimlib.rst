====================================
Indirect Optimization Library Module
====================================

.. module:: beluga.optimlib

Introduction
------------

This module automates the indirect optimization process.

+------------------------+
| Valid methods          |
+========================+
| indirect               |
+------------------------+
| diffyg                 |
+------------------------+
| direct                 |
+------------------------+

Indirect and Diffy G
--------------------

Given an OCP :math:`\Sigma`, indirect-style methods create a dual BVP :math:`\Lambda` as follows:

.. math::
    \Lambda = (E \circ \lambda)(\Sigma)

After compiling the resulting BVP :math:`\Lambda`, it can be solved by most algorithms in the :ref:`bvpsol`.

There are two indirect-style methods available. To read more, see:

.. toctree::
    :maxdepth: 2

    indirect.rst
    diffyg.rst

Direct
------

Given an OCP :math:`\Sigma`, direct-style methods pass through the majority of OCP info unmodified. The result is
compiled and discretization occurs in the :ref:`bvpsol`. Not all BVP solvers are compatible with direct-style methods.

Base Class Reference
--------------------

.. autofunction:: init_workspace

.. autofunction:: make_augmented_cost

.. autofunction:: make_augmented_params

.. autofunction:: make_boundary_conditions

.. autofunction:: make_constrained_arc_fns

.. autofunction:: make_control_dae

.. autofunction:: make_control_law

.. autofunction:: make_costate_names

.. autofunction:: make_costate_rates

.. autofunction:: make_dhdu

.. autofunction:: make_time_bc

.. autofunction:: process_quantities

.. autofunction:: sanitize_constraint_expr

.. autofunction:: total_derivative

.. autofunction:: utm_path

.. autofunction:: rash_mult

.. autofunction:: F_momentumshift

.. autofunction:: F_scaletime

.. autofunction:: F_RASHS

.. autofunction:: F_EPSTRIG

.. autofunction:: F_UTM

.. autofunction:: DualizeMapper

.. autofunction:: F_PMP

.. autofunction:: F_ICRM
