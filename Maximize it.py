from itertools import product
from functools import partial

k, m = map(int, input().split())

def s(lst: tuple, mod: int) -> int:
    return sum(map(lambda x: x**2, lst)) % mod
    
s_fixed = partial(s, mod=m)
lsts = []

for _ in range(k):
    n, *arr = map(int, input().split())
    lsts.append(arr)

print(max(map(s_fixed, product(*lsts))))
