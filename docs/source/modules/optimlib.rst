Indirect Optimization Library Module
====================================

.. module:: beluga.optimlib

Introduction
------------

This module automates the indirect optimization process.

+------------------------+
| Valid methods          |
+========================+
| direct                 |
+------------------------+
| traditional (brysonho) |
+------------------------+
| icrm                   |
+------------------------+
| diffyg                 |
+------------------------+

Direct
------

Bryson Ho
---------

ICRM
----

Diffy G
-------

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
