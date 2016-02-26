# -*- coding: utf-8 -*-
"""utils module to aop feature."""

import sys


def get_module_and_classname(classpath):
    """Splits classpath to modulepath and classname."""
    parts = classpath.split(".")
    classname = parts.pop()
    modulename = ".".join(parts)
    return modulename, classname


def get_class(classpath):
    """Returns an instance of a class."""
    modulename, classname = get_module_and_classname(classpath)  # Split the class path
    __import__(modulename)
    klass = getattr(sys.modules[modulename], classname)
    return klass
