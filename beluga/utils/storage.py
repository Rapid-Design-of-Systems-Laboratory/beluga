import cloudpickle as pickle


def save(sol_set=None, ocp=None, bvp=None, filename='data.beluga'):

    save_dict = {}

    if sol_set is not None:
        save_dict['solutions'] = sol_set

    if ocp is not None:
        save_dict['prob'] = ocp

    if bvp is not None:
        save_dict['bvp'] = bvp

    with open(filename, 'wb') as file:
        pickle.dump(save_dict, file)


def load(filename):
    with open(filename, 'rb') as file:
        save_dict = pickle.load(file)

    return save_dict


