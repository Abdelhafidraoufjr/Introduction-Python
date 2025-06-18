birthdays = {
    "Alice": "1992/04/12",
    "Bob": "1988/11/23",
    "Charlie": "2000/07/05",
    "Diana": "1995/09/30",
    "Ethan": "1983/12/17"
}

print("Bienvenue dans le répertoire des anniversaires !")
print("Voici les personnes dont nous connaissons les anniversaires :")

for name in birthdays:
    print("-", name)

person_name = input("\nEntrez le nom de la personne : ")

if person_name in birthdays:
    print(f"L'anniversaire de {person_name} est le {birthdays[person_name]}.")
else:
    print(f"Désolé, nous n'avons pas les informations d'anniversaire pour {person_name}.")
