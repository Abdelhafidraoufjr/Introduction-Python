# Provided family data
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

# Loop through the dictionary and calculate prices
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name.capitalize()} (age {age}) ticket price: ${price}")
    total_cost += price

# Print the total cost
print(f"\nTotal cost for the whole family: ${total_cost}")
