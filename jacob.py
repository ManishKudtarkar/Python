l1 = [[2,5,5,10,7],(15,2,7,9),(3,4,6,7),{2,5,8,7,9}]

for elem in l1:
    s=0
    c=0
    print(elem)
    for e in elem:
        s=s+e
        c=c+1

    print(s, s/c)
    print()
l2 = type(l1[0])
print(l2)
l3= count(l2)
