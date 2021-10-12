import time
from typing import Union, Callable


class Timer:
    """
    Timer context manager to time blocks of code and output to screen for debugging.

    This base timer uses time.monotonic and timer function.

    Example:
        with Timer():
            print(sum([i for i in range(1_000_000)]))

    """
    timer_func = time.monotonic

    start_time = None
    end_time = None
    total_time = None

    def __init__(self, logging_func: Union[Callable, None] = None, log_prefix: str = 'Run Time: '):
        """
        :param logging_func: function to call to display elapsed time (ex. print, logging.info, logger.debug)
        :param log_prefix: string to prefix log message
        """
        self.logging_func = logging_func
        self.log_prefix = log_prefix

    def __enter__(self):
        """
        Sets start_time when entering context manger
        :return:
        """
        self.start_time = self.timer_func()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Computes total_time and runs output

        :param exc_type: exception type (not used but needed for context managers)
        :param exc_val: exception value (not used but needed for context managers)
        :param exc_tb: exception traceback (not used but needed for context managers)
        :return:
        """
        self.end_time = self.timer_func()
        self.total_time = self.end_time - self.start_time
        self.log()

        return False

    def form_log_string(self):
        """
        Method to format string to display elapsed time in seconds
        :return:
        """
        return '{:.6g} seconds'.format(self.total_time)

    def log(self):
        """
        Log or print elapsed time
        :return:
        """
        if self.logging_func is not None:
            log_string = self.log_prefix + self.form_log_string()
            self.logging_func(log_string)


class PerfTimer(Timer):
    """
    Timer subclass which use time.perf_counter as timer function
    Suggested to use for measuring short code blocks
    """
    timer_func = time.perf_counter


class ProcessTimer(Timer):
    """
    Timer subclass which use time.process_time as timer function
    Suggested to use for profiling
    """
    timer_func = time.process_time


class TimerNS(Timer):
    """
    Timer that uses nanosecond timer function time.monotonic_ns to measure time with int instead of float
    Avoid truncation errors for short times
    """
    timer_func = time.monotonic_ns

    def form_log_string(self):
        """
        Method to format string to display elapsed time in seconds and nanoseconds
        :return:
        """
        return '{:.6g} seconds ({} ns)'.format(self.total_time * 1e-9, self.total_time)


class PerfTimerNS(TimerNS):
    """
    Nanosecond timer subclass which use time.perf_counter_ns as timer function
    Suggested to use for measuring short code blocks
    """
    timer_func = time.perf_counter_ns


class ProcessTimerNS(TimerNS):
    """
    Nanosecond timer subclass which use time.perf_counter_ns as timer function
    Suggested to use for measuring short code blocks
    """
    timer_func = time.process_time_ns
