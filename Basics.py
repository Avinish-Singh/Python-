a = float(input("Enter number = "))
b = float(input("Enter number = "))

avg = (a + b) / 2
print("Average of two number = " , avg)

user_name = input("Enter name = ")
age = int(input("Enter age = "))
print("Hello" , user_name , "you are" , age , "yeras old ")

a = int(input("Enter integer value = "))
b = float(input("Enter decimal value = "))
x = float(a)
y = float(b)
print("a = ", x ,"b = " , y)

n = int(input("Enter number : "))
sum = 0;
for val in range(1,n+1,1):
    sum += val

print("Sum of" , n , "Numbers =" , sum)

a = int(input("Enter number : "))
b = int(input("Enter number : "))
print("sum =",a+b)
print("diff =" ,a-b)
print("multiply =" ,a*b)
print("divide =" ,a/b)
print("reminder =" ,a%b)
print("power =" ,a**b)

a = input("Enter something :")
x = int(a) 
print(type(x))
y = float(a) 
print(type(y))
z = str(a)
print(type(z))

x = 10 + 3 * 2 ** 2;
print(x)

x = int(input("Enter number :"))
y = int(input("Enter number :"))
z = x
x = y
y = z
print(x)
print(y)

temp_celci = input("Enter temperature in Celcius :")
y = float(temp_celci)
tem_frahen = (y* (9/5))+32
print(tem_frahen)

radius = int(input("Enter radius of circle : "))
area = 3.14 * radius * radius
print(area)

prin = int(input("Enter principle amount : "))
rate = int(input("Enter rate : "))
time = int(input("Enter time :"))
si = (prin * rate * time) / 100
print(si)


#Calculate average of three number
def avg_3(a,b = 1,c = 1):
    sum = a + b + c
    return (sum/3)
a = int(input("Enter number :"))
b = int(input("Enter number :"))
c = int(input("Enter number :"))
ans = avg_3(a)
print(ans)

#Calculate factorial
def factorial(n):
    fact = 1
    for val in range(1 , n+1):
        fact *= val
    return fact
ans = factorial(5)
print(ans)

n = int(input("Enter number"))