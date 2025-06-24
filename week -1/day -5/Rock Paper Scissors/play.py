from game import Game

def play():
    game = Game()
    user = game.get_user_item()
    computer = game.get_computer_item()
    result = game.get_game_result(user, computer)

    print(f'You selected : {user}')
    print(f'The computer rockselected : {computer}')

    if result == 'win':
        print("✅ You win!")
    elif result == 'loss':
        print("❌ You lose.")
    else:
        print("🤝 It's a draw.")

    return result