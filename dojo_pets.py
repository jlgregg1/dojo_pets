class Pet:
    def __init__(self, name, type, tricks, energy, health, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health
        self.sound = sound
    
    def __repr__(self):
        display = f"Name:{self.name}, type:{self.type}, tricks:{self.tricks}, energy:{self.energy}, health:{self.health}, sound:{self.sound}"
        return display

    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy +=5
        self.health +=10
        return self
    def play(self):
        self.health +=5
        return self
    def noise(self):
        print(self.sound)
        return self

class Dog(Pet):
    def __init__(self, name, type, tricks, energy, health, sound, fleas):
        super().__init__(name, type, tricks, energy, health, sound)
        type = "dog"
        self.type = type
        self.fleas = fleas

    def __repr__(self):
        display = f"Name:{self.name}, type:{self.type}, tricks:{self.tricks}, energy:{self.energy}, health:{self.health}, sound:{self.sound}, fleas:{self.fleas}"
        return display
    
    def sleep(self):
        self.energy += 100
        return self

pet_1 = Pet("Fluffy", "dog", "fetch", 5, 10, "woof")
pet_1.noise().play().eat().sleep()
print(pet_1)

dog_1 = Dog("Fido", "dog", "roll over", 10, 50, "woof", False)
dog_1.noise().play().eat().sleep()
print(dog_1)


