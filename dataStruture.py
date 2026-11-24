word = "I love "
word1 = "python"
sentence = word + " "  + word1
print(sentence)
print(word[4])
for ch in word1:
    print(ch)

print(word1[-4:-2])
print(word1[5:7])

word = "I study python from apna college"
print(len(word))
print(word[13:len(word)])

a = 5;
b = 6;
sum = a + b 
print("sum of {1} + {0} = {2}" .format(a,b,sum))

a = 5
b= 56
sum = a + b
print("sum {a} & {b} ".format(a= 5, b= 5))
print(f"avg of {a} & {b} = {(a+b)/2}")


# lists  --> mutable
marks = [88,87,86,85,84 , 9.2 ,9.4]
print(len(marks))
marks[4] = 89
print(marks[0])
print(marks)
print(type(marks))
print(marks[5:])
print(marks[-5:-2])
marks.append(9)
marks.insert(2,9.2)
marks.sort()
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
idx = 0
for val in marks :
    if(val == 85):
        print(f"{85} is found at idx {idx}")
        break
    idx+=1

# tuples  --> immutable
tup = (1,2,3,4,5,6,7,8.7)
print(type(tup))
print(len(tup))
print(tup[4])
print(tup[:])
tup1 = (1,)
print(type(tup1))
sum = 0
for val in tup:
    sum+=val
print(sum)
val = tup.index(7)
count = tup.count(6)
print(val)
print(count)

#dictionary 
dict = {
    "name" : "Avinish"
}