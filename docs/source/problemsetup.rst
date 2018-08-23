.. _Brachistochrone: https://en.wikipedia.org/wiki/Brachistochrone_curve

.. _Composition mapping: https://en.wikipedia.org/wiki/Function_composition

.. _Shooting: https://en.wikipedia.org/wiki/Shooting_method

.. _Collocation: https://en.wikipedia.org/wiki/Collocation_method

Optimal Control
===============

In optimal control theory, we wish to solve problems of the form

.. math::
    \begin{aligned}
        \min J &= \int_{t_0}^{t_f} L \circ \gamma \; dt + \Phi \circ \gamma \rvert_{t_0} + \Phi \circ \gamma \rvert_{t_f} \\
        \text{Subject to:}& \\
        \mathbf{\dot{x}} &= \mathbf{f}(t, \mathbf{x}, \mathbf{u}) \\
        0 &= \mathbf{\Psi}(t_0, \mathbf{x}_0, t_f, \mathbf{x}_f)
    \end{aligned}

Example Problems
----------------

.. toctree::
    :maxdepth: 2

    examples/1-brachistochrone
    examples/2-planarhypersonic
    examples/3-hypersonic3dof
