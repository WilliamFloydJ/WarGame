import math

def emptyList(val):
    if val:
        return val
    else:
        return []

def tupleAdd(v1:tuple,v2:tuple):
    return tuple(x + y for x, y in zip(v1, v2))

def real_ceil(fl:float):
    if fl < 0:
        return math.floor(fl)
    elif fl > 0:
        return math.ceil(fl)
    else:
        return 0