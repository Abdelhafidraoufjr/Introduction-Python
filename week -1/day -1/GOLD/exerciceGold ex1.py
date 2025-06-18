month = int(input("Entrez un mois entre 1 et 12 : "))

if 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    print("Erreur !! Mois invalide.")
1