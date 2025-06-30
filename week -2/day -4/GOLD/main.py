from auth_db import register_user, login_user

logged_in = None

while True:
    action = input("Tapez 'login', 'register' ou 'exit' : ").strip().lower()

    if action == "exit":
        print("👋 Fin du programme.")
        break

    elif action == "login":
        username = input("Nom d'utilisateur : ")
        password = input("Mot de passe : ")
        if login_user(username, password):
            logged_in = username
            print(f"✅ Connecté(e) en tant que {logged_in}")
        else:
            print("❌ Identifiants invalides.")
            signup = input("Souhaitez-vous vous inscrire ? (oui/non) ").strip().lower()
            if signup == "oui":
                register_user(username, password)

    elif action == "register":
        while True:
            username = input("Choisissez un nom d'utilisateur : ")
            password = input("Choisissez un mot de passe : ")
            register_user(username, password)
            break
