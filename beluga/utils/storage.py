import json
from ..data_classes.trajectory import Trajectory


def save(sol_set, filename='data.json'):

    filetype = filename.split('.')[-1]

    if filetype == 'json':
        parsed_data = [[sol.form_data_dict(use_arrays=False) for sol in cont] for cont in sol_set]

        with open(filename, 'w') as file:
            json.dump(parsed_data, file)

    elif filetype == 'npz':
        import numpy as np

        parsed_data = np.array(
                [np.array([sol.form_data_dict() for sol in cont], dtype=object) for cont in sol_set], dtype=object)
        np.savez(filename, parsed_data)

    elif filetype == 'mat':
        raise NotImplementedError
        # from scipy.io import savemat
        #
        # parsed_data = dict()
        # for idx, cont in enumerate(sol_set):
        #     parsed_data[idx] = [sol.form_data_dict() for sol in cont]
        #
        # savemat(filename + '.mat', parsed_data)

    else:
        raise NotImplementedError('File type {} not supported'.format(filetype))


def load(filename):

    filetype = filename.split('.')[-1]

    if filetype == 'json':
        with open(filename, 'r') as file:
            raw_data = json.load(file)

    elif filetype == 'npz':
        import numpy as np
        raw_data = np.load(filename, allow_pickle=True)['arr_0.npy']

    elif filetype == 'mat':
        from scipy.io import loadmat
        raw_data = loadmat(filename)

    else:
        raise NotImplementedError('File type {} not supported'.format(filetype))

    sol_set = [[Trajectory(**sol_data) for sol_data in cont] for cont in raw_data]

    return sol_set
