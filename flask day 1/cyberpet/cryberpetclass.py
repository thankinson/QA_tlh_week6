class Cyberpet():
    def __init__(self, id = -1, petName = "pet", petType = "dog", petAge = 2):
        self._id = id
        self._petName = petName
        self._petType = petType
        self._petAge = petAge
        self._petHealth = 50

    def __str__(self):
        return f'Pet ID: {self._id}, Pet Name: {self._petName}, Species: {self._petType}, Pet Age: {self._petAge}'

    def get_pet_details(self):
        return f'---------- \nPet Name: {self._petName} \nPet Type: {self._petType} \nPet Age: {self._petAge} \n----------'

    def feed_pet(self):
        petHealth = self._petHealth + 5
        return f'{self._petName} health increased by 5 to {petHealth}'

    def pet_play(self):
        petHealth = self._petHealth - 10
        return f'after playing with {self._petName}, its health dropped to {petHealth}'

    def pet_sleep(self):
        if self._petHealth < 5:
            return f"{self._petName} helth is {self._petHealth} and requires sleep or food to recover"
    
    