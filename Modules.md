# Modules

```` 
import os
print("My working directory:",os.getcwd())
 ````
"os.getcwd" can be said as the alternative for pwd in command prompt. Which give the crruntly working directory.
#
```
 lst = os.listdir(r"C:\Users\Admin\OneDrive\Desktop\Upflairs\test_MODULES")
 print (lst)
```
"os.listdir" Is the altermative for ls in command prompt. This command gives the list of all the files in the directory.
#
There are three kind of paths:- relative paths , absolute path and python path
```
os.chdir("directory_name")                                   
print(os.listdir())
print("no. of items:",len(lst))
```
"os.chdir" is the alternative for "cd" in command prompt. We need to mention name of the directory inside the brackets.
#
```
os.makedirs("HELLOWORLD.py", exist_ok= True)  
```
"os.makedirs" is the alternate for mkdir in command prompt. "exist_ok= True" is used so that it does not throw an error if there if a directory with similar path already exist
#
``` 
os.rmdir("path") 
```     
"os.rmdir" is used so that and empty directory can be removed. If the directory is not empy then it will throw error.
#

```
os.removedirs("path")
```
"os.removedirs" is used as a method the recursively removes directories.    
#
```
path1 = "can give a file Name"
path2 = "2nd file name"
complete_path = os.path.join(path1,path2)
print("The file is present at:",complete_path)
os.chdir(complete_path)
```
"os.path.join" is used to join two paths.
#
```
if os.path.exist("hello.txt"):                      
    print("Your file exist")
else:
    text_file = open("hello.txt",'x')               
```
this is used to find wether te file already exist or not.
"x" is used in the so that if there is no such file as the given file, then the file is created.