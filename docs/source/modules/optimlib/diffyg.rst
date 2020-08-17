.. _diffyg:

===============
Diffy G Methods
===============

Indirect method of optimization based on Differential Geometry [1]_.

Controls are handled in one of two ways: Symplectic ICRM [1]_ [2]_ or PMP.

Path constraints are handled in one of two ways: UTM [3]_ [4]_ [5]_ [6]_ or epsilon-trig [3]_ [4]_

Inequality boundary constraints are handled using UTM [7]_.

Switching conditions are handled using RASHS [8]_.

Base Class Reference
--------------------

.. module:: beluga.optimlib.diffyg

.. autofunction:: ocp_to_bvp

References
----------

.. [1] Michael J. Sparapany. Aerospace Mission Design on Quotient Manifolds. Dissertation. Purdue University Graduate School, 2020.

.. [2] Michael J. Sparapany, and Michael J. Grant. "The Geometric Adjoining of Optimal Information in Indirect Trajectory Optimization." 2018 AIAA Guidance, Navigation, and Control Conference. 2018.

.. [3] Kshitij Mall, and Michael J. Grant. "Epsilon-Trig Regularization for Bang-Bang Optimal Control Problems." Journal of Optimization Theory and Applications, Vol. 174, No. 2, 2017, pp. 500-517

.. [4] Kshitij Mall, and Michael J. Grant. "Trigonomerization of Optimal Control Problems with Bounded Controls." AIAA 2016-3244, AIAA Atmospheric Flight Mechanics Conference, Washington D.C., 13-17 Jun. 2016

.. [5] Kshitij Mall, and Michael J. Grant. "Trigonomerization of Optimal Control Problems with Mixed State-Control Constraints." Journal of Optimization Theory and Applications. [Submitted]

.. [6] Kshitij Mall. "Advancing Optimal Control Theory using Trigonometry for Solving Complex Aerospace Problems." Dissertation. Purdue University, West Lafayette, 2018

.. [7] Nolan, Sean M., Michael J. Sparapany, and Daniel A. DeLaurentis. "Extension of Unified Trigonometrization Method to Enforce Inequality Boundary Conditions in Optimal Control Problems." AIAA AVIATION 2020 FORUM. 2020.

.. [8] Harish Saranathan, and Michael J. Grant. "The Relaxed Autonomously Switched Hybrid System (RASHS) Approach to Indirect Multi-Phase Trajectory Optimization for Aerospace Vehicles." AIAA 2018-0016, 2018 AIAA Atmospheric Flight Mechanics Conference. 2018
