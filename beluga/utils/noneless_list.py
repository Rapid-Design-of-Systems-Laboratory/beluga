from typing import Iterable


class NonelessList(list):
    def __init__(self, *args):
        if len(args) == 0:
            super(NonelessList, self).__init__()
        elif len(args) == 1:
            _iterable = self._process_input(args[0])
            super(NonelessList, self).__init__(_iterable)
        else:
            raise TypeError('NonelessList expected at most 1 argument, got {}'.format(len(args)))

    def __repr__(self):
        return super(NonelessList, self).__repr__()

    def __setitem__(self, key, value):
        if value is None:
            super(NonelessList, self).__delitem__(key)
        else:
            super(NonelessList, self).__setitem__(key, value)
            self._remove_nones()

    def __add__(self, other):
        return NonelessList(super(NonelessList, self).__add__(other))

    def __mul__(self, other):
        return NonelessList(super(NonelessList, self).__mul__(other))

    @staticmethod
    def _process_input(iterable):
        if not isinstance(iterable, Iterable):
            raise TypeError('\'{}\' object is not iterable'.format(type(iterable).__name__))
        else:
            return [item for item in iterable if item is not None]

    def append(self, _object) -> None:
        if _object is not None:
            super(NonelessList, self).append(_object)

    def extend(self, _iterable) -> None:
        _iterable = self._process_input(_iterable)
        super(NonelessList, self).extend(_iterable)

    def insert(self, _index: int, _object) -> None:
        if _object is not None:
            super(NonelessList, self).insert(_index, _object)

    def _remove_nones(self):
        while self.count(None) > 0:
            self.remove(None)
