#Jonathan Sanchez
#12/11/2022
# This is the start of the game that gets all the imports to continues with the game

#Remember to put all your files into the same folder on your computer!
#Otherwise, these import statements won't be able to find them properly

#Import the main character and section files here
import main_character
import section_1
import section_2
import section_3
import section_4


#Intro text to the user
#The empty input functions are only here so the player has to type something to move on
#(like pressing a button in a video game to move the dialogue along)
print("Hello there!")
print("Welcome to my game")
print("hints There is a 2/3 chances of something bad can happened when stealing jewelry!!")
print("Press enter to begging game")# in this part of the code is when the user is welcome of playing the game
input()
print("Max, one of the greatest robbers in town ready to rob a family that recently just move into town.")

#And do/say anything else to get your game started
# in the final part is when the game starts to play
#Then call your first section.
section_1.start()
