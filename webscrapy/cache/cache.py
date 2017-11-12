__author__ = 'xXl'
import logging

def _init():
    global _global_dict
    _global_dict = {}

def set_value(key,value):
    _global_dict[key] = value

def get_value(key):
    try:
        return _global_dict[key]
    except KeyError:
        logging.debug(key+'不存在')
        return None