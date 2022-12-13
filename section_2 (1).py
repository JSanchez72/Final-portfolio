# jonathan Sanchez
 # 11/6/22
# in this part of code the main character will get in the second part of the game and has to escape

# import main_character and section_2 here
import main_character
import section_3



# This will control the whole section.
# It'll need the player character as an input in order to interact with them.
def start():
    print(
        ":2))Max is on the third floor, and it is dark trying to escape will be a challenge with a crazy family sleeping in their beds. !")

    print(# this part of the story give info at what floor the user is at at what options is given to him
        " Max is on the third floor, and he is trying to find keys to escape from the front door and steel to make money from the stolen items. .")
    print("What is Max next step to escape?")# this part of the code will be the same for the next steps
    choice = int(input(
        "1. steal items from the third floor 2.find the keys from the third floor 3. open one of the empty rooms and stare out the window  4.Open the door to the second floor"))

    if choice == 1:
        print(" steal items from the third floor.")
        choice = input(" Max made a lot of noice and woke up the family GAME OVER")
        exit()
        # in this part of story max made a lot of noise and the family woke up
        # You keep the items at the end of the game
        # try to get out of the third floor
    elif choice == 2:
        print("find the keys from the third floor.")
        # character is in the hallway of the house
        print("there was no keys in the hallway")

    elif choice == 'open one of the empty rooms and stare out the window': # not sure why there is no stoping
        # in this section the character found keys for the front door
        print(found_keys)

        if choice == 'Open the door to the second floor':# IDK why there is a bug or I think I am missing something
            print()
            # In this part of the code the character did found a key
    # Give the player some options of things to do here.
    # Be sure to put their choice in a variable!

    # One of the options should move the story to the next section with code like this:
    section_3.start()

   # this when the next chapter beggins
# there is nothing extra to add in this part