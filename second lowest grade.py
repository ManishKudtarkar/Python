if __name__ == '__main__':
    arr = {}  
    lowest = float('inf')  
    second = float('inf')  

    for _ in range(int(input("Enter the number of students: "))):
        name = input("Enter the student's name: ")
        score = float(input("Enter the student's score: "))
        arr[score] = arr.get(score, []) + [name]

        
        if score < lowest:
            second = lowest
            lowest = score
        elif lowest < score < second:
            second = score

    if second in arr:
        print('\n'.join(sorted(arr[second])))
    else:
        print("No second-lowest score found.")
