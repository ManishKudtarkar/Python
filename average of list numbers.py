def calculate_average():
  numbers = list(map(float,input("Enter numbers seperated by space").split()))
  average = sum(numbers)/len(numbers)
  print(f"Average:{average:.2f}")
calculate_average()
