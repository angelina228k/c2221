class Vet:
    def __init__(self, name):
        self.name = name

    def treat_pet(self, pet):
        if not pet.is_healthy:
            print(f"Ветеринар {self.name} лікує {pet.name}.")
            pet.hunger = max(0, pet.hunger - 20)
            pet.energy = min(100, pet.energy + 30)
            pet.happiness = min(100, pet.happiness + 20)
            pet.is_healthy = True
            print(f"{pet.name} тепер здоровий!")
        else:
            print(f"{pet.name} здоровий(-а) і не потребує лікування.")

if __name__ == "__main__":

    owner = Owner("Олексій")

    pet1 = Pet("Барсик", "котик")
    pet2 = Pet("Рекс", "собачка")
    vet = Vet("Доктор Айболить")
    owner.adopt_pet(pet1)
    owner.adopt_pet(pet2)

    owner.care_for_pets()
    owner.show_pets_status()

    print("Візит до ветеринара:")
    for pet in owner.pets:
        vet.treat_pet(pet)

    owner.show_pets_status()