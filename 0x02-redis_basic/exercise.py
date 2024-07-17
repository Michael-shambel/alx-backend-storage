#!/usr/bin/env python3
"""
creating a cache class with the instance of radis and flushdb
creating store method thatakes data argumetn and return string
and generate a random key
"""
import redis
import uuid
from typing import Union


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
