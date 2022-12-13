# jonathan Sanchez
# 11/6/22
# in this part of code the main character will get in the third part of the game and has to escape

# import main_character and section_2 here
import main_character
import section_4


# This will control the whole section.
# It'll need the player character as an input in order to interact with them.
def start():
    print(
        "3))Max is on the second floor and is still dark trying to escape and steel items from the house.: !")

    print(
        " Max, is on the second floor, and he is trying to find keys to escape from the front door and steel to make money from the stolen items. .")
    print("What is Max next step to escape?")# this part of the code will be the same for the next steps
    game = True
    choice = int(input(
        "1. steal items from the second floor 2.Used the flashlight to find the keys from the hallway   3.Open another empty room and stare out in the lake and see a foggy dark night 4.go and open the door to the first main floor.5.take out of your pocket an empty bottle of pills (no affect) "))
#in this part there are the question that the gamer choses to do to play the level
    if choice == 1:
        print(" steal items from the second floor.")
        #choice = input("o you want to take items ")
        choice = input(" Max made a lot of noice while stealing GAME OVER")
        exit()
        # You keep the items at the end of the game
        # try to get out of the second floor
    elif choice == 2:
        print("Used the flashlight to find the keys from the hallway .")
        # character is in the hallway of the house and found keys
        print("there was keys in the hallway")

    if choice == 'Open another empty room and stare out in the lake and see a foggy dark night “go back to the hallway':
              # in this part of the code there is no effect of going in the empty room so i am making the charater to go back the main room/hallway
        print(go_to_mainhall)
        if choice == 'go and open the door to the first main floor ':
            print()

            # In this part of the code the character did found a key
        if choice ==5:
            print("take out of your pocket an empty bottle of pills ")
            print(no_affect)

    # One of the options should move the story to the next section with code like this:
    section_4.start()


    #In this code there is no need to add or take information about the coding part.