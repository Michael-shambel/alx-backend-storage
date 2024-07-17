#!/usr/bin/env python3
"""
creating a cache class with the instance of radis and flushdb
creating store method thatakes data argumetn and return string
and generate a random key
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: callable) -> callable:
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        self._redis.incr(key)
        return method(*args, **kwds)
    return wrapper


class Cache:
    """
    cache class that intialize redis and flushdb
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: int) -> Union[int, None]:
        return self.get(key, fn=int)
