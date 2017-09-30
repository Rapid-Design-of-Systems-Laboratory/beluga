"""
Contains classes and functions related to Optimal Control.

Module: optimlib
"""

from .brysonho import *

def sigmoid_two_sided(x, ub, lb, slopeAtZero=1):
    """Two-sided saturation function based on the sigmoid function."""
    pass


def sigmoid_one_sided(x, ub=None, lb=None, slopeAtZero=1):
    """
    One-sided saturation function based on the sigmoid function.

    Only of the bounds must be defined.
    """
    pass

# Implement workflow using simplepipe and functions defined above
ICRM = sp.Workflow([
    sp.Task(process_quantities,
            inputs=('quantities'),
            outputs=('quantity_vars', 'quantity_list', 'derivative_fn')),

    sp.Task(ft.partial(make_augmented_cost, location='initial'),
            inputs=('initial_cost', 'constraints'),
            outputs=('aug_initial_cost')),
    sp.Task(ft.partial(make_aug_params, location='initial'),
            inputs=('constraints'),
            outputs=('initial_lm_params')),

    sp.Task(ft.partial(make_augmented_cost, location='terminal'),
            inputs=('terminal_cost', 'constraints'),
            outputs=('aug_terminal_cost')),
    sp.Task(ft.partial(make_aug_params, location='terminal'),
            inputs=('constraints'),
            outputs=('terminal_lm_params')),
    sp.Task(make_hamiltonian_and_costates,
            inputs=('states', 'path_cost', 'derivative_fn'),
            outputs=('ham', 'costates')),
    sp.Task(ft.partial(make_boundary_conditions, location='initial'),
            inputs=('constraints', 'states', 'costates', 'aug_initial_cost', 'derivative_fn'),
            outputs=('bc_initial')),
    sp.Task(ft.partial(make_boundary_conditions, location='terminal'),
            inputs=('constraints', 'states', 'costates', 'aug_terminal_cost', 'derivative_fn'),
            outputs=('bc_terminal')),
    sp.Task(make_time_bc, inputs=('constraints', 'bc_terminal'), outputs=('bc_terminal')),
    sp.Task(make_dhdu,
            inputs=('ham', 'controls', 'derivative_fn'),
            outputs=('dhdu')),
    sp.Task(make_control_law,
            inputs=('dhdu','controls'),
            outputs=('control_law')),

    sp.Task(generate_problem_data,
            inputs='*',
            outputs=('problem_data')),
], description='Traditional optimal control workflow')


# Call doctest if the script is run directly
if __name__ == "__main__":
    import doctest
    doctest.testmod()
