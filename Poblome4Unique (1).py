# Jonathan Sanchez
# 11/20/22
# In this part of codding we are making a code that make up numbers but in different type of patterns in the coding
list=[1,1,1,2,3,3,4,4,4,5,5,6]
my_list=[]# in the beggining of the coding I added the number that are scambel
for n in list:
  if n not in  my_list:# in this part of the work not in work with the sequence of numbers that turn in to one formal number
   my_list.append(n)
# at the end there is a sequence that prints out the code to be in one single line
print(my_list)