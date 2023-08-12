
Example for Execution of lines of code ---
def hello() :
    print("Good Morning!")
    print("How are you..??")
    print("What's up??")
print("hi")
print("hello")
hello()
print("done!")


 Example for add two num using function :-

def add(a,b): 
 return a+b 
result=add(12,15)
print(result)


Another Example --------------------------------------

def hf(str):
  return str
result = hf("hello world")
print(result)

Another Example --------------------------------------

def hf():
 print("hw")
 print("gh kfjg 66666")
hf()
hf()

Another Example --------------------------------------

def add(x,y):
 c=x+y
 print(c)
add(5,4)

Another Example --------------------------------------

def add_sub(x,y) :
  c=x+y
  d=x-y
  print(c,d)
add_sub(15,5)

Another Example --------------------------------------

def multi(a,b) :
  c = a * b
  print(c)
multi(10,20)

Another Example --------------------------------------
  
def hf():
 return "Hello"
print(hf())

Another Example --------------------------------------

def hello(wish):
 return '{}'.format(wish)
print(hello("mrcet"))


Another Example --------------------------------------

def greet(gesture,name) :
    print("Hello " + '' + gesture  + '' +  name)
greet("Good Morning ", "Anand")

def hello(wish,name='anand'):
 return '{},{}'.format(wish,name)
print(hello("good morning"))


Another Example --------------------------------------

def wish(*names):
 
 for name in names:
  print("Hello",name)
wish("MRCET","CSE","SIR","MADAM")

"""This function greets all
 the person in the names tuple."""
 # names is a tuple with arguments

 
Another Example --------------------------------------

--------------- To find the area of Circle-------------------------  
pi = 3.14
def area_of_circle () :
  d = int(input(("Enter the diameter : ")))
  a = pi*d
  print("Area of Circle is : ", a)
area_of_circle()


 Program to write sum different product and using arguments with return value function.

def calculate(a,b) :
    sum = a+b
    product = a*b
    subtract = a-b
    mod = a%b
    division = a/b
    return(sum,product,subtract,mod,division)
a = int(input(("Enter the value of a ")))
b = int(input(("Enter the value of b ")))
s,p,d,m,q =calculate(a,b)
print("Sum= ",s,"diff= ",d,"mul= ",p,"div= ",q,"mod= ",m)


Write a program to find biggest of two numbers using functions.

def biggest(a,b):
 if a>b :
  return a
 else :
  return b
 
a=int(input("Enter a value"))
b=int(input("Enter b value"))
#function call 
big= biggest(a,b)
print("big number= ",big)
 
Another Example --------------------------------------

i=1
while i<=3:
 print("MRCET",end=" ")
 j=1
 while j<=1:
   print("CSE DEPT",end="")
   j=j+1
 i=i+1
 print()

i = 1
while (i < 10):
  print (i)
  i = i+1

def f2():
 y = "local"
 print(y)
f2()

--------------------------------------------------------------------------
x = "global"
def f3():
 global x
 y = "local"
 x = x * 2
 print(x)
 print(y)
 
f3()

--------------------------------------------------------------------------------

Recursion Function :-

   Find Factorial of number 0 and 5

def fact(x) :
  if x == 0 :
     result = 1
  else :
     result = x*fact(x-1)
  return result
print(fact(0))
print(fact(5))
---------------------OR------------------------------------

def fact(x):
 if x==0:
  result = 1
 else :
  result = x * fact(x-1)
 return result
print("zero factorial",fact(0))
print("five factorial",fact(5))

------------------------OR------------------------------------------

def calculate_fact(a) :
    if a == 0 :
     return 1
    else :
        result = a * calculate_fact(a-1)
    return result
calculate_fact(10)
print("The factorial of 10 is",calculate_fact(10))

-------------------------OR---------------------------------------------

def calc_factorial(x):
 """This is a recursive function
 to find the factorial of an integer"""
 if x == 1:
  return 1
 else:
  return (x * calc_factorial(x-1))
num = 4
print("The factorial of", num, "is", calc_factorial(num))

-------------------------------------------------------------------------


Strings methods ------


string="123alpha"
str = string.isalnum()     #Alpha Numeric
print(bool(str))


string="ABC"
str1 = string.isalpha()    #Alphabets only
print(bool(str1))

string="789456123"
str2 = string.isdigit()      #Digits only
print(bool(str2))


string="abc"
str3 = string.islower()     #Lowercase 
print(bool(str3))

string="123456789"
str4 = string.isnumeric()      #Numerics only
print(bool(str4))

string=" "
str5 = string.isspace()         #Space 
print(bool(str5)) 

string="Nikhil Is Learning"
str6 = string.istitle()           #Title
print(bool(str6)) 


string="HELLO"
str7 = string.isupper()         #Only Uppercase
print(bool(str7)) 


string="Nikhil Is Learning"
new_string = string.replace('Nikhil','Anand')   #Replace
print(new_string) 

string="NikhilIsLearning"
str8 = string.split()                #Split
print(bool(str8))
print(str8) 


string='Nikhil Is Learning'
str9 = string.count('b')                 #Count
print(bool(str9)) 


string="Nikhil Is Learning"
str10 = string.find('a')                 #Find a letter from index 0
print(bool(str10)) 
print(str10)

string="HELLO"
string.swapcase()              #Swapcase
print(bool(string)) 



string="Nikhil Is Learning"
string.startswith('N')          #startswith
print(bool(string)) 



string="Nikhil Is Learning"
string.startswith('g')         #endswith  
print(bool(string)) 

--------------------------------------------------------------------------------------
Using Recursive Method

def fact(x) :
    if x == 0 :
       return 1
    else :
      result = x*(fact(x-1))  
      return result

fact(5)
print("Factorial of 5 is ",fact(5) )

----------------------------------OR--------------------------------------------------
 
def factorial(n):

    if n == 0 or n == 1:
        return 1

    result = 1
    for num in range(1, n+1):
        result = result * num
    
    return result

n = 5
ans = factorial(n)
print("Factorial of number ",n, " = ", ans)

------------------------------------OR----------------------------------------------
def fact(n) :
    if n == 0 :
        return 1
    result = 1

    for i in range(1, n+1) :
        result = result * i
    return result

num = 2
fact(num)
print("The factorial of ",num,"is",fact(num))

------------------------------------------------------------------------------------

Write a program to find a square and cube of numbers

def square_cube(a) :
    if a == 0  :
        return 1
    else :
        sqr = a*a 
        cub = a*a*a
        return sqr, cub

num1 = 5  
sqr1, cub1 = square_cube(num1)
print("The square of ",num1, "is",sqr1)
print("The cube of ",num1, "is",cub1)

---------------------------OR-----------------------------------------------------------------------

def square_and_cube(n):
    sqr = n*n
    cube = n*n*n
    return sqr,cube

num = 3
sqr_ans , cube_ans = square_and_cube(num)
print("Square of ",num," is : ",sqr_ans)
print("Cube of ",num," is : ",cube_ans)
    
--------------------------------------------------------------------------------------------------------

Write a program to create a table of 5 using for loop ----

num = 20
for i in range(1, 11) :
 a = num * i
 print(f"{num} *", i, "=", (a))

 -------------------------------------------OR------------------------------------------------------------
for i in range(1, 11):
    print("10 *", i, "=", (10 * i))
----------------------------------------------------------------------------------------------------

Write a program to create a table of 5 using FUNCTION 

def table(num) :
 for i in range(1,11) :
  a = num * i
  print(f"{num} * {i} = {a}")

table(10)

----------------------------------------------------------------------------------------------------
How to create optional arguments in python fucntions

def opt_arguments(a, b=15) :
    c = a*b
    print(c)

a = 2
b = 10
opt_arguments(a,b)

----------------------------------------------------------------------------------------------------------

def opt_arguments(a, b=15, c=10) :
    d = a*b*c
    print(d)

a = 2
b = 10
c = 2
opt_arguments(a,b,c)

---------------------------------------------------------------------------------------------

Lambda Functions ------------------------

First normal function to add integer 5 in given number
def add_five(num):
    result = num + 5
    return result



How to create Lambda Functions----

lambda_add_five = lambda x : x + 5

x = 10
print(lambda_add_five(x))

Write a lambda function to add two input numbers

lambda_add_two_num = lambda c : a + b

a = 5
b = 30
c = 0
print(lambda_add_two_num(c))

----------------------------------OR---------------------------------------

lambda_add_two_nums = lambda x , y : x + y

a = 30
b = 20
print(lambda_add_two_nums(a,b))

Wite a lambda function to concatenate two input strings

lambda_add_two_input_strings = lambda x , y : x + y

x = "Anand"
y = " Madkar"

print(lambda_add_two_input_strings(x,y))

-------------------------------------------------------------------------------------

Write a lambda function to calculate maximum of two numbers

lambda_max_of_two_nums = lambda x,y : x if x > y else y 

x = 40
y = 30

print(lambda_max_of_two_nums(x,y))

-------------------------------------------------
How to work with map() , filter(), reduce()
--------------------------------------
Map Function 
--------------------------------
implement map function

list1 = [1,2,3,4,5,6,7,8,9]

square_num = lambda x : x*x

square_list = list(map(square_num, list1))
print(square_list)

------------------------------------------------------------------------------------
 Example to sqaure the each num of list using function :-

def square_list(lst):
    result = [x ** 2 for x in lst] 
    return result
    
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]   
result = square_list(lst)
print(square_list(lst))

Add sequential respective elements in two given lists using map function 

list_a = [1,2,3,4,5]
list_b = [5,4,3,2,1]

add_elements = lambda x, y : x + y

result =  list(map(add_elements , list_a, list_b ))
print(result)

--------------------------------------------------------------------------------------

Reduce Function -----------------

----------------------------------------------------------------------------------------

How to use reduce functions -

import functools

list_x = [1,2,3,4,5]

# Add two nums --------
add_two_nums = lambda x , y : x + y
result = functools.reduce(add_two_nums , list_x)
print(result)

# Multiply two nums--------
multiply_two_nums  = lambda x , y : x * y
result = functools.reduce(multiply_two_nums , list_x)
print(result)

----------------------------------------------------------------------------------------

How to use filter ()

Create list of only odd elements
seq = [1,2,5,6,9,7,10]

filter_odd = lambda x : x % 2 != 0

result = list(filter(filter_odd , seq))
print(result)

filter_even = lambda x : x % 2 == 0

result = list(filter(filter_even , seq))

print(result)

-------------------------------------------------------------------------------------------

List Comprehension 

Write a program to generate list of 10 numbers
result = []
for i in range(1,11):
    result.append(i)

print(result)

Write a program to multiply each element of list with 2

result = []
for i in range(1,11) : 
    result.append(i*2)
print(result)   


Write a program to find even nums from the list

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25]

for i in list :
    if i%2 == 0 :
        result = i
        print(result)

Write a program to find even nums from the list

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25]

for i in list :
    if i%2 == 0 :
        result = i
        list(result)
        print(result)
-----------------------------------------------------------------------------------
Write a program to find odd nums from the list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25]
result_list = []

for i in original_list:
    if i % 2 != 0:
        result_list.append(i)

print(result_list)

convert all string into upper case in given list
list_a = ['hi', 'hello' , 'bye' , 'nice']

result = [ x.upper() for x in list_a  ]
print(result)

----------------------------------------------------------------------------------------

Put all negative numbers after positive numbers from given list
list_a = [9,-1,2,-5,1,10,-6]

# result = [9,2,1,10,-1,-5,-6]
# result1= [x for x in list_a if x>0 ]
# result2= [x for x in list_a if x<0 ]
# print (result1 + result2)

result = [ x for x in list_a if x>0 ] + [ x for x in list_a if x<0 ]
print (result)
 
-----------------------------------------------------------------------------------------------------

CLASS AND OBJECTS (OOPS CONCEPTS)********************************
********************************************************************************************

How to create a class in Python

class Employee:
    # Constructor of class

    # it is mainly used for assignment of instance variables
    def __init__(self, name, salary ):

        # instance variable or instance attributes
        self.emp_name = name
        self.emp_salary = salary

    # method of a class
    def displayEmployeeInfo(self):
        print("Employee name : ",self.emp_name, " , Employee Salary : ",self.emp_salary)

emp1 = Employee('Shashank', 1000)
emp2 = Employee('Rahul', 2000)

emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()

print(emp1.emp_name)
print(emp2.emp_name)


----------------------------------------------------------------------------------------

class Employee:

    # Class attribute
    empCount = 0

    # Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self, name, salary ):
        # instance variable or instance attributes
        self.emp_name = name
        self.emp_salary = salary
        Employee.empCount += 1

    # method of a class
    def displayEmployeeInfo(self):
        print("Employee name : ",self.emp_name, " , Employee Salary : ",self.emp_salary)

        # method of a class
    def displayEmployeeCount(self):
        print("Employee Count : ",Employee.empCount)

emp1 = Employee('Shashank', 1000)
emp1.displayEmployeeInfo()
emp1.displayEmployeeCount()

emp2 = Employee('Rahul', 2000)
emp2.displayEmployeeInfo()
emp2.displayEmployeeCount()


emp1.displayEmployeeCount()
emp2.displayEmployeeCount()

