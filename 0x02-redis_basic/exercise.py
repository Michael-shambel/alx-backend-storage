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
    """
    cout decoretor that count the
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: callable) -> callable:
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


# def replay(method: callable):
#     """
#     display the history of call
#     """
#     redis_inst = method.__self__._redis
#     method_name = method.__qualname__
#     input_key = f"{method_name}:inputs"
#     output_key = f"{method_name}:outputs"
#     inputs = redis_inst.lrange(input_key, 0, -1)
#     outputs = redis_inst.lrange(output_key, 0, -1)
#     print(f"{method_name} was called {len(inputs)} times:")
#     for inp, outp in zip(inputs, outputs):
#         print(f"{method_name}(*{inp.decode('utf-8')})
#               -> {outp.decode('utf-8')}")


class Cache:
    """
    cache class that intialize redis and flushdb
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)
