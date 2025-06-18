basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")  
basket.remove("Blueberries")  

basket.append("Kiwi")  
basket.insert(0, "Apples")  

apple_count = basket.count("Apples")  
print(f"Number of apples in the basket: {apple_count}")

# print(basket)
basket.clear()  
print(basket)