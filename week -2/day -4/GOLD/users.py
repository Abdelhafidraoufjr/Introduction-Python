# users.py (Partie 1 et 2)
users = {
    "alice": "pass123",
    "bob": "hello456",
    "charlie": "qwerty"
}

logged_in = None

while True:
    action = input("Tapez 'login', 'exit' ou 'register' : ").strip().lower()

    if action == "exit":
        print("À bientôt !")
        break

    elif action == "login":
        username = input("Nom d'utilisateur : ")
        password = input("Mot de passe : ")
        if username in users and users[username] == password:
            logged_in = username
            print(f"✅ Vous êtes maintenant connecté(e) en tant que {logged_in}")
        else:
            print("❌ Identifiants incorrects.")
            if username not in users:
                register = input("Souhaitez-vous vous inscrire ? (oui/non) ").strip().lower()
                if register == "oui":
                    while True:
                        new_username = input("Entrez un nouveau nom d'utilisateur : ")
                        if new_username in users:
                            print("❌ Ce nom d'utilisateur existe déjà.")
                        else:
                            break
                    new_password = input("Entrez un mot de passe : ")
                    users[new_username] = new_password
                    print("✅ Inscription réussie ! Vous pouvez maintenant vous connecter.")

    elif action == "register":
        while True:
            new_username = input("Entrez un nouveau nom d'utilisateur : ")
            if new_username in users:
                print("❌ Ce nom d'utilisateur existe déjà.")
            else:
                break
        new_password = input("Entrez un mot de passe : ")
        users[new_username] = new_password
        print("✅ Inscription réussie !")

