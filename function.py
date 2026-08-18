'''def addition(x,y):
    sum=x+y
    return sum
add=addition(10,20)
print(add)
#print(addition(10,20))'''

'''def square(num):
    print(num*num)
    
print(square(2*2))'''

#program to display greeting using function


#program to diplay square of number using function


'''Write a function is_even(num) that returns True if the number is even,
otherwise False.'''
'''def is_even(num):
    if num%2==0:
        print(f"{num} is a even")
    else:
        return False
print(is_even(10))
print(is_even(13))'''

#default argument 
'''def greet(name="Sonam"):
    print("Hello I am",name)
greet("Wangmo")'''


# function argument arbiterie keyword argument 
'''def name(*name1):
    print(name1)

name("Karma","Sonam","Pema")'''

#Keyword argument 

'''def student(**info):
    for k, v in info.items():
        print(k, ":", v)

student(name="Sonam", age=15, school="SJMSS",Class=10)'''

# accessing the value
'''def bio(**info):
    #for k,v in info.items():
        print("Name:",info["name"])
        print("Class:",info["Class"])
        print("Sec:",info["sec"])

bio(name="Tashi",Class=10,sec="B")'''

#Types of user define function 

#non parameteraize func
'''def mul():
    a=5
    b=2
    multi=a*b
    print(multi)
mul()'''

#parametarized 
'''def mul(a,b):
    multi=a*b
    print(multi)
mul(3,5)'''

#function with argument and return 
'''def add(x,y):
    sum = x+y
    #return sum
    print(sum)
addition=add(5,4)
print(addition*2/2)'''

'''def fun1():
    global name
    name="Tashi"
fun1()

def fun2():
    age=17
    print(f"My name is {name} and i am {age} old")
fun2()'''


#accessing local variable from different function
'''def fun1():
    global name
    name="Sonam"
fun1()

def fun2():
    age=13
    print(f"my name is {name} and i am {age}")
fun2()'''

'''school="SJMSS"
def sh():
    global school
    school="SJHSS"
    print(school)
sh()
#print(school)'''

#side=float(input("Enter side:"))
'''def multiply(x,y):
    product=x*y
    return product
print(multiply(2,5))
print(multiply(5,5))
print(multiply(10,5))'''

'''def distance(speed,time):
    dist=speed*time
    return dist
    
s=int(input("Enter speed:"))
t=int(input("Enter time:"))
dis=distance(s,t)
print(f"The total distance cover is {dis} km/hrs")'''

def multiply(x,y):
    return x*y
print(multiply(4,5))
print(multiply(5,5))


'''def distance(speed,time):
    dist=speed*time
    #return dist
    print(f"total dis cover is { dist}")
sp=int(input("Enter speed:"))
ti=int(input("Enter time:"))
distance(sp,ti)
#print(f"The total distance covered is {dis} km/hrs")'''

#to check enter str is greater than 17 or not 
'''st=input("Enter any string to check")
def decision(text):
    if len(text)>17:
        print("This is a long string")
    else:
        print("This is a short string")
decision(st)'''  

#recursive function to find total of even number
'''def sum_even(n):
    if n == 0:
        return 0       
    elif n % 2 == 0:
        return n + sum_even(n - 2)        
    else:
        return sum_even(n - 1)
n = int(input("Enter a range of number: "))
print(f"The sum of even numbers up to {n} is {sum_even(n)}")'''

#function in turtle
'''import turtle
t=turtle.Turtle()
def square(size):
    for i in range(4):
        t.fd(size)
        t.rt(90)
        t.fd(80)
square(300)
turtle.done()'''

#to find the sum of nth natural number recursive function
'''def sum_of_natural(num):
    if num ==0:
        return 0
    else:
        return num + sum_of_natural(num-1)
n=int(input("Enter any number:"))
print(sum_of_natural(n))'''


#Fabonacci series
'''num=int(input("Enter nay number:"))
def fabonacci(n):
    if n==0: 
        return 0
    elif n==1:
        return 1
    else:
        return fabonacci(n-1) +fabonacci(n-2)
for i in range(num):
    print(fabonacci(i), end=" ")'''
    
school=["SJMSS","SJPS","DPS"]
print(school[2])





    







