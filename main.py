from random import choice
from time import sleep
from os import system

class Jokempo(object):
    def __init__(self):
        self.options = ("stone", "paper", "scissors")
        self.name = str(input("Enter your name: ")).capitalize()
        self.player_choice = 0
        self.main()

    def menu(self, msg):
        print("="*15)
        print(msg)
        print("="*15)

    def win(self, msg):
        print("!"*30)
        print("\033[32m", msg, "\033[0;0m")
        print("!"*30)
    
    def lose(self, msg):
        print("="*30)
        print("\033[31m", msg, "\033[0;0m")
        print("="*30)

    def player_option(self):
        print(f"Welcome, {self.name}. Please, choice your option.")
        print("""
        1 - Stone
        2 - Paper
        3 - Scissors
        4 - Exit""")
        self.player_choice = int(input(""))
        if 0 < self.player_choice < 4:
            self.player_choice = self.options[self.player_choice - 1]
        elif self.player_choice == 4:
            self.menu("See you later!")
            quit()
        else:
            print("Please, enter a valid option!")
            self.player_option()

    def who_win(self):
        sleep(1)
        if (self.bot_choice == "stone" and self.player_choice == "scissors") or (self.bot_choice == "scissors" and self.player_choice == "paper") or (self.bot_choice == "paper" and self.player_choice == "stone"):
            self.lose(f"You lose! You choice was {self.player_choice} and the Bot choice was {self.bot_choice}")
        
        elif (self.bot_choice == "stone" and self.player_choice == "paper") or (self.bot_choice == "scissors" and self.player_choice == "stone") or (self.bot_choice == "paper" and self.player_choice == "scissors"):
            self.win(f"You win! Your choice was {self.player_choice} and the Bot choice was {self.bot_choice}")
        
        else:
            self.menu("Draw! You two choice the same option!")
        sleep(2)
        self.main()

    def main(self):
        system("cls")
        system("clear")
            
        self.bot_choice = choice(self.options)
        self.menu("JOKEMPO")
        self.player_option()
        self.who_win()

        
    
Jokempo()