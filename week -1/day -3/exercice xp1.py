class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = max([cat1, cat2, cat3], key=lambda cat: cat.age)
    print(f"Le chat le plus âgé est {oldest_cat.name}, il a {oldest_cat.age} ans.")


cat1 = Cat("mimi", 1)
cat2 = Cat("meow", 3)
cat3 = Cat("rio", 7)


find_oldest_cat(cat1,cat2,cat3)

