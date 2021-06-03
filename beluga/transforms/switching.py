import sympy

from beluga.data_classes.symbolic_problem import Problem


def regularize_switch(prob: Problem, switch_idx: int = 0):
    switch = prob.switches.pop(switch_idx)

    switch_fun = sum([function * sum([1 / (1 + sympy.exp(condition / switch.tol_param))
                                      for condition in conditions_for_function])
                      for function, conditions_for_function in zip(switch.functions, switch.conditions)])

    prob.subs_all(switch.sym, switch_fun)

    return prob, None


def regularize_switches(prob: Problem):
    for _ in range(len(prob.switches)):
        regularize_switch(prob, switch_idx=0)

    return prob, None
