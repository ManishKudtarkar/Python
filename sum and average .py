l1 = [[2,5,5,10,7],(15,2,7,9),{2,5,8,7,9}]
list_sum = sum(l1[0])
list_avg = sum(l1[0]) / len(l1[0])

tuple_sum = sum(l1[1])
tuple_avg = tuple_sum / len(l1[1])

set_sum = sum(l1[2])
set_avg = set_sum / len(l1[2])


print(l1[0])
print(l1[1])
print(l1[2])
print("sum =",list_sum)
print("avg =",list_avg)
print("sum tup =",tuple_sum)
print("avg tup=",tuple_avg)
print("sum set =",set_sum)
print("avg set=",set_avg)
