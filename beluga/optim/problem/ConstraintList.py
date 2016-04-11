from beluga.optim.problem import Constraint

class ConstraintList(list):
    def get(self,constraint_type):
        return [x for x in self if x.type == constraint_type]

    def initial(self, expr, unit):
        self.add(Constraint('initial',expr,unit))
        return self

    def terminal(self, expr, unit):
        self.add(Constraint('terminal',expr,unit))
        return self

    def independent(self, expr, unit):
        """
        Add a constraint on the independent variable
        """
        self.add(Constraint('independent',expr,unit))
        return self

    def interior_point(self, expr, unit):
        self.add(Constraint('interior_point',expr,unit))
        return self

    def equality(self, expr, unit):
        self.add(Constraint('equality',expr,unit))
        return self

    def path(self, expr, direction, limit, unit):
        self.add(Constraint('path', expr, unit, direction, limit))
        return self

    def control(self, expr, lbound, ubound, unit):
        # TODO: Maybe make a better, unified way of defining constraints?
        c = Constraint('control', expr, unit)
        c.ubound = ubound
        c.lbound = lbound
        self.add(c)


    def add(self,constraint=None):
        if constraint is None:
            constraint = Constraint()
        self.append(constraint)
        return constraint
