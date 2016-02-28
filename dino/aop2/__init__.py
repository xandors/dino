# -*- coding: utf-8 -*-

"""
Aspect Oriented Programming Library for Python.
Provides tools to (un)weave and get advices, and check joinpoint status.
"""

from .advice import weave, unweave, get_advices, weave_on
from .joinpoint import Joinpoint, JoinpointError, is_intercepted, get_intercepted

__all__ = [
    'weave',
    'weave_on',
    'get_advices',
    'unweave',
    'Joinpoint',
    'JoinpointError',
    'is_intercepted',
    'get_intercepted'
]
