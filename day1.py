#Variables
x=10
y=10
z=x
print(f"Value of x: {x}")
print(f"Type of x: {type(x)}")
print(f"Memory of x(id): {id(x)}")
print(f"Memory of x(id): {id(y)}")
print(f"Are they same: {x is y}")
print(f"Are they same: {z is y}")
#Data Types
#1. Data types of numeric int,float complex
comp=2+4j
print(comp.real,comp.imag)
#2.Data type Strings single line and multiple line
s="Hello"
ms="""H
E
L
L
O"""
print(s)
print(ms)
#3. Boolean & None Types for none write None in var
# Mutability(list,dict,sets) And Immutability(int,float,string etc.)
#Operators
#1. Arithematic Operators
a=int(input("Enter any no.:"))
b=2
print(a+b,a-b,a/b,a//b,a%b,a**b)
#Even odd using if else
if a%b==0:
    print("Even")
else:
    print("Odd")
#2. Comparison Operators (==,!=,>,<,>=,<=)
#3. Logical Operators (and,or,not)
n1=int(input("Enter num1: "))
n2=int(input("Enter num2: "))
n3=int(input("Enter num3: "))
if n1>n2 and  n1>n3:
    print(f"{n1} is the greatest")
elif n2>n1 and n2>n3:
    print(f"{n2} is the greatest")
else:
    print(f"{n3} is the gratest")
#4. Assignment Operators (=,+=,*=,-= etc..)
#5. Bitwise Operators (&,|,^,~,<<,>>)