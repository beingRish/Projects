import random
import time
import sys

def player_detail():
    player_name = input("Enter Your Name: ")
    return player_name

def greetings_for_player():
    struct_type_time=time.localtime()
    hours=int(time.strftime("%H",struct_type_time))
    if hours>=0 and hours<12:
        return "Good Morning"
    elif hours>=12 and hours<17:
        return "Good Afternoon"
    elif hours>=17 and hours<20:
        return "Good Evening"
    else:
        return "Good Night"

def result_decorator():
    for _ in range(32):
        print("-",end="")
    print()

def exit_game():
    print("\n-------Game Ended-------")
    sys.exit()

def valid_choice_exit_game():
    print("\nPlease Enter a Valid Choice Next Time !")
    print("\n-------Game Ended-------")
    sys.exit()

def quit_choice_game_exit():
    print("\nYou Quit Game !")
    print("\n-------Game Ended-------")
    sys.exit()

def introduction_to_game():
    input("{}, {}. Welcome To The Rock Paper Scissor Game: ".format(greetings_for_player(),player_detail()) + "[Press Enter Key To Continue Game]  ")
    print("\nLet's take a Look how to play this Game: \n")
    print("1.  You have to Choose from Rock, Paper and Scissor. ")
    print("2.  After, You Enter your Choice, computer also randomly Chose one option.")
    print("3.  If Your Choice and computer Choice are same, then it will be counted as Draw or Tie Game")
    print("4.  If Your Choice and Computer Choice are distinct, then the stronger object among both objects Wins.")
    print("5.  To Quit Game, Enter \"Quit\" in your choice Section.")
    game_began_choice = input("\nSo Let's began with the Game [Y/N]:   ")
    print()
    if game_began_choice in ["Y","N"]:
        if game_began_choice=="Y":
            game_logic()
        else:
            quit_choice=input("Do You Want to Quit Game[Y/N]: ")
            if quit_choice in ["Y","N"]:
                if quit_choice=="Y":
                    exit_game()
                else:
                    game_logic()
            else:
                valid_choice_exit_game()
    else:
        valid_choice_exit_game()

def game_logic():
    objects=["rock","paper","scissor"]
    while True:
        computer_choice=random.choice(objects)
        user_guess=input("Enter Your Choice: ").lower()
        if user_guess in ["quit"]:
             quit_choice_game_exit()
        elif user_guess in objects:
                print("Computer Chose: {}".format(computer_choice))
                result_decorator()
                if user_guess==computer_choice:
                     print("Tough Competetion ! It's a Tie.")
                elif user_guess=="rock":
                     if computer_choice=="paper":
                       print("Paper covers rock! You lose.")
                     else:
                       print("Rock smashes scissor! You win.")
                elif user_guess=="paper":
                     if computer_choice=="rock":
                       print("Paper covers rock! You win.")
                     else:
                       print("Scissor cuts paper! You lose.")
                else:
                     if computer_choice=="rock":
                       print("Rock smashes scissor! You lose.")
                     else:
                       print("Scissor cuts paper! You win.")
                result_decorator()
                print()
        else:
            valid_choice_exit_game()


#Function Call To Run Game
introduction_to_game()