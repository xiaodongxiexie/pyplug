# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/8/6

import sys
import types

from functools import wraps
from typing import Union
from bisect import insort_right


__all__ = ["Plug", "plug", "customization"]


class FuncAlreadyExistError(Exception):
    def __init__(self, func_name: str):
        self.func_name = func_name

    def __repr__(self) -> str:
        return f"{self.func_name} already existed"

    __str__ = __repr__


class Plug(type):
    """
    metaclass to trace which should been executed together.
    """
    def __new__(mcs, name, bases, d):
        if not hasattr(mcs, "__customization_storage__"):
            setattr(mcs, "__customization_storage__", {})
            setattr(mcs, "__ordered_customization_storage__", [])
        for k, v in d.items():
            if not hasattr(v, "__customization_name__"):
                continue
            if getattr(v, "__customization_name__") != "customization":
                continue

            storage_key = ".".join([name, k])

            if storage_key in mcs.__customization_storage__:
                raise FuncAlreadyExistError(storage_key)
            else:
                mcs.__customization_storage__[storage_key] = v
                insort_right(mcs.__ordered_customization_storage__, (-v._weight, storage_key, v))
        return super().__new__(mcs, name, bases, d)


class plug(metaclass=Plug):
    ...


class customization:
    """
    this can use as a decorator in a class.
    ...example
        class your-class(plug):
            @customization(<this-func-weight: [int, flot]>)
            def your-func(...):
                do_something(...)
                return something

    """

    def __init__(self, weight: Union[int, float] = 0):
        """
        :param weight: this can change your custom-made func call order
                       larger then have a priority
        """

        class _customization:
            def __init__(self, func: callable):
                wraps(func)(self)
                self.func = func
                self.__customization_name__ = "customization"

            def __call__(self, *args, **kwargs):
                return self.func(*args, **kwargs)

            def __get__(self, instance, cls):
                if instance is None:
                    return self
                return types.MethodType(self, instance)

        _customization._weight = weight
        self._customization = _customization

    def __call__(self, func: callable):
        return self._customization(func)

