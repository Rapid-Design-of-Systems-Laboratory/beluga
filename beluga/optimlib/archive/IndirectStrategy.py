from NumOptControl import NumOptControl

class IndirectStrategy(object):
    def __init__(self, config, problem):
        # all config stuff goes in this variable
        # logging level, output ... etc.
        self.config = config
        self.problem = problem

    def execute(self):
        self.nec_cond = NumOptControl()

        # Call functions in other classes in the right order?

    pass

if __name__ == '__main__':
    s = IndirectStrategy(None, None)
    s.execute()
