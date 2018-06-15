Indirect Optimization Library Module
====================================

.. module:: beluga.optimlib

Introduction
------------

This module automates the indirect optimization process.

+------------------------+
| Valid methods          |
+========================+
| traditional (brysonho) |
+------------------------+
| icrm                   |
+------------------------+

Bryson Ho
---------

ICRM
----

Base Class Reference
--------------------

.. autofunction:: init_workspace

.. autofunction:: jacobian

.. autofunction:: make_augmented_cost

.. autofunction:: make_augmented_params

.. autofunction:: make_boundary_conditions

.. autofunction:: make_costate_names

.. autofunction:: make_costate_rates

.. autofunction:: make_dhdu

.. autofunction:: make_parameters

.. autofunction:: make_time_bc

.. autofunction:: process_quantities

.. autofunction:: sanitize_constraint_expr

.. autofunction:: total_derivative

.. autofunction:: make_hamiltonian_and_costate_rates

.. autofunction:: make_control_law

.. autofunction:: process_constraint

.. autofunction:: process_path_constraints

.. autofunction:: make_constraint_bc

.. autofunction:: make_constrained_arc_fns

.. autofunction:: generate_problem_data
