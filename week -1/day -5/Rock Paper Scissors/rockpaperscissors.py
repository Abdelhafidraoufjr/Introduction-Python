from game import Game


def get_user_menu_choice():
    data = ['1','2','3']
    print("Menu \n")
    print("1- Play a new game.")
    print("2- Show scores.")
    print("3- Quit.")

    choice = input("Enter you choice :").lower().strip()

    if choice in data:
        return choice
    else:
        print("Invalid choice!")
        return None
    
def print_results(results):
    print("Résultats des parties jouées :")
    print(f"- Parties gagnées : {results['win']}")
    print(f"- Parties perdues : {results['loss']}")
    print(f"- Parties nulles : {results['draw']}")
    print("Merci d’avoir joué !")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "1":
            game = Game()
            user = game.get_user_item()
            computer = game.get_computer_item()
            result = game.get_game_result(user, computer)
            results[result] += 1

        elif choice == "2":
            print_results(results)

        elif choice == "3":
            print_results(results)
            break