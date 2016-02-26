# -*- coding: utf-8 -*-

from dino.aop import utils


class TestUtils(object):
    def test_get_module_and_classname(self):
        modulename, classname = utils.get_module_and_classname('aop.test_utils.TestUtils')
        assert modulename == self.__module__
        assert classname == self.__class__.__name__

    def test_get_class(self):
        klass = utils.get_class('aop.test_utils.TestUtils')
        assert 'aop.test_utils' == klass.__module__
        assert 'TestUtils' == klass.__name__
