import numpy as np


class BaseSol:
    def __init__(self, t, y, u, p, k):
        self.t = t
        self.y = y
        self.u = u
        self.p = p
        self.k = k


class SolSet:
    def __init__(self, prob):

        self.prob = prob
        self.solutions = []
        self.mappings = []
