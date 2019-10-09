.. _Brachistochrone: https://en.wikipedia.org/wiki/Brachistochrone_curve

.. _Composition mapping: https://en.wikipedia.org/wiki/Function_composition

.. _Shooting: https://en.wikipedia.org/wiki/Shooting_method

.. _Collocation: https://en.wikipedia.org/wiki/Collocation_method

Optimal Control
===============

In optimal control theory, we wish to solve problems of the form

.. math::
    \begin{aligned}
        \min_{\boldsymbol{u}} J &= \int_{t_0}^{t_f} L(t, \boldsymbol{x}, \boldsymbol{u}) \; dt + \eta(\boldsymbol{x}(t_f)) \\
        \text{Subject to:}& \\
        \dot{\boldsymbol{x}} &= \mathbf{f}(t, \boldsymbol{x}, \boldsymbol{u}) \\
        0 &= \boldsymbol{\phi}(t_0, \boldsymbol{x}(t_0)) \\
        0 &= \boldsymbol{\xi}(t_f, \boldsymbol{x}(t_f)) \\
        \boldsymbol{g}_{lower} &\leq \boldsymbol{g}(\boldsymbol{x}, \boldsymbol{u}, t) \leq \boldsymbol{g}_{upper}
    \end{aligned}

Setting up a Problem
--------------------

Initialize a new Optimal Control Problem with

>>> import beluga
>>> ocp = beluga.OCP()
<beluga.problem.OCP object at 0x0...>

Define parameters in the Optimal Control Problem with

>>> ocp.<parameter>(value1, value2, ..., valuen)

for example

>>> ocp.independent('t', 's')

defines the independent variable :math:`t` with units of :math:`s` representing "seconds". Info for available parameters are included in the OCP documentation.

.. include:: ../../examples/README.rst

Base Class Reference
--------------------

.. autoclass:: beluga.OCP
    :members: constant, control, get_constants, get_controls, get_independent, get_initial_cost, get_path_constraints, get_path_cost, get_quantities, get_switches, get_terminal_cost, independent, initial_cost, path_constraint, path_cost, terminal_cost
    :noindex:
