# jonathan Sanchez
# 11/6/22
# in this part of code the main character will get in the fourth part of the game and has to escape


import main_character



# This will control the whole section.
# It'll need the player character as an input in order to interact with them.
def start():

    print(# in this part there are details of were is the main character
        "4))Max is on the first floor and is still dark trying to escape and steel items from the house.: !")

    print(
        "Max is on the first floor, and he is trying to find keys to escape from the front door and steel to make money from the stolen items. “His head is starting to hurt and got a small flash back but does not know what it means.")
    print("What is Max next step to escape?")# this part of the code will be the same for the next steps
    choice = int(input(
        "1. steal items from the second first 2.used flashlight to find keys at the kitchen 3.go to the front door check under the rug inside the house  4.Got all the keys leave house and escape with stolen items."))
#in this part there are the question that the gamer choses to do to play the level
    if choice == 1:
        print(" steal items from the first floor.")
        #choice = input("o you want to take items Y ")
        choice = input(" Max made a lot of noice GAME OVER")
        exit()

        # You keep the items at the end of the game
        # try to get out of the second floor
    elif choice == 2:
        print("Used the flashlight to find the keys at the kitchen .")
        # character is in the hallway of the house and found keys
        print("there was keys in the hallway")

    if choice == 'go to the front door check under the rug inside the house ':
              # in this part of the code there is no effect of going in the empty room so i am making the charater to go back the main room/hallway
        print("there was keys in the rug")

        if choice == 'Got all the keys leave house and escape with stolen items ':
            import main.game1.py
            # In this part the main charter found all the key and escape the house with the jewerly


    # In the end of the code I put the comments of the back story of what happend in the end with the main character
    print("main game")
    #import main.game1.py
    #In this code there is no need to add or take information about the coding part.
    print("He saw a family portrait and he saw himself in it with his family. ")
    print("At the end of the game Max remembers everything the house that he robed is his house the bone from the attic is his family the death from him is from killing himself he was delusional).    ")
# the end of the game
# the last part it a type of aoutro of the game.
#import turtle
#turtle.bgcolor("black")
#squary = turtle.Turtle()

#I was thinking of using this part of code from the start of the game like a trasition from the menue to the game

#squary.speed(1000)
#squary.pencolor("red")
#for n in range(4000):

#I learn this part in python readings and other resources

    #squary.forward(n)
    #squary.left(71)
#input()


