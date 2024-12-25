if __name__ == '__main__':
    stud_list=[]
    scorelist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scorelist.append(score)
        stud_list.append([name,score]) 
  
    seclow=sorted(set(scorelist))
    sorted_list= sorted(stud_list)  
    for name,score in sorted_list:
        if score == seclow[1]:
          print(name)
