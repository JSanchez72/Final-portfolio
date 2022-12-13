#Jonathan Sanchez
#11/1/2022
# In this question there is a multiply actions of nubers that need to be action majority is math related
num=1
while num<=50:# in this fisrt part it is shows the number going 1 to 50 and stops
    print (num)
    num = num+1
print(3%9)# in this part i put some divition if it work to calculate it by addid numbers
print("divided by 3")
print(5%10)
print("divided by 5")# in this part of code is making the user type the numbers that is divisibel by the number
num=3
number= int(input("Give me a number that is divided by 3:\n"))
if number % 3 ==0:
    print("Your number is divisible by 3!")
else:# in this part of coding is making it divide by 3 if not it will give a responces as incorrect same with number 5
    print(" Your number is not divided by 3!")

num=5
number= int(input("Give me a number that is divided by 5 :\n"))
if number % 5 ==0:# the percentage means the divition that is being calculated.
    print("Your number is divisible by 5")
else:
    print(" Your number is not divided by 5")

num=3,5 # in this part of the code is divided by 3 and 5 and the system is calculating if the number is divided by both numbers that is 3 and 5
number= int(input("Give me a number that is divided by 3 and 5 :\n"))
if number %3/5 ==0:
    print("Your number is divisible by 3/5")
else:
    print(" Your number is not divided by 3/5")
# at the end it will give you option if the user got it wrong or right.


