.. |plot0| image:: https://rawgit.com/Rapid-Design-of-Systems-Laboratory/beluga/master/examples/1-brachistochrone/plot0.png

.. |plot1| image:: https://rawgit.com/Rapid-Design-of-Systems-Laboratory/beluga/master/examples/1-brachistochrone/plot1.png

.. |plot2| image:: https://rawgit.com/Rapid-Design-of-Systems-Laboratory/beluga/master/examples/1-brachistochrone/plot2.png

Brachistochrone Problem
=======================

|plot0|

Here, we're going to solve the Brachistochrone problem. First, import :code:`beluga` and :code:`logging`. :code:`beluga` is the optimal control solver and :code:`logging` will keep track of solver progress. We will also need pi (3.14) and a plotting tool. We will use the :code:`Python` built-in :code:`math.pi` and :code:`matplotlib`'s :code:`pyplot` module, but any approximation of :math:`\pi` and plotting tool will do::

    import beluga
    import logging
    from math import pi
    import matplotlib.pyplot as plt

Initialize an optimal control problem in :code:`beluga` using::

    ocp = beluga.OCP('brachistochrone')

Next, we define the independent variable. In most problems, this is usually time::

    ocp.independent('t', 's')

As you can see, this has syntax of :code:`ocp.independent(variable_name, variable_units)`. The solver will take units into account for all inputs and attempt to automatically nondimensionalize problems. Next, we need to define the dynamic constraints (equations of motion) that must be satisfied. The syntax is :code:`ocp.state(state_name, state_rate, state_units)`::

    ocp.state('x', 'v*cos(theta)', 'm')
    ocp.state('y', 'v*sin(theta)', 'm')
    ocp.state('v', 'g*sin(theta)', 'm/s')

Note that we have used :code:`theta` in describing the rates of change, however they have not been defined yet. This is OK since it is a control variable and we are just defining an input script. The solver will figure out what the each term is based on it's definition. Next, we will define the control variable for our system with the syntax :code:`ocp.control(control_name, control_units)`::

    ocp.control('theta','rad')

These control variables are the parameters in the optimization package :code:`beluga`. To define non-optimization type quantities, use the :code:`constant` method::

    ocp.constant('g', -9.81, 'm/s^2')

In a single given optimization problem, gravity will not change, therefore the :code:`ocp.constant(const_name, const_val, const_units)` method was used. Next, let's define the path cost to minimize, :math:`L`::

    ocp.path_cost('1', 's')

For the Brachistochrone, we want to minimize time of travel. Therefore by integrating :math:`\int 1 \circ \gamma \; dt= \int 1 \; dt = t_f - t_0`, we are minimizing :math:`t_f - t_0`. We would like the bead to start and stop at specific locations, so let's set some boundary conditions::

    ocp.constraints()
    ocp.initial('x', 'm')
    ocp.initial('y', 'm')
    ocp.initial('v', 'm/s')
    ocp.terminal('x-x_f', 'm')
    ocp.terminal('y-y_f', 'm')

We are fixing :math:`x` to start at the position, or rather the boundary condition :math:`x = 0` must be satisfied. The astute dynamicist will recognize that :math:`v_f` is free. :code:`beluga` can interpret a multitude of boundary conditions. Next, define the units in terms of states that have been define so the solver knows how to automatically scale all the variables::

    ocp.scale(m='y', s='y/v', kg=1, rad=1)

We told the solver that a meter is 1 :math:`y` and a meter per second is 1 :math:`y/v`. We also told it that kilograms and radians don't need to be scaled. Next, let's choose a numerical solver. Shooting sounds good::

    bvp_solver = beluga.bvp_algorithm('Shooting')

The :code:`Shooting` solver usually ends up being one of the best choices, however Collocation fundamentally works differently and, if a problem has a tough time with :code:`Shooting`, then :code:`Collocation` might be able to get the job done. To use :code:`Collocation` instead, just use::

    bvp_solver = beluga.bvp_algorithm('Collocation')

Now we have a problem and a solver, but that's not enough to solve the problem at hand. Optimal control problems are notoriously difficult and sensitive, so they need a good initial guess. Let's guess a solution to the Brachistochrone problem::

    guess_maker = beluga.guess_generator('auto', start=[0,0,0], direction='forward', costate_guess = -0.1)

So we guessed that :code:`beluga` will automatically handle us propagating forward with the initial positions of each of our states at 0, 0, and 0. Considering our initial boundary conditions were 0's, that wasn't difficult. On the other hand, :code:`beluga` uses methods that are typically known as `indirect methods`. Therefore it generates mathematical entities known as :code:`costates` with, potentially, no physical meaning. An initial guess is given for these as well. Since our first problem is small, some -0.1's will do nicely. So we came up with a guess, now let's string together a bunch of smaller optimal control problems to solve a much larger one, or rather a continuation set::

    continuation_steps = beluga.init_continuation()
    continuation_steps.add_step('bisection')
    continuation_steps[-1].num_cases(21)
    continuation_steps[-1].const('x_f', 10)
    continuation_steps[-1].const('y_f',-10)

So when we created :code:`continuation_steps`, it behaves likes a :code:`Python list()`. In this case there's only 1 continuation set. What this continuation set does is it drags out the terminal boundary conditions, :math:`x_f` and :math:`y_f`, to (10, -10). It will do this in 21 evenly spaced steps, using the previous solution as an initial guess into the next. Optimal control theory can be difficult, and even the simplest of problems won't converge, so lets use our :code:`logging` package to keep track of the output and progress::

    beluga.add_logger(logging_level=logging.DEBUG)

Finally. with all of the components defined let's solve the output::

    sol = beluga.solve(ocp, method='traditional', bvp_algorithm=bvp_solver, steps=continuation_steps, guess_generator=guess_maker)

We told :code:`beluga` to use the `traditional` method of optimal control theory based on Pontryagin's Minimum Principle. There are other choices available (RST LINK TO BELUGA CHOICES). The :code:`sol` result will take in a time and give out position and the optimal control. To use :code:`sol`, see (RST LINK TO TRAJECTORY()). To plot the trajectory, use :code:`matplotlib.pyplot`::

    plt.plot(sol.y[0], sol.y[1])
    plt.show()


|plot1|

|plot2|
