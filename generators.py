from terms import var, app, abs
from itertools import product

def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def rotate(l, n):
    n = n % len(l)
    return l[n:] + l[:n]

def plus(*iterables):
    iters = tuple(map(iter, iterables))
    indices = tuple(range(len(iterables)))
    while len(indices) > 0:
        index = indices[0]
        try:
            yield iters[index].__next__()
            indices = rotate(indices, 1)
        except StopIteration:
            indices = indices[1:]

def times(*iterables):
    iters = tuple(map(iter, iterables))
    seen = [[] for iterable in iterables]
    indices = tuple(range(len(iterables)))
    while len(indices) > 0:
        index = indices[0]
        try:
            element = iters[index].__next__()
            yield from product(*seen[:index], [element], *seen[index+1:])
            seen[index].append(element)
            indices = rotate(indices, 1)
        except StopIteration:
            indices = indices[1:]

def variables(depth):
    return map(var, range(depth))

def terms(depth=0):
    yield from plus(
        variables(depth),
        map(abs, terms(depth + 1)),
        map(app, terms(depth), terms(depth))
    )