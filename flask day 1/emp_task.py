import employee 
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
    emp.age = 250
    print(emp.age)
