import random

def compare_numbers(user_number):
    """
    Compare un nombre donné par l'utilisateur à un nombre aléatoire (1‑100).
    Affiche un message de réussite ou d'échec.
    """
    if not 1 <= user_number <= 100:
        print("Erreur : le nombre doit être compris entre 1 et 100.")
        return

    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("Success! 🎉 Les deux nombres sont identiques.")
    else:
        print(f"Fail! Votre nombre : {user_number}, Nombre aléatoire : {random_number}")

compare_numbers(50)  
compare_numbers(23)
