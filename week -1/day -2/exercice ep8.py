base_price = 10.0
topping_price = 2.5
toppings = []

print("Entrez les garnitures pour votre pizza (tapez 'quit' pour terminer) :")

while True:
    topping = input("→ Garniture : ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Ajout de {topping} à votre pizza.")

total_price = base_price + len(toppings) * topping_price

print("\n--- Résumé de votre commande ---")
if toppings:
    print("Garnitures choisies :", ", ".join(toppings))
else:
    print("Aucune garniture ajoutée.")
print(f"Prix total : {total_price:.2f} $")
