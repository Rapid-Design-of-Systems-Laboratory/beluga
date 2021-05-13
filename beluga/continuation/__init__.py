"""
Module: continuation
"""

from .continuation import ContinuationList, ContinuationVariable, ManualStrategy,\
    ProductStrategy, BisectionStrategy, run_continuation_set

from .guess_generators import guess_generator, GuessGenerator, match_constants_to_states
