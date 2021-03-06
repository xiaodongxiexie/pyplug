# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/8/7

import unittest

from pyplug.plug import Plug, plug, customization, staticcustomization, FuncAlreadyExistError

default = "my_first_hook"

Plug.__default__ = default

class KlassOne(plug):
    @customization(100, default=default)
    def do_something(self, info, value, loc=1):
        return info, value, loc

    @staticcustomization(90, default=default)
    def do_something_else(self, info, value, loc=2):
        return {
            "info": info,
            "value": value,
            "loc": loc
        }


class KlassTwo(plug):
    @customization(110, default=default)
    def do_something(self, info, value, loc=3):
        return [info, value, loc]

    @customization(default=default)
    def do_something_special(self, different_arg):
        return different_arg



class TestPlugWithNoOrder(unittest.TestCase):

    def test_func_length(self):
        self.assertEqual(len(Plug.__customization_storage__), 4)

    def test_property_type_is_dict(self):
        self.assertIsInstance(Plug.__customization_storage__, dict)

    def test_func_been_contained(self):
        self.assertIn("KlassOne.do_something", Plug.__customization_storage__)
        self.assertIn("KlassOne.do_something_else", Plug.__customization_storage__)
        self.assertIn("KlassTwo.do_something", Plug.__customization_storage__)
        self.assertIn("KlassTwo.do_something_special", Plug.__customization_storage__)

    def test_func_with_same_args(self):
        parameter = {"args": (1, 2), "kwargs": {"loc": 100}}
        func_with_same_arg = {
            "KlassOne.do_something",
            "KlassOne.do_something_else",
            "KlassTwo.do_something"
        }
        config = {
            "default": parameter,
            "do_something_special": {"args": ("i am special",), "kwargs": {}}
        }
        for func_name, func in Plug.__customization_storage__.items():
            if func_name in func_with_same_arg:
                cfg = config["default"]
            else:
                cfg = config["do_something_special"]
            print(func(*cfg["args"], **cfg["kwargs"]))


class TestPlugWithOrder(unittest.TestCase):

    def test_property_type_is_list(self):
        self.assertIsInstance(Plug.__ordered_customization_storage__, list)

    def test_func_length(self):
        self.assertEqual(len(Plug.__ordered_customization_storage__), 4)

    def test_func_been_with_ordered(self):
        self.assertEqual(Plug.__ordered_customization_storage__[0][1],
                         "KlassTwo.do_something")
        self.assertEqual(Plug.__ordered_customization_storage__[1][1],
                         "KlassOne.do_something")
        self.assertEqual(Plug.__ordered_customization_storage__[2][1],
                         "KlassOne.do_something_else")
        self.assertEqual(Plug.__ordered_customization_storage__[3][1],
                         "KlassTwo.do_something_special")


class TestExistKlassAndFunc(unittest.TestCase):

    def test_exist_klass_and_func(self):
        with self.assertRaises(FuncAlreadyExistError) as cm:
            from test_plug_else import KlassOne as AnotherKlassOne
        self.assertRegex(cm.exception.__str__(), ".*already existed")


if __name__ == '__main__':

    unittest.main()
