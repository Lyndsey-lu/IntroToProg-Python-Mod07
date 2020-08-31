# Exception Handling and Converting to Binary Data
*Lyndsey Holmes*

*08/30/2020*

## Introduction
Exception handling is a way to prevent Python from throwing errors that would end the script before intended break.  The most common need for exception handling is when a script requires user input.  If the user does not enter expected data, then Python will throw an error and end the script.  In order to prevent the script from ending, the script can have try-except functions, send an error to the user to explain why entered data failed.  Otherwise, Python will return an error that a user may not understand.  For example, if the user needs to type in a number between 1-10 and instead a letter was received by the script, the user may not be aware that they typed a letter vs number.  Python would return an error stating, str not accepted, require int or float.  Exception handling allows the user to receive a better error justification.
Pickling is a process that converts large bits of data to binary format for storage or data transfer.  It is a module add-on to Python.  It allows for converting objects to binary data for compression.

### Exception Handling
The purpose of this exception handling example is to show that when user input fails, the try-except function can catch the error before exiting the script.  For this case, the script asks a user to enter a number.  Figure 1: Exception Handling shows the code for the try-except function.  The try function checks if the user input can be converted from a string to an integer.  If this was not inside a try-except function.  Figure 2: Python Error shows the error received if the try-except function was not utilized.  As you can see from Figure 2, the error message received is “ValueError: invalid literal for int() with base 10: ‘l’. “

![Image of Exception Handling Code](https://github.com/Lyndsey-lu/images/ExceptionHandling.png)
*Figure 1: Exception Handling*

![Image of Python Error](https://github.com/Lyndsey-lu/images/PythonError.png)
*Figure 2: Python Error*

That is not a clear error to a user that may not be a developer.  As shown in Figure 3: Try-Except Set Error, the error can be set to ask the user again for a number and provide the details that explain what was entered originally and why it will not work.   This version tells the user that ‘l’ is not a number and asks for the user to try again.  Then the while loop repeats the request for the user to input number. 

![Image of Running Exception Handling code](https://github.com/Lyndsey-lu/images/RunExceptionHandling.png)
*Figure 3: Try-Except Set Error*

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
