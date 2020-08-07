# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/8/6

from pyplug.plug import Plug, plug, customization


default = "my_first_hook"

Plug.__default__ = default


class Mock(object):

    def __init__(self, *args, **kwargs):
        ...

    def __call__(self, *args, **kwargs):
        return True


class FetchData(plug):
    @customization(0, default=default)
    def test(self, url="http://example.com/data"):
        data = Mock(url)()
        return data


class FetchData2(plug):
    @customization(10, default=default)
    def test(self, times: int, url="http://example2.com/data"):
        """
        this is some description
        """
        data = []
        for i in range(times):
            data.append(Mock(url)())
        return data

    def this_will_never_been_executed(self):
        return "will not been executed"


if __name__ == '__main__':

    config = {
        "FetchData.test": {"args": (), "kwargs": {"url": "http://fake.com"}},
        "FetchData2.test": {"args": (100,), "kwargs": {"url": "http://fake.com"}}
    }

    for _, func_name, func in Plug.__ordered_customization_storage__:
        print(func(*config[func_name]["args"], **config[func_name]["kwargs"]))

    for func_name, func in (Plug.__customization_storage__).items():
        print(func(*config[func_name]["args"], **config[func_name]["kwargs"]))
