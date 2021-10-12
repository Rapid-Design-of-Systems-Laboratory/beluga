import time

import pytest

from .timers import Timer, PerfTimer, ProcessTimer, TimerNS, PerfTimerNS, ProcessTimerNS

abs_tol = 5e-2  # absolute tolerance of timers in seconds (has to account for wrapping context manager)
rel_tol = 1e-1  # relative tolerance of timers in seconds (has to account for wrapping context manager)


def func_to_time() -> int:
    return sum([i for i in range(1_000_000)])


@pytest.mark.parametrize('timer_class', [Timer, PerfTimer, ProcessTimer])
def test_timers(timer_class):
    """
    Function to test the timers that record time as a float.
    :param timer_class: the timer class to test
    :return:
    """
    timer = timer_class()

    with timer:
        output = func_to_time()

    check_t0 = time.perf_counter()
    expected_output = func_to_time()
    check_tf = time.perf_counter()
    delta_t = check_tf - check_t0

    assert output == expected_output                # checks if context manager modifies contents
    assert isinstance(timer.total_time, float)      # checks if timer measures in float like expected
    assert timer.total_time == pytest.approx(delta_t, abs=abs_tol, rel=rel_tol)  # checks if timer is accurate


@pytest.mark.parametrize('timer_class', [TimerNS, PerfTimerNS, ProcessTimerNS])
def test_ns_timers(timer_class):
    """
    Function to test the timers that record time as a interger number of nanoseconds.
    :param timer_class: the timer class to test
    :return:
    """
    timer = timer_class()

    with timer:
        output = func_to_time()

    check_t0 = time.perf_counter_ns()
    expected_output = func_to_time()
    check_tf = time.perf_counter_ns()
    delta_t = check_tf - check_t0

    assert output == expected_output              # checks if context manager modifies contents
    assert isinstance(timer.total_time, int)      # checks if timer measures in float like expected
    assert timer.total_time == pytest.approx(delta_t, abs=abs_tol * 1e9, rel=rel_tol)  # checks if timer is accurate

