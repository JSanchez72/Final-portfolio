# Jonathan Sanchez
# 12/3/2022
# in this sytem of coding we are trying to make a code that put years to leap year and say if its true of falce
def isleapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:# in the system we are trying to solve how to guess if some years have leap year if no is falce
         if year % 400 == 0:
            return True
        else:# In this part of the code we code if the statement is correct from the year place
            return False
    else:
        return True
       # if:
    #return False
print(isleapYear(2000))#in this last part of the code we put the year and see if its true or false