from random import choice,randint


class Game:
    # def __init__(self,user=0):
    #     self.user_choice = user
    def body_rock_paper_scissors(self,user_choice):
        # print("Please choose one of these items:\n1.rock\n2.Paper\n3.scissors")
        items = ["rock","paper","scissors"]
        com_choice = choice(items)
        if user_choice == com_choice:
            return "Draw\n\nNew round:\n"
        elif user_choice == "rock" and com_choice == "paper":
            return f"You lost.\ncomputer`s choice: {com_choice}\n\nNew round:\n"
        elif user_choice == "rock" and com_choice == "scissors":
            return f"Excellent!!!\nYou won\ncomputers choice: {com_choice}\n\nNew round:\n"
        elif user_choice == "paper" and com_choice == "rock":
            return f"Excellent!!!\nYou won\ncomputers choice: {com_choice}\n\nNew round:\n"
        elif user_choice == "paper" and com_choice == "scissors":
            return f"You lost.\ncomputers choice: {com_choice}\n\nNew round:\n"
        elif user_choice == "scissors" and com_choice == "rock":
            return f"You lost.\ncomputers choice: {com_choice}\n\nNew round:\n"
        elif user_choice == "scissors" and com_choice == "paper":
            return f"Congratulations!!!\nYou won\ncomputers choice: {com_choice}\n\nNew round:\n"

    def paly_rock_paper_scissors(self): #user_choice
        while True:
            user_choice = input("Enter rock,paper or scissors(press 'e' to exit or press 'n' to play next game):")
            if user_choice == "e":
                return "Exiting..."
            elif user_choice == 'n':
                print("\nGuess number:","\n")
                self.play_guess_num(int(input('Enter the 1sh bound: ')),int(input('Enter the 2sh bound: ')))
            print(self.body_rock_paper_scissors(user_choice))


    def play_guess_num(self,a,b):
        i = 3
        com_guess = randint(a, b)
        while i > 0:
            user_guess = int(input("Enter your guess:"))
            if user_guess == com_guess:
                return "Excellent!\nYou Won"
            if i != 1:
                if user_guess < com_guess:
                    print('Smaller')
                elif user_guess > com_guess:
                    print('Bigger')
            i -= 1
        else:
            print(f'You Lost\nThe number was {com_guess}')
            return


print("Which game do you like to play?\n1.rock,paper,scissors\n2.Guess number\n")
user = input("Enter the number of game:")
game = Game()
if user=="1":
    print("rock,paper,scissors:", "\n")
    print(game.paly_rock_paper_scissors())
elif user=="2":
    print("Guess number:", "\n")
    first_bound = int(input('Enter the 1sh bound: '))
    second_bound = int(input('Enter the 2sh bound: '))
    game.play_guess_num(first_bound,second_bound)
else:
    print("Invalid input, please try again.")
# print(input("Press enter to play next game"))
# print(input("Press enter to exit"))