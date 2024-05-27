#                                            CONDITIONAL STATEMENT:-
```
age = int(input("Enter the age"))
if age>18 and age<21:
    print("You are able to vote")
elif age>21:
    print("You can stand in election")
else:
    print("You are not capable to vote or stand in election")        
```

#                                                     LOOPS:-

Ther are two kinds of loops in python.
for loop, while loop
```
for i in range(0,10,2):
    print(i)
```
```
count = 0
for i in range(1,11):
    count += 1
    continue
print(count)
```
```
str = 'upflairs'
for char in str:
    print(char, end=" ")
```    
```
 d = {'A':0,'B':2,'C':3,'D':4}
  for i in d.values():         
      print(i)
 for keys,values in d.items():
     print(keys,"=>",values)
```
.items(), defualt is key.
```
lst = [52,342,34,31,32,43,47,56,45,94,98,54]
for i,item in enumerate(lst):
    print(i,"=>",item)
```
```
while True:
    password = eval(input("Enter the password"))
    if password == 1234:
        print("UNLOCKED")   
```
```
new_lst = []
avg = 0
lst = [12,23,34,45,65,76,87,98,90,67]
for i in lst:
    if i%2 == 0:
       new_lst.append(i)
       avg += i
print(new_lst)       
print(avg/len(lst))       
```

#                                                   FUNCTIONS
```
 def add(i,j):
     return i+j                                            
```     
return keyword stops the working of a function. No further lines in the functions will be used. The variables wil be released.          
```
 print(add(6,9))                 


 def greet():
     print("GOOD EVENING")

 greet()   
```
