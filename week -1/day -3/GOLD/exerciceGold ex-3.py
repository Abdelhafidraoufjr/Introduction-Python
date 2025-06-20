class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice_level": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice_level": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice_level": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice_level": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice_level": "B", "gluten": True},
        ]

    def add_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"].lower() == name.lower():
                print(f"{name} est déjà au menu.")
                return
        self.menu.append({
            "name": name,
            "price": price,
            "spice_level": spice,
            "gluten": gluten
        })
        print(f"{name} a été ajouté au menu.")

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"].lower() == name.lower():
                item["price"] = price
                item["spice_level"] = spice
                item["gluten"] = gluten
                print(f"{name} a été mis à jour.")
                return
        print(f"{name} n'est pas dans le menu.")

    def remove_item(self, name):
        for item in self.menu:
            if item["name"].lower() == name.lower():
                self.menu.remove(item)
                print(f"{name} a été supprimé du menu.")
                return
        print(f"{name} n'est pas dans le menu.")

    def display_menu(self):
        print("📋 Menu actuel :")
        for item in self.menu:
            gluten_status = "Oui" if item["gluten"] else "Non"
            print(f"- {item['name']} | {item['price']}€ | Épicé: {item['spice_level']} | Gluten: {gluten_status}")
    
if __name__ == "__main__":
    manager = MenuManager()

    manager.display_menu()

    print("\nAjout d'un nouveau plat :")
    manager.add_item("Pizza", 20, "B", True)

    print("\nMise à jour d'un plat existant :")
    manager.update_item("Pizza", 22, "C", False)

    print("\nSuppression d'un plat :")
    manager.remove_item("Soup")

    print("\nMenu après modifications :")
    manager.display_menu()
