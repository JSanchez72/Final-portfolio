#jonathan Sanchez
#11/6/22
# in this part of code the main character will get in to the first sectrion of the story and will have options to do in the story

#import main_character and section_2 here
import main_character
import section_2

#This start function is called by main_game.
#This will control the whole section.
#It'll need the player character as an input in order to interact with them.
def start():
    print("1)) Max got in the house from the attic, but his ladder accidently fell of the ceiling and can not escape the home from the attic anymore his goal is to rob the family and leave the home using the front or back door. But when Max notice pile of bones in the attic Max knew that this family is not normal The Objective: escape the home without making any noise. !")

    print("It was a dark night, a mansion to steel items from the family that moved into town. The Back door is blocked the only way is by the front door but it has 3 different lock so find three different keys to escape. .")
    print("What is Max next step to escape?")
    choice = int(input("1. Steal box of watches and Jewerly 2.Jump of the attic and break your legs 3. Open the attic door and go to the third floor 4.Find a flashlight and keys for the front door"))
# Keys for the front door not fount in the attic find a variable that calculate the keys.
    if choice == 1:# in this part it give options to the user to choose what to do in the story
        print("Steal box of watches and Jewerly.")
        choice = input(" Found some valiable to steel and put in inventory")
        if choice == 'dA':# every code is being copy but difrent story of outcome
            print("Y")
        # You keep the items at the end of the game
        # try to get out of the attic
    elif choice == 2:
        print("Jump of the attic and break your legs.")
        choice = input(" Max broke his leg and died from blood loss GAME OVER")
        exit()
        # Let the character decided to jump or not

        if choice == 'do you want to jump of the roof Y/N':# in this part the user have to decides to jump from the atict
            #choice = input(" Max made a lot of noice game over")
            #exit()
            print(Y)# the player jumps and the game ends
            print (N) # the player will still be in the attic and going down a level.
    if choice== 'Open the attic door and go to the third floor':
        print(section_2.py)
        # in this section the character go to the next section of the house
        if choice=='Find a flashlight and keys for the front door':
            print(found_flashlight)
            # In this part of the code the character did not find a key
    #Give the player some options of things to do here.
    #Be sure to put their choice in a variable!
    
    #Then use an if/elif/else statement to do something based on the player's choice.
    
    #One of the options should move the story to the next section with code like this:
    section_2.start()# in this part of the code is when its starts
    #import section_2

# there is nothing extra to add in this part
