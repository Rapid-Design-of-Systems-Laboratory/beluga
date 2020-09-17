import cloudpickle as pickle


def save(ocp=None, bvp=None, bvp_solver=None, sol_set=None, filename='data.beluga'):
    assert any([ocp is not None, bvp_solver is not None, sol_set is not None]), 'No data given to save.'

    save_dict = {}
    # if ocp is not None:
    #     # assert ocp.__class__ is beluga.Problem, 'prob should be of beluga.problem.OCP class'
    #     save_dict['prob'] = ocp
    #
    # if bvp is not None:
    #     save_dict['prob'] = bvp
    #
    # if bvp_solver is not None:
    #     # assert issubclass(bvp_solver.__class__, beluga.bvp_solvers.BaseAlgorithm), 'bvp_solver should be subclass ' \
    #     #                                                                       'of beluga.bvp_solvers.BaseAlgorithm'
    #     save_dict['prob solver'] = bvp_solver

    if sol_set is not None:
        # assert all([sol.__class__ is beluga.ivp_solvers.ivp_solvers.Trajectory for cont_set in sol_set for sol in cont_set]),\
        #     'all solutions in sol_set should be of class beluga.ivp_solvers.ivp_solvers.Trajectory'
        save_dict['solutions'] = sol_set

    with open(filename, 'wb') as file:
        pickle.dump(save_dict, file)

    # with open(filename, 'wb') as file:
    #     pickle.dump(sol_set, file)


def load(filename):
    with open(filename, 'rb') as file:
        save_dict = pickle.load(file)

    return save_dict

