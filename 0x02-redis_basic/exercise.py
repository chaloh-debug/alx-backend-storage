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
