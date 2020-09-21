from typing import Iterable

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


def tuplefy(iter_var):

    if isinstance(iter_var, Iterable):
        iter_var = tuple([tuplefy(item) for item in iter_var])

    return iter_var
