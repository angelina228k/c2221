class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
    def feed(self, food_amount):
        self.hunger = max(0, self.hunger - food_amount)
        print(f"{self.name} поїв(-ла)! Рівень голоду: {self.hunger}")

    def play(self):
        if self.energy >= 10:
            self.happiness = min(100, self.happiness + 20)
            self.energy = max(0, self.energy - 10)
            print(f"{self.name} пограв(-ла) і став(-ла) щасливішим(-ою)! "
                  f"Рівень щастя: {self.happiness}, енергії: {self.energy}")
        else:
            print(f"{self.name} занадто втомлений(-а), щоб гратися.")

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.happiness = max(0, self.happiness - 5)
        print(f"{self.name} поспав(-ла). Рівень енергії: {self.energy}, щастя: {self.happiness}")

    def status(self):
        print(f"Ім'я: {self.name}, Вид: {self.species}")
        print(f"Рівень голоду: {self.hunger}, Енергії: {self.energy}, Щастя: {self.happiness}")

# Демонстрація використання класу
if __name__ == "__main__":
    my_pet = Pet("Барсик", "котик")

    my_pet.status()
    my_pet.feed(20)
    my_pet.play()
    my_pet.sleep()
    my_pet.status()