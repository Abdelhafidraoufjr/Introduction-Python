import random

def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 10), 1)
    elif season == "spring":
        return round(random.uniform(10, 20), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn":
        return round(random.uniform(5, 20), 1)
    else:
        return round(random.uniform(-10, 40), 1)  # au cas où

def get_season(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return "unknown"

def main():
    try:
        month = int(input("Entrez le mois actuel (1 à 12) : "))
        season = get_season(month)
        temp = get_random_temp(season)

        print(f"\nLa température actuelle est de {temp}°C.")

        if temp < 0:
            print("Brrr, il fait un froid de canard ! Portez des couches supplémentaires aujourd'hui.")
        elif temp < 16:
            print("Il fait plutôt frais ! N'oubliez pas votre manteau.")
        elif temp < 24:
            print("Beau temps.")
        elif temp < 32:
            print("Un peu chaud, restez hydraté.")
        else:
            print("Il fait vraiment chaud ! Restez au frais.")
    except ValueError:
        print("Veuillez entrer un mois valide sous forme de nombre (1 à 12).")

main()
