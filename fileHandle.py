f = open("text.txt" , "a")
data = f.readline()  #data store 
f.write("\nnew text is append by \n using append mode")
print(data)
print(type(data))
f.close()

f =  open("sample.txt" , "x")
f.write("Create new file by \n using x mode in file hndling ")
f.close()

f = open("sample.txt" , "r")
data = f.readline()  #return all data of file in the form of string
print(data)
line = f.readline()
print(line)
print(type(data))
f.close() 


f = open("sample.txt" , "w")
f.write("Hello world")
f.close()


f = open("Sample.txt" , "a")
f.write("\nUsing python ")


f = open("sample.txt" , "w+")
data = f.read()
print(data)
f.write("Hello world")
f.close()

with open("text.txt" , "r") as f:
    data = f.read()
    print(data)

with open("text.txt" , "w") as f:
    f.write("New data")

import os

os.remove("text.txt")

with open("practice.txt" , "w") as f:
    f.write("Hi everyone\nWe are learning File I/o\nusing Java\nI like Programming in Java")


with open("practice.txt" , "r+") as f:
    data = f.read()

new_data = data.replace("Java" , "Python")
print(new_data)

with open("practice.txt" , "w") as f:
    f.write(new_data)

def check_for_word():
    with open("practice.txt" , "r+") as f:
        data = f.read()
        if(data.find("lrearning") != -1):
            print("Found")
        else:
            print("Not Found")

check_for_word()


i = 1
with open("names.txt" , "w") as f:
    while(i <=5):
        data = input("Enter name :")
        f.write(data)
        f.write("\n")
        i += 1

with open("names.txt", "r") as f:
    fdata = f.read()
    print(fdata)

list = [5,10,15,20,25]
new_list = [val for val in list if val > 15]
print(new_list)


