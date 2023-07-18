"""
# Pytest Dryrun Plugin

A Pytest plugin to ignore tests during collection without reporting them in the
test summary.
"""
__version__ = "0.1.0"
__all__ = [
    'dryrun',
]
from typing import Callable, ParamSpec, TypeVar


P = ParamSpec('P')
T = TypeVar('T')


def dryrun(func: Callable[P, T]) -> Callable[P, T]:
    """
    Mark a test as being a dryrun test

    Alias to `pytest.mark.dryrun`
    """
    import pytest
    return pytest.mark.dryrun(func)


del P, T, Callable, ParamSpec, TypeVar
