#impooter Dog class from exercice xp-2

from week_1.day_4.exercice_xp2 import Dog

import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        all_names = ", ".join([self.name] + list(dog_names))
        print(f"{all_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet.")
if __name__ == "__main__":
    dog1 = PetDog("Fido", 2, 10)
    dog2 = PetDog("Buddy", 3, 15)
    dog3 = PetDog("Max", 4, 12)

    dog1.train()            

    dog1.play(dog2.name, dog3.name)

    dog1.do_a_trick()        
    dog2.do_a_trick()       
