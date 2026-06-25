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