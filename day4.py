#Types of Arguments in Python
#1. Positional Arguments(arguments passed in the same order as parameters)
def intro(name,age=18):
    print(f"My name is {name} and age is {age}")
intro("Pratham",19)
intro(19,"Pratham")
#2. default Arguments(takes default values if argument not given)
intro("Pratham")
#3. Keyword Arguments(can pass arguments in any order by giving variable name also)
intro(age=19,name="Pratham")

#Variable length arguments
#1.*args (takes multiple values in form of a tuple)
def calc(*exp):
    print(f"Expenses received: {exp} (Types: {type(exp)})")
    return sum(exp)
total=calc(2,10.5,8.5,15)
print(total)
#2. **kwargs (takes as key value pairs ,i.e, dictionary)
def reg(**d):
    print(d)
    print(d.items())
    for n,a in d.items():
        print(n,a)
reg(Pratham=19,Rahul=20)

#Variable Scope(Local and Global)
#in global variable if changed inside a function then it changes only copy not actual if have to change actual variable then redefine it using global var_name in function
a=10
def change():
    a=20
    print("Inside function:",a)
print("Outside function",a)

a=10
def change():
    global a
    a=20
    print("Inside function:",a)
print("Outside function",a)

#Recursive Function
def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))
#Fibonnaci Series
def fib(n):
    if(n==0): 
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))

#Data Structures
#1. List
#1.1 Append and Extend
list1=[10,20,30]
list2=[40,50]
list1.append(60)
list1.append(list2) #treats list2 as single element
list1.extend(list2)
print(list1)
#1.2 insert and remove(first ocuurence only ) and pop(we will have to give index of element to be removed and also returns removed element)
list1.insert(0,50)
print(list1)
list1.remove(50)
print(list1)
list1.pop(4)
print(a,list1)
#1.3 Slicing(list1[start:stop:step] runs upto stop-1 and can also give in -ve for backward)
print(list1[0:3])
#1.4 Sorting(.sort() by default asc if .sort(reverse=True) then desc and can also use sorted(list_name) func which returns sorted list)
sal=[10000,20000,30000,40000]
for i in range(0,len(sal)):
    sal[i]-=sal[i]*0.7
print(sal)
# Remove all occurences of -99.0
predictions=[0.15,-99.0,0.82,1.45,-99.0,0.67,2.1]
while -99 in predictions:
    predictions.remove(-99)
print(predictions)