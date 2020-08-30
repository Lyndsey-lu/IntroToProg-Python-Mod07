# Exception Handling and Converting to Binary Data
*Lyndsey Holmes*

*08/30/2020*

## Introduction
Exception handling is a way to prevent Python from throwing errors that would end the script before intended break.  The most common need for exception handling is when a script requires user input.  If the user does not enter expected data, then Python will throw an error and end the script.  In order to prevent the script from ending, the script can have try-except functions, send an error to the user to explain why entered data failed.  Otherwise, Python will return an error that a user may not understand.  For example, if the user needs to type in a number between 1-10 and instead a letter was received by the script, the user may not be aware that they typed a letter vs number.  Python would return an error stating, str not accepted, require int or float.  Exception handling allows the user to receive a better error justification.
Pickling is a process that converts large bits of data to binary format for storage or data transfer.  It is a module add-on to Python.  It allows for converting objects to binary data for compression.

### Explanation of Exception Handling

### Explanation of Pickling Script


    # ------------------------------------------------- #
    Title: Assignment 07
    Description: Two examples of: pickling binary files and exception handling
    ChangeLog: (Who, When, What)
    Lyndsey Holmes,8/25/2020,Created Script
    # ------------------------------------------------- #
    import pickle  # This imports code from another code file!
    
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
