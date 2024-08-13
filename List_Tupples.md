# LIST

 insertion,
 deletion,
 append,
 creation,
 remove,
 clear,


**Difference between extend and append**
```
 lst1 = [1,2,3,4]    
 lst2 = [5,6,7,8]
 
 lst1.append(lst2)
 print(lst1)

 lst1.extend(lst2)
 print(lst1)
```
# 2d Array
```
 lst = [[1,2,3,4],
        [4,5,6,7],
        [8,2,9,4]]
 print(lst[1][2:])
```

# Tupples
```
 tpl = (3)
 print(tpl)
 print(type(tpl))
```
```
 tpl = (3,)
 print(tpl)
 print(type(tpl))
```

 **Tupple unpacking**
```
 tpl = ('Rohan','CSE',211479)
 name, branch, enroll_number = tpl
 print(tpl,'\n')
 print('My name is :',name,'\n')
 print('My branch is :',branch,'\n')
 print('My enroll number is :',enroll_number,'\n')
```

 Replication
```
 tpl = (1,2,3)
 print(tpl*2)
```
 _count, index_

#  Sets
```
 st = {10,20,30,30,30,30,30,40,'upflairs',True,75,2}
 print(st)
 ```
 remove,
 add,
 discard,



# input
```
 name = eval(input("Enter your name:"))
 print("Welcome,",name)
```
 EVAL CAN MAKE THE INPUT DYNAMIC AND NOT RESTRIC TO ENTER ONLY INT AUR FLOAT(WE NEED TO USE INVERTED COMAS FOR STRING).