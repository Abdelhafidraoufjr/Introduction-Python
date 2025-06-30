from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("Menu Editor")
    print("V. Afficher un article")
    print("A. Ajouter un élément")
    print("D. Supprimer un élément")
    print("U. Mettre à jour un élément")
    print("S. Afficher le menu ")
    print("E. Exit")
def add_item_to_menu():
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    item = MenuItem(item_name, item_price)
    item.save()
    print(f"Item '{item_name}' added with price {item_price}.") 
def remove_item_from_menu():
    item_name = input("Enter item name to delete: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        item.delete()
        print(f"Item '{item_name}' deleted.")
    else:
        print(f"Item '{item_name}' not found.")
def update_item_in_menu():
    item_name = input("Enter item name to update: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        new_name = input("Enter new item name: ")
        new_price = float(input("Enter new item price: "))
        item.update(new_name, new_price)
        print(f"Item '{item_name}' updated to '{new_name}' with price {new_price}.")
    else:
        print(f"Item '{item_name}' not found.")               
def show_restaurant_menu():
    items = MenuManager.all()
    if items:
        print("Restaurant Menu:")
        for item in items:
            print(f"{item.item_name} - {item.item_price}")
    else:
        print("No items in the menu.")        


if __name__ == "__main__":  
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").upper()
        if choice == 'V':
            item_name = input("Enter item name to view: ")
            item = MenuManager.get_by_name(item_name)
            if item:
                print(f"Item: {item.item_name}, Price: {item.item_price}")
            else:
                print("Item not found.")
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_in_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            print("Exiting the menu editor.")
            break
        else:
            print("Invalid choice. Please try again.")
                    