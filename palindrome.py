def is_palindrome():
  text = input("Enter the strng").strip().lower()
  
  if text == text[::-1]:
    print("The string is a palindrome")
  else:
    print("The string is not a palindrome")
    
is_palindrome()
