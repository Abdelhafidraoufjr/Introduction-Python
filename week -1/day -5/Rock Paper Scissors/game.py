import random
class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        item = ['rock','paper','scissors']
        while True :
            user_input = input("choose rock, paper, scissors :").lower().strip()
            print(f"⤵️ You typed: '{user_input}'")
            if user_input in item:
                return user_input
            else:
                print("invalid input. try again.")
            
    def get_computer_item(self):
        return random.choice(['rock','paper','scissors'])
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        elif(
            user_item == "rock" and computer_item == "scissors"
            or user_item == "paper" and computer_item == "rock"
            or user_item == "scissors" and computer_item == "paper"
        ):
            return 'win'
        else:
            return 'loss'