#!/usr/bin/env python3
'''module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''module-level Redis instance.
'''


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        ''' wrapper function for caching the output.
        '''
        redis_store.incr(f'count:{url}')
        reslt = redis_store.get(f'reslt:{url}')
        if reslt:
            return reslt.decode('utf-8')
        reslt = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'reslt:{url}', 10, reslt)
        return reslt
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Return content of a URL after caching the request's response,
    and trackin request.
    '''
    return requests.get(url).text
