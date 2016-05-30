# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


def require_value_from_dict(dict, key):
    try:
        if isinstance(dict[key], str):
            return dict[key].strip()
        elif isinstance(dict[key], unicode):
            return dict[key].strip()
        else:
            return dict[key]
    except:
        return None
