# ------------------------------------------------- #
# Title: Assignment 07
# Description: Two examples of: pickling binary files and exception handling
# ChangeLog: (Who, When, What)
# Lyndsey Holmes,8/25/2020,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!
#import numpy as np

# Data -------------------------------------------- #
FileName = 'data_file.txt'
tuple_data = ()
lst_tuples = []

# Exception Handling
while(True):
    user_input = input("Input number any number: ")    # input function from user 
    try:
        int(user_input)     # check if input from user is integer using exception handling.  
        print("You have entered the number " + user_input)
        break               # exit program if user input is integer 
        
    except:
        print(user_input + " is not a number.  Please try again.") # error exception
    

# Pickling
is_pickle = input("Do you wish to convert to binary file ('y' or 'n'): ")
if is_pickle.lower == 'y':
    file = open(FileName, 'r')  # open file and read in to list

    for row in file.readlines():    # create a list of tuples
        temp = row.split(",")
        tuple_data = (temp[0], temp[1])
        lst_tuples.append(tuple_data)

    file.close()
    new_file = open('file.dat', 'wb')
    pickle.dump(lst_tuples, new_file)
    new_file.close()  

else:
    pass 