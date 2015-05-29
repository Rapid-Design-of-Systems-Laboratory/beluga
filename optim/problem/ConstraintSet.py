from optim.problem import Constraint

class ConstraintSet(list):
    def get(self,constraint_type):
        return [x for x in self if x.type == constraint_type]

    def add_initial(self, expr, unit):
        self.add(Constraint('initial',expr,unit))
        return self

    def add_terminal(self, expr, unit):
        self.add(Constraint('terminal',expr,unit))
        return self
        
    def add(self,constraint=None):
        if constraint is None:
            constraint = Constraint()
        self.append(constraint)
        return constraint
