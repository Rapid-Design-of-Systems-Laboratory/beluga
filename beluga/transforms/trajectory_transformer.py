from abc import ABC, abstractmethod
from typing import Iterable

from beluga.data_classes.trajectory import Trajectory
from beluga.utils.noneless_list import NonelessList


class TrajectoryTransformer(ABC):
    def __init__(self):
        pass

    def __repr__(self):
        return '{}<{}>'.format(self.__class__.__name__, id(self))

    @abstractmethod
    def transform(self, traj: Trajectory) -> Trajectory:
        pass

    @abstractmethod
    def inv_transform(self, traj: Trajectory) -> Trajectory:
        pass

    def transform_many(self, trajs):
        # TODO Make parallel
        return [self.transform(traj) for traj in trajs]

    def inv_transform_many(self, trajs):
        # TODO Make parallel
        return [self.inv_transform(traj) for traj in trajs]

    def __call__(self, trajs, inv=False):
        if isinstance(trajs, Iterable):
            if inv:
                return self.inv_transform_many(trajs)
            else:
                return self.transform_many(trajs)
        else:
            if inv:
                self.inv_transform(trajs)
            else:
                return self.transform(trajs)


class TrajectoryTransformerList(TrajectoryTransformer):
    # TODO Add multiprocessing
    def __init__(self):
        super(TrajectoryTransformerList, self).__init__()
        self.transforms = NonelessList()
        self.transform_funcs = NonelessList()
        self.inv_transform_funcs = NonelessList()

    def __repr__(self):
        return 'TransformerList{}'.format(self.transforms)

    def append(self, transform: TrajectoryTransformer):
        if isinstance(transform, TrajectoryTransformerList):
            if len(transform.transforms) == 0:
                transform = None

        if transform is not None:
            self.transforms.append(transform)
            self.transform_funcs.append(transform.transform)
            self.inv_transform_funcs.append(transform.inv_transform)

    def transform(self, traj):
        for _map in self.transform_funcs:
            _map(traj)

        return traj

    def inv_transform(self, traj):
        for _inv_map in reversed(self.inv_transform_funcs):
            _inv_map(traj)

        return traj
