import sys


s,t = list(map(int, input().strip().split(' ')))
a, b = list(map(int, input().strip().split(' ')))
n, m = list(map(int, input().strip().split(' ')))
apple = [int(apple_t) for apple_t in input().strip().split(' ')]
orange = [int(orange_t) for orange_t in input().strip().split(' ')]
count =[0, 0]
for i in apple:
    if(i + a >= s and i + a <= t):
        count[0] +=1

for j in orange:
    if(j + b >= s and j + b <= t):
        count[1] +=1   

print(count[0])

print(count[1])
