car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

manufacturers = [m.strip() for m in car_string.split(",")]

print(f"Il y a {len(manufacturers)} fabricants dans la liste.")

print("Fabricants en ordre décroissant (ZA) :")
for name in sorted(manufacturers, reverse=True):
    print("-", name)

count_with_o = sum(['o' in m.lower() for m in manufacturers])
print(f"\nNombre de fabricants contenant la lettre 'o' : {count_with_o}")

count_without_i = sum(['i' not in m.lower() for m in manufacturers])
print(f"Nombre de fabricants ne contenant pas la lettre 'i' : {count_without_i}")

dup_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

unique_manufacturers = list(set(dup_list))

print("\nEntreprises sans doublons :")
print(", ".join(unique_manufacturers))
print(f"Nombre total d'entreprises sans doublons : {len(unique_manufacturers)}")

print("\nFabricants (lettres inversées, triés A-Z) :")
for name in sorted(unique_manufacturers):
    print("-", name[::-1])
