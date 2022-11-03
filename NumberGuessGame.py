import time
import random
import sys

def playerDetail():
    player_name=input("Enter Your Name:   ")
    return player_name

def greetingsOfDay():
         struct_type=time.localtime()
         hour=int(time.strftime("%H",struct_type))
         if hour>=0 and hour<12:
             return "Good Morning"
         elif hour>=12 and hour<17:
             return "Good Afternoon"
         elif hour>=17 and hour<20:
             return "Good Evening"
         else:
             return "Good Night"
def introductionToGame():
    input("{}, {}. Welcome To The Number Guess Game: ".format(greetingsOfDay(),playerDetail())+"[Press Any Key To Continue Game]  ")
    print("\nLet's take a look at the rules to play this Game: ")
    print("\n1.  You have given a choice to choose a given numbers range.")
    print("2.  A Number is picked by game randomly from given number's range.")
    print("3.  You have given 4,7,11 number of chances according to difficulty Mode of Game i.e For most difficult Mode you get more chances. ")
    print("4.  You have to Guess the number selected by Game Correctly.\n")
    game_began_choice=input("So Let\'s began with the Game [Y/N]:   ")
    print()
    if game_began_choice=="Y":
        print()
    elif game_began_choice=="N":
        Quit_game_choice=input("Do you want to Quit Game[Y/N]:  ")
        if Quit_game_choice=="Y":
            print("\n-------Game Ended-------")
            sys.exit()

def Game_Mode_Choice():
    print("\nPick a Level: \n")
    print("Easy: \n","1. Between 1 and 10 ","2. Between 1 and 100 ","3. Between -1000 and 1000 \n",sep="\n")
    print("Hard: \n", "4. Between 1 and 10 ", "5. Between 1 and 100 ", "6. Between -1000 and 1000\n ", sep="\n")
    user_level_choice=input("Enter Level Number: ")
    print()
    if user_level_choice.isdigit():
        user_level_choice=int(user_level_choice)
    else:
        print("Please Enter a Valid Number Choice Next Time !")
        print("\n-------Game Ended-------")
        sys.exit()
    match user_level_choice:
        case 1:
                 (lower_limit,upper_limit,chances,Mode)=(1,10,5,"easy")
        case 2:
                 (lower_limit, upper_limit, chances, Mode) = (1,100,7,"easy")
        case 3:
                 (lower_limit, upper_limit, chances, Mode) = (-1000,1000,11,"easy")
        case 4:
                 (lower_limit, upper_limit, chances, Mode) = (1, 10, 5, "hard")
        case 5:
                 (lower_limit,upper_limit,chances,Mode)=(1,100,7,"hard")
        case 6:
                 (lower_limit,upper_limit,chances,Mode)=(-1000,1000,11,"hard")
        case _:
            print("\nPlease Enter a Valid Choice Number Next Time !")
            sys.exit()
    return (lower_limit,upper_limit,chances,Mode)

def random_number_generator(lower_limit,upper_limit):
    random_number=random.randint(lower_limit,upper_limit)
    return random_number
def input_decorator():
    for _ in range(40):
        print("-",end="")
    print()

def game_execution():
    introductionToGame()
    (lower_limit,upper_limit,chances,Mode)=Game_Mode_Choice()
    random_number = random_number_generator(lower_limit, upper_limit)
    guess_list,first_try = [],chances
    while chances:
        if Mode=="easy" and chances!=first_try:
            print("\nYour Previous choice :  ",guess_list)
        chances -= 1
        input_decorator()
        user_input_number=input("Pick a Number Between {} and {} :  ".format(lower_limit,upper_limit))
        input_decorator()
        if user_input_number.isdigit():
             user_input_number=int(user_input_number)
             guess_list.append(user_input_number)
        else:
            print("Please Enter a Valid Number Next Time!")
            continue
        if user_input_number == random_number:
            print("---------------------------------------- You got it, Right! ----------------------------------------")
            break
        elif user_input_number > random_number:
            print("Your guess {} is Too High!".format(user_input_number))
        else:
            print("Your Guess {} is Too Low!".format(user_input_number))
        print("--->  You have {} chances Left\n".format(chances))
    else:
        print("----------------------------------------- You Lose the Game!, No Chance Left ----------------------------------------")

game_execution()