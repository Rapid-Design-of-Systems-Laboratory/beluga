.. _indirect:

================
Indirect Methods
================

Indirect method of optimization based on Bryson-Ho [1]_.

Controls are handled in one of two ways. ICRM [2]_ [3]_ or PMP.

Path constraints are handled in one of two ways. ICRM [2]_ [3]_ or UTM [4]_ [5]_ [6]_ [7]_

.. From Mall: "use [4] for bang-bang and singular control problems"
    "Use [5] for problems with control constraints"
    "Use [6] for problems with mixed state and control constraints (q=0)"
    "Use [7] as catch-all (thesis)"

Base Class Reference
--------------------

.. module:: beluga.optimlib.indirect

.. autofunction:: ocp_to_bvp

References
----------

.. [1] Arthur E. Bryson, and Yu-Chi Ho. "Applied Optimal Control: Optimization, Estimation, and Control." Hemisphere, New York (1975)

.. [2] Thomas Antony, and Michael J. Grant. "Path Constraint Regularization in Optimal Control Problems using Saturation Functions." 2018 AIAA Atmospheric Flight Mechanics Conference. 2018

.. [3] Antony, Thomas. "Large Scale Constrained Trajectory Optimization Using Indirect Methods." Dissertation. Purdue University, West Lafayette, 2018

.. [4] Kshitij Mall, and Michael J. Grant. "Epsilon-Trig Regularization for Bang-Bang Optimal Control Problems." Journal of Optimization Theory and Applications, Vol. 174, No. 2, 2017, pp. 500-517

.. [5] Kshitij Mall, and Michael J. Grant. "Trigonomerization of Optimal Control Problems with Bounded Controls." AIAA 20163244, AIAA Atmospheric Flight Mechanics Conference, Washington D.C., 13-17 Jun. 2016

.. [6] Kshitij Mall, and Michael J. Grant. "Trigonomerization of Optimal Control Problems with Mixed State-Control Constraints." Journal of Optimization Theory and Applications. [Submitted]

.. [7] Kshitij Mall. "Advancing Optimal Control Theory using Trigonometry for Solving Complex Aerospace Problems." Dissertation. Purdue University, West Lafayette, 2018
