# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
import codecs


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


def get_gb2312_txt():
    f = codecs.open('data/gb2312.txt', 'r', 'utf-8')
    return f.read()
