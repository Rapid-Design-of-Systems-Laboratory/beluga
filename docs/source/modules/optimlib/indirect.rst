.. _indirect:

================
Indirect Methods
================

Indirect method of optimization based on Bryson-Ho [1]_.

Controls are handled in one of two ways. ICRM [2]_ [3]_ or PMP.

Path constraints are handled in one of two ways. ICRM [2]_ [3]_ or UTM [4]_ [5]_

Base Class Reference
--------------------

.. module:: beluga.optimlib.indirect

.. autofunction:: ocp_to_bvp

References
----------

.. [1] Arthur E. Bryson, and Yu-Chi Ho. "Applied Optimal Control: Optimization, Estimation, and Control." Hemisphere, New York (1975).

.. [2] Thomas Antony, and Michael J. Grant. "Path Constraint Regularization in Optimal Control Problems using Saturation Functions." 2018 AIAA Atmospheric Flight Mechanics Conference. 2018.

.. [3] Antony, Thomas. "Large Scale Constrained Trajectory Optimization Using Indirect Methods." Dissertation. Purdue University, West Lafayette, 2018.

.. [4] Kshitij Mall, and Michael J. Grant. "Trigonomerization of Optimal Control Problems with Bounded Controls." AIAA Atmospheric Flight Mechanics Conference. 2016.

.. [5] Kshitij Mall. "Advancing Optimal Control Theory using Trigonometry for Solving Complex Aerospace Problems." Dissertation. Purdue University, West Lafayette, 2018.
