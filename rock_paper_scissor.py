import random


hand = ['rock', 'paper', 'scissor']
win = "YOU WON!"
lose = "YOU LOST :/"
selection = input("Welcome to Rock, Paper, Scissor!\nType 'rock', 'paper', or 'scissor' to select your weapon: ")
# new_hand = hand.remove(selection)
computer_selection = random.choice(hand)
print(f'BOT selected {computer_selection}.')


class Game:
    def __init__(self, person, computer):
        self.person = person
        self.computer = computer

    def heirarchy(self):
        if self.person == self.computer:
            print('tie try again')
            return ""
        else:
            if self.person == hand[0]:
                if self.computer == hand[1]:
                    return lose
                else:
                    return win
            if self.person == hand[1]:
                if self.computer == hand[2]:
                    return lose
                else:
                    return win
            if self.person == hand[2]:
                if self.computer == hand[0]:
                    return lose
                else:
                    return win
            if self.person not in hand:
                return 'error: invalid input'
            return ""        

gabe = Game(selection, computer_selection).heirarchy()

print(gabe)
# python
