from beluga.optimlib.functional_maps.prob_maps import *


def ocp_to_bvp(ocp: SymOCP,
               method='traditional',
               control_method='differential',
               analytical_jacobian=True,
               momentum_shift=True,
               scale_time=True,
               reduction=False
               ):
    """
    Converts an OCP to a BVP using indirect methods.

    :param ocp:
    :param method:
    :param control_method:
    :param analytical_jacobian:
    :param momentum_shift:
    :param scale_time:
    :param reduction:
    :return:
    """

    prob_chain = [ocp]
    map_chain = []

    """
    Make independent variable a state
    """
    if momentum_shift:
        ocp, mapper = f_momentum_shift(ocp)
        prob_chain.append(ocp)
        map_chain.append(mapper)

    """
    Handle Path constraints
    """
    for path_constraint in ocp.constraints['path']:
        if path_constraint['method'] is None:
            raise NotImplementedError
        elif path_constraint['method'].lower() == 'epstrig':
            ocp, mapper = f_epstrig(ocp)
        elif path_constraint['method'].lower() == 'utm':
            ocp, mapper = f_utm(ocp)
        else:
            raise NotImplementedError(
                'Unknown path constraint method \"' + str(path_constraint['method'].lower()) + '\"')

        prob_chain.append(ocp)
        map_chain.append(mapper)

    """
    Deal with staging, switches, and their substitutions
    """
    if ocp.switches:
        ocp, mapper = f_rashs(ocp)
        prob_chain.append(ocp)
        map_chain.append(mapper)

    """
    Dualize the problem.
    """
    dual, mapper = f_dualize(ocp, method=method)
    prob_chain.append(dual)
    map_chain.append(mapper)

    """
    Build control law
    """
    if control_method.lower() == 'algebraic':
        dual, mapper = f_algebraic_control_law(dual)
    elif control_method.lower() == 'differential':
        dual, mapper = f_differential_control_law(dual, method=method)
    elif control_method.lower() == 'numerical':
        raise NotImplementedError('Numerical control method not implemented yet')
    else:
        raise NotImplementedError('Unknown control method {}'.format(control_method))

    prob_chain.append(dual)
    map_chain.append(mapper)

    """
    Recompose dual problem as BVP
    """
    bvp, mapper = f_squash_to_bvp(dual)
    prob_chain.append(bvp)
    map_chain.append(mapper)

    """
    Scale the EOMs to final time.
    """
    if scale_time:
        bvp, mapper = f_normalize_time(bvp)
        prob_chain.append(bvp)
        map_chain.append(mapper)

    """
    Form analytical Jacobians
    """
    if analytical_jacobian:
        bvp, mapper = f_compute_analytical_jacobians(bvp)
        prob_chain.append(bvp)
        map_chain.append(mapper)

    sol_set = SolSet(bvp)
    sol_set.backward_stack = map_chain

    return bvp, sol_set




