str1 = "hi my name is maddy"
res = str1[1:2]+" "+str1[3:5]+" "+str1[11:13]+" "+str1[16:19]
print(res)

str2 = "this is big data batch"
lst = str2.split()
print(lst)


a = "milin"
print(a.replace("i","o"))

string2 = "life is good"
print("2".join(string2))

string3 = "my name is maddy"
res = " ".join(ele.capitalize()for ele in string3.split())
print(res)

print(string3.title())
boss= string3.find("m")
print(boss)

str3 = "people"
for index,char in enumerate(str3):
  print(index,char)
  
str5 ="my name is maddy"
print([i for i,char in enumerate(str5) if char =='m'])

#Wrapping
import textwrap
def wrap(string, max_width):
    s1 = textwrap.fill(string, max_width)
    return s1
