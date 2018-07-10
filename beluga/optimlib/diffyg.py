from sympy.diffgeom import Manifold as sympyManifold
from sympy.diffgeom import Patch, CoordSystem, Differential, covariant_order, WedgeProduct
from sympy.printing import pprint
from sympy.simplify import simplify
import itertools
from beluga.utils import keyboard

class Manifold(object):
    def __new__(cls, *args, verbose=False):
        obj = super(Manifold, cls).__new__(cls)
        if len(args) >= 1:
            dependent = args[0]

        if len(args) >= 2:
            name = args[1]
        else:
            name = 'manifold'

        obj.name = name
        obj.dimension = len(dependent)
        obj._manifold = sympyManifold(obj.name, obj.dimension)
        obj._patch = Patch('Atlas', obj._manifold)
        obj._coordsystem = CoordSystem('Coordinates', obj._patch, names=dependent)
        return obj

    def __init__(self, *args, verbose=False):
        if verbose:
            print('The manifold `{}` has been created'.format(self.name))

        self.base_coords = self._coordsystem.coord_functions()
        if verbose:
            pprint('The following coordinates have been created: ' + str(self.base_coords))

        self.base_vectors = self._coordsystem.base_vectors()
        if verbose:
            pprint('The following base vectors have been created: ' + str(self.base_vectors))

        self.base_oneforms = self._coordsystem.base_oneforms()
        if verbose:
            pprint('The following base one forms have been created: ' + str(self.base_oneforms))

    def sharp(self, f):
        set1d = dict(zip(self.base_oneforms, self.base_vectors))
        return f.subs(set1d, simultaneous=True)

    def flat(self, f):
        set1D = dict(zip(self.base_vectors, self.base_oneforms))
        return f.subs(set1D, simultaneous=True)

    def exteriorderivative(self, f):
        order = covariant_order(f)

        # Automatically return 0 if f's grade is equal to manifold dimension
        if order == self.dimension:
            return 0

        if order == 0:
            return sum([Differential(f)(D_x)*dx for (D_x, dx) in zip(self.base_vectors, self.base_oneforms)])

        # If's f's grade is 1 or higher, we still need to implement this
        if order > 0:
            raise NotImplementedError


class FiberBundle(Manifold):
    def __new__(cls, *args, verbose=False):
        if len(args) < 2:
            raise ValueError('Fiber bundles must be constructed with two manifolds.')

        A = args[0]
        B = args[1]

        if len(args) == 3:
            name = args[2]
        else:
            name = A.name + B.name + '_fiberbundle'

        Ax = [str(x) for x in A.base_coords]
        Bx = [str(x) for x in B.base_coords]

        obj = super(FiberBundle, cls).__new__(cls, Ax + Bx, name, verbose=verbose)
        obj.vertical = A
        obj.horizontal = B

        return obj

    def __init__(self, *args, verbose=False):
        super(FiberBundle, self).__init__(*args, verbose=verbose)

        set1x = dict(zip(self.horizontal.base_coords, self.base_coords[self.vertical.dimension:]))
        set1d = dict(zip(self.horizontal.base_oneforms, self.base_oneforms[self.vertical.dimension:]))
        set1D = dict(zip(self.horizontal.base_vectors, self.base_vectors[self.vertical.dimension:]))
        set2x = dict(zip(self.vertical.base_coords, self.base_coords[:self.vertical.dimension]))
        set2d = dict(zip(self.vertical.base_oneforms, self.base_oneforms[:self.vertical.dimension]))
        set2D = dict(zip(self.vertical.base_vectors, self.base_vectors[:self.vertical.dimension]))

        self.horizontal.base_coords = [x.subs(set1x, simultaneous=True) for x in self.horizontal.base_coords]
        self.horizontal.base_oneforms = [d.subs(set1d, simultaneous=True) for d in self.horizontal.base_oneforms]
        self.horizontal.base_vectors = [D.subs(set1D, simultaneous=True) for D in self.horizontal.base_vectors]
        self.vertical.base_coords = [x.subs(set2x, simultaneous=True) for x in self.vertical.base_coords]
        self.vertical.base_oneforms = [d.subs(set2d, simultaneous=True) for d in self.vertical.base_oneforms]
        self.vertical.base_vectors = [D.subs(set2D, simultaneous=True) for D in self.vertical.base_vectors]

    def projection(self, input):
        return input[self.vertical.dimension:]

    def horizontalexteriorderivative(self, f):
        return self.horizontal.exteriorderivative(f)

    def verticalexteriorderivative(self, f):
        return self.vertical.exteriorderivative(f)


class JetBundle(FiberBundle):
    def __new__(cls, *args, verbose=False):
        if not isinstance(args[0], FiberBundle):
            raise ValueError('Jet bundles must be constructed from a fiber bundle.')

        if not isinstance(args[1], int):
            raise ValueError('Jet bundles must have a jet order.')

        if len(args) < 3:
            name = args[0].name + '_jetbundle'

        obj = args[0]
        obj.jetorder = args[1]

        hor_dim = obj.horizontal.dimension
        base_coords = [str(x) for x in obj.vertical.base_coords]
        coords = [str(x) for x in obj.vertical.base_coords]
        for ii in range(obj.jetorder):
            vals = [list(range(hor_dim)) for _ in range(ii+1)]
            for jord in itertools.product(*vals):
                for state in base_coords:
                    str_to_append = [str(_) for _ in jord]
                    coords.append(state + '_' + str('_'.join(str_to_append)))

        obj.vertical = Manifold(coords, obj.vertical.name + '_jet', verbose=verbose)
        obj.base_coords = obj.vertical.base_coords + obj.horizontal.base_coords
        obj.base_forms = obj.vertical.base_oneforms + obj.horizontal.base_oneforms
        obj.base_vectors = obj.vertical.base_vectors + obj.horizontal.base_vectors
        obj.dimension = obj.vertical.dimension + obj.horizontal.dimension

        return obj


class SymplecticManifold(Manifold):
    def __new__(cls, *args, verbose=False):
        obj = super(SymplecticManifold, cls).__new__(cls, *args, verbose=verbose)
        if obj.dimension % 2 == 1:
            raise ValueError
        obj.symplecticform = 0
        return obj

    def __init__(self, *args, verbose=False):
        super(SymplecticManifold, self).__init__(*args, verbose=verbose)
        d = int(self.dimension/2)
        self.symplecticform = sum([WedgeProduct(dx,dy) for (dx, dy) in zip(self.base_oneforms[:d], self.base_oneforms[d:])])
