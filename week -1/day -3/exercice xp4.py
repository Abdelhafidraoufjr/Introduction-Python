class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, animal_name):
        if animal_name not in self.animals:
            self.animals.append(animal_name)
            print(f"{animal_name} ajouté")
        else:
            print(f"{animal_name} est déjà présent")

    def get_animals(self) -> None:
        new_animals_list = []
        for animal in self.animals:
            if animal not in new_animals_list:
                new_animals_list.append(animal)

        self.animals = new_animals_list

        if self.animals:
            print("Animaux du zoo :", ", ".join(self.animals))
        else:
            print("Le zoo est vide pour l’instant")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} vendu")

    def sort_animals(self):
        self.animals.sort()
        print("Animaux triés :", ", ".join(self.animals))






my_zoo = Zoo("Mon Zoo")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Tigre")
my_zoo.add_animal("Lion") 
my_zoo.add_animal("Ours")
my_zoo.add_animal("Tigre")  
my_zoo.add_animal("Zèbre")

my_zoo.sell_animal("Lion")
my_zoo.get_animals()
my_zoo.sort_animals()