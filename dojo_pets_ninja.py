import dojo_pets

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def __repr__(self):
        display = f"first name:{self.first_name}, last_name:{self.last_name}, pet:{self.pet}, treats:{self.treats}, pet_food:{self.pet_food}"
        return display

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()


ninja_1 = Ninja("Rapunzel", "Disney", dojo_pets.Pet("Maximus", "stallion", "gallop", 100, 1000, "whinny"), "apples", "alfalfa")
ninja_1.feed().walk().bathe()
print(ninja_1.pet)