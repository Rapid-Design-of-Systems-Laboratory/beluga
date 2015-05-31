class DynamicSystemList(list):
    """Describes a list of dynamic systems"""
    def constraints(self,select=0):
        """Sets constraints for given system in the list"""
        return self

    def state(self,var,eqn,unit):
        """Adds a state to all systems in the list"""
        [s.state(var,eqn,unit) for s in self]
        return self

    def constant(self,var,val,unit):
        """Adds a state to all systems in the list"""
        [s.constant(var,val,unit) for s in self]
        return self

    def control(self,var,unit):
        """Adds a control variable to all systems in the list"""
        [s.control(var,unit) for s in self]
        return self

    def independent(self,name,unit,select=None):
        """Sets independent variable for all/some systems in the list"""
        if select is None:
            [s.independent(var,unit) for s in self]
        else:
            [self[i].independent(var,unit) for i in select]
        return self
