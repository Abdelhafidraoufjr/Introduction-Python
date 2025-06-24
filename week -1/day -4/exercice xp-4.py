from Person import Person

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)
        print(f" {first_name} {self.last_name} is born into the family!")

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No member named {first_name} was found in the family.")
    def add_member(self, first_name, age):
        def family_presentation(self):
            print(f"\n👨‍👩‍👧‍👦 Family name: {self.last_name}")
            print("Members:")
            for member in self.members:
                print(f" - {member.first_name} {member.last_name}, {member.age} years old")

if __name__ == "__main__":
    smith_family = Family("Smith")

    smith_family.born("Alice", 16)
    smith_family.born("Bob", 20)
    smith_family.born("Charlie", 12)

    smith_family.family_presentation()

    smith_family.check_majority("Alice")
    smith_family.check_majority("Bob")
    smith_family.check_majority("Charlie")
    smith_family.check_majority("Derek")  
