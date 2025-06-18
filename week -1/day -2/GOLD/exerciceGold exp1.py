birthdays = {
    "Alice": "1992/04/12",
    "Bob": "1988/11/23",
    "Charlie": "2000/07/05",
    "Diana": "1995/09/30",
    "Ethan": "1983/12/17"
}

print("Bienvenue dans le répertoire des anniversaires !")
print("Vous pouvez consulter les dates d'anniversaire des personnes de la liste.")

name = input("Entrez le nom de la personne : ")

if name in birthdays:
    print(f"L'anniversaire de {name} est le {birthdays[name]}.")
else:
    print(f"Désolé, je ne connais pas l'anniversaire de {name}.")
