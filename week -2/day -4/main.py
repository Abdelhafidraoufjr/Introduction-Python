from menu_item import MenuItem
from menu_manager import MenuManager

item = MenuItem('Burger', 35)
item.save()
print(f"Item saved: {item.item_name} at price {item.item_price}")

item.delete()
print(f"Item deleted: {item.item_name}")

item.save()  
item.update('Veggie Burger', 37)

item2 = MenuManager.get_by_name('Beef Stew')
if item2:
    print(f"Item: {item2.item_name}, Price: {item2.item_price}")
else:
    print("Item not found.")

items = MenuManager.all()
for i in items:
    print(f"{i.item_name} - {i.item_price}")
