from collections import OrderedDict

cache = OrderedDict()
ops = ['A', 'B', 'C', 'A', 'D']
capacity = 3

for key in ops:
    if key in cache:
        cache.move_to_end(key)
    else:
        if len(cache) == capacity:
            cache.popitem(last=False)
        cache[key] = True

print(list(cache.keys()))