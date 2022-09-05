# def print_h1(name):
#     print(f'hi, {name}')

# if __name__ == '__main__':
#     print_h1('PyCharm')

# print("Hello World")
# print()
# print()
# print()
# print()
# print("hello again")

# fname = input("What is your name? : ")
# print(fname)

# num1 = float(input("enter your first number: "))
# num2 = float(input("enter your second number: "))
# addnum = num1 + num2

# print(f'num 1 {num1} + {num2} = {addnum}')

# def myname(name):
#     print(f'my name is {name}')

# myname('bob')
########################################################
# def greeting(person_name):
#     myname = input('what is your name: ')
#     print(f'My name is {myname}')
###########################################################
###########################################################
###########################################################
##                     numeric check                     ##
###########################################################

# def greeting(person_name, age):
#     print(f'My name is {person_name}')
#     if age:
#         print(f'Its your Birthday!')
#         age += 1
#         print(f'You are now {age} years old')

# def getage():
#     myage = input('What is your age: ')
#     if myage.lower() == "q":
#         print("good bye")
#         exit(0)
#     return myage

# myname = input('what is your name: ')
# myage = getage()

# while not myage.isnumeric():
#     print(f"{myname}'s age is not numeric")
#     myage = getage()

# greeting(myname, int(myage))

#############################################
            ## using imports ##
            ###################

import employee #### imports from employee.py
emp_id_generator = 0

def greeting(emp):
    print(f'My name is {emp.firstname} {emp.lastname}')
    if emp.age:
        print(f'Its your Birthday!')
        emp.age += 1
        print(f'You are now {emp.age} years old')

def getage():
    myage = input('What is your age: ')
    print("hit getage")
    if myage.lower() == "q":
        print("good bye")
        exit(0)
    return myage

def get_employee_details():
    # global fname, sname, myage
    global emp_id_generator
    fname = input('please enter your first name: ')
    sname = input('please enter yoru last name ')
    myage = getage()

    while not myage.isnumeric():
        print(f"{fname}'s age is not numeric")
        myage = getage()
    emp_id_generator = emp_id_generator + 1
    emp = employee.Employee(emp_id_generator, fname, sname, int(myage) )

    return emp

emps = {}
while True:
    print("while true")
    emp = get_employee_details()
    emps[emp.id] = emp
    if input("Do you want to add another employee t the dictionary? Y/N").upper() == "N":
        break

emp = employee.Employee()
emps[emp.id] = emp
for emp_id in emps:
    emp = emps[emp_id]
    print(emp)
    print(emp.get_credentials())
    print(emp.get_age())
    # emp.set_age(250)
    emp.age = 250
    print(emp.age)
    # print(emp.get_age())

# emp_id_generator = emp_id_generator + 1
# emp.id = emp_id_generator
# emp.firstname = fname
# emp.lastname = sname
# emp.age = int(myage)

# print(f'{emp_id}: {emp.firstname} {emp.lastname} is {emp.age} years old')
# emp1 = get_employee_details()
# greeting(emp1)

# print(f'{emp1.firstname} {emp1.lastname} is {emp1.age} years old')


###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################

# myage = input('What is your age: ')
# print(f'print  var before func {myage} ')

# if not myage.isnumeric():
#     print(f"{myname}'s age is not numeric")
#     exit(0)


#############################################################


# brakes it
# if myage > 0:
#     greeting(myname, myage)
# else:
#     greeting(myname)

