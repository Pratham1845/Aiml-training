#ATM simulator
balance = 1000
while True:
    print("Welcome to ATM Simulator\nPlease choose one options:\n1. Check Balance\n2. Withdraw Money\n3. Deposit Money\n4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print(f"Your Balance is: {balance}")
    elif choice == 2:
        amt=int(input("Enter Amount to withdrew: "))
        if amt<=balance:
            balance-=amt
            print(f"Updated Balance: {balance}")
        else:
            print("Insufficient balance")
    elif choice==3:
        amt=int(input("Enter amount to deposit: "))
        balance+=amt
        print(f"Updated balance: {balance}")
    elif choice==4:
        print("Exiting...")
        break
    else:
        print("Choose valid option(1,2,3,4)")

#Shopping Cart Simulator

#Functions

#1. Built in functions (len,sum,max,min,abs,round(number,digits(precision)),print)
str="Hello"
l=[1,2,3,4,5,6,7]
print(len(str),len(l))

#2. Custom Functions and parameters and arguments
def sum(a,b):
    print(f"Sum: {a+b}")
sum(4,5)

def calculator(a,b,op):
    if op=="+":
        print(f"Sum: {a+b}")
    elif op=="-":
        print(f"Difference: {a-b}")
    elif op=="*":
        print(f"Multipilication: {a*b}")
    elif op=="/":
        print(f"Division: {a/b}")
calculator(10,4,'+')
# return statement in functions
# Prime numbers
def is_prime(num):
    for i in range(2,int(num**0.5)+1,1):
        if num==i: continue
        if num%i==0:
            return False
    else:
        return True
num=int(input("Enter any no.:"))
if(is_prime(num)):
    print("The no. is prime")
else:
    print("Not prime")