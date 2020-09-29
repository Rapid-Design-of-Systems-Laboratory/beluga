import cloudpickle as pickle


def save(sol_set, filename='data.beluga'):

    save_dict = {}

    if sol_set is not None:
        save_dict['solutions'] = sol_set

    with open(filename, 'wb') as file:
        pickle.dump(save_dict, file)


def load(filename):
    with open(filename, 'rb') as file:
        save_dict = pickle.load(file)

    return save_dict


