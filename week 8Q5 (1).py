# Jonathan Sanchez
# 12/3/2022
# In this last part of the work we are making a formula that make a charactor actions in a type of inventory haves.
class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):# in this part of the code is when there are  the difrent type of work that shows of the items and more

        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses


player1 = character('', '', '')# Shows the character type inventory
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:# in this code it shows the weapons and weaknesses from the player
    print("Debuff: ", debuff)

def task1(player1):
    if 'rope' in player1.weapons and 'coat' in player1.weapons and 'fisrt aid kit' in player1.weaknesses:
        return True
    else:
        return False
def task2(player):
    if 'pan' in player.weapons and 'groceries' in player.weapons and 'small' not in player.weaknesses:
        return True
    else:# From the 3 playes there are difreent type of
        return False
def task3(player):
    if 'ideas'in player1.weapons and 'paper' in player1.weapons and 'pen' in player1.weapons and 'confusion' not in player1.weaknesses:
        return True
    else:
        return False
print(task1(player1))
print(task2(player1))
print(task3(player1))
