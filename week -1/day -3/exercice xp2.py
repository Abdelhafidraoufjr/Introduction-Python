class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait ouaf")

    def jump(self):
        print(f"{self.name} saute de {self.height * 2} cm") 


dog1 = Dog("Rex", 50)

print(f"Le chien {dog1.name} mesure {dog1.height} cm.")
dog1.bark()
dog1.jump()
