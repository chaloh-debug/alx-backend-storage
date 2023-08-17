#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


class Cache:
    """ Create a redis cache """
    def __init__(self):
        """ Initialize the cache """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """ Get data from redis """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data
    
    def get_str(self, key: str) -> str:
        """ Get a string from redis """
        return self.get(key, lambda x: x.decode("utf-8"))
    
    def get_int(self, key: str) -> int:
        """ Get an int from redis """
        return self.get(key, lambda x: int(x.decode("utf-8")))
