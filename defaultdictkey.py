from collections import defaultdict

a, b = map(int, input().split())
dict = defaultdict(list)

# Read list A
for _ in range(a):
    dict['A'].append(input())

# Read list B
for _ in range(b):
    dict['B'].append(input())

# For each word in B, find and print positions in A
for word in dict['B']:
    target_index = [str(i + 1) for i, val in enumerate(dict['A']) if val == word]
    if target_index:
        print(' '.join(target_index))
    else:
        print(-1)
