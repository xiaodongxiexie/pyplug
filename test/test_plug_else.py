# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/8/7

from pyplug.plug import Plug, plug, customization


default = "my_first_hook"

Plug.__default__ = default


class KlassOne(plug):
    @customization(100, default=default)
    def do_something(self, info, value, loc=1):
        return info, value, loc
