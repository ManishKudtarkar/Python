numbers= list(map(float,input("Enter numbers:\n").split()))
order = input ("sort (a)scendingor (d)escending?\n").lower()
print(sorted(numbers)if order =="a" else sorted(numbers,reverse=True))
