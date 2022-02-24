from functools import lru_cache
from timeit import repeat

@lru_cache(maxsize=16)
def steps_to(stair):
    pass


print(steps_to(30))

#to know the cash info
print(steps_to.cache_info())

"""Output:
53798080
CacheInfo(hits=52, misses=30, maxsize=16, currsize=16)"""