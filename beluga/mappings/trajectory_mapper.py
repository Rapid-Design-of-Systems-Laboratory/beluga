from typing import Iterable
from abc import ABC, abstractmethod
import copy

from beluga.utils.noneless_list import NonelessList
from beluga.data_classes.trajectory import Trajectory


class TrajectoryMapper(ABC):
    def __init__(self):
        pass

    def __repr__(self):
        return '{}<{}>'.format(self.__class__.__name__, id(self))

    @abstractmethod
    def map(self, traj: Trajectory) -> Trajectory:
        pass

    @abstractmethod
    def inv_map(self, traj: Trajectory) -> Trajectory:
        pass

    def map_many(self, trajs):
        # TODO Make parallel
        return map(self.map, trajs)

    def inv_map_many(self, trajs):
        # TODO Make parallel
        return map(self.inv_map, trajs)

    def __call__(self, trajs, inv=False):
        if isinstance(trajs, Iterable):
            if inv:
                return self.inv_map_many(trajs)
            else:
                return self.map_many(trajs)
        else:
            if inv:
                self.inv_map(trajs)
            else:
                return self.map(trajs)


class TrajectoryMapperList(TrajectoryMapper):
    # TODO Add multiprocessing
    def __init__(self):
        super(TrajectoryMapperList, self).__init__()
        self.mapper_list = NonelessList()
        self.maps = NonelessList()
        self.inv_maps = NonelessList()

    def __repr__(self):
        return 'MapperList{}'.format(self.mapper_list)

    def append(self, mapper: TrajectoryMapper):
        if isinstance(mapper, TrajectoryMapperList):
            if len(mapper.mapper_list) == 0:
                mapper = None

        if mapper is not None:
            self.mapper_list.append(mapper)
            self.maps.append(mapper.map)
            self.inv_maps.append(mapper.inv_map)

    def map(self, traj):
        for _map in self.maps:
            _map(traj)

        return traj

    def inv_map(self, traj):
        for _inv_map in reversed(self.inv_maps):
            _inv_map(traj)

        return traj
