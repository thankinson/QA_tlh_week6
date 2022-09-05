import cryberpetclass
pet_id_generator = 0

def get_pet_age():
    page = input("What is your pets age: ")
    if page.lower() == "q":
        print("Good Bye")
        exit(0)
    return page

def get_cyberpet_details():
    global pet_id_generator
    pname = input("What is your pets name: ")
    ptype = input("What type of pet do you have: ")
    page = get_pet_age()

    while not page.isnumeric():
        print(f"what is {pname}'s age?")
        page = get_pet_age()
    
    pet_id_generator = pet_id_generator + 1
    cyberPet = cryberpetclass.Cyberpet(pet_id_generator, pname, ptype, int(page))

    return cyberPet

pets = {}
while True:
    cyberpet = get_cyberpet_details()
    pets[cyberpet._id] = cyberpet
    if input("Do you want to addd another pet: Y/N").upper() == "N":
        break

cyberpet = cryberpetclass.Cyberpet()
pets[cyberpet._id] = cyberpet

for pet_id in pets:
    cyberpet = pets[pet_id]
    print(cyberpet.get_pet_details())
    print(cyberpet.feed_pet())
    print(cyberpet.pet_play())

    