# Exception Handling and Converting to Binary Data
*Lyndsey Holmes*

*08/30/2020*

## Introduction
Exception handling is a way to prevent Python from throwing errors that would end the script before intended break.  The most common need for exception handling is when a script requires user input.  If the user does not enter expected data, then Python will throw an error and end the script.  In order to prevent the script from ending, the script can have try-except functions, send an error to the user to explain why entered data failed.  Otherwise, Python will return an error that a user may not understand.  For example, if the user needs to type in a number between 1-10 and instead a letter was received by the script, the user may not be aware that they typed a letter vs number.  Python would return an error stating, str not accepted, require int or float.  Exception handling allows the user to receive a better error justification.
Pickling is a process that converts large bits of data to binary format for storage or data transfer.  It is a module add-on to Python.  It allows for converting objects to binary data for compression.

### Exception Handling
The purpose of this exception handling example is to show that when user input fails, the try-except function can catch the error before exiting the script.  For this case, the script asks a user to enter a number.  Figure 1: Exception Handling shows the code for the try-except function.  The try function checks if the user input can be converted from a string to an integer.  If this was not inside a try-except function.  Figure 2: Python Error shows the error received if the try-except function was not utilized.  As you can see from Figure 2, the error message received is “ValueError: invalid literal for int() with base 10: ‘l’. “

![ExceptionHandling](https://user-images.githubusercontent.com/59658526/91678111-7b067b00-eaf9-11ea-8511-e95b466e29b2.png)
*Figure 1: Exception Handling*

![PythonError](https://user-images.githubusercontent.com/59658526/91678139-95405900-eaf9-11ea-97d3-540133643b5c.png)
*Figure 2: Python Error*

That is not a clear error to a user that may not be a developer.  As shown in Figure 3: Try-Except Set Error, the error can be set to ask the user again for a number and provide the details that explain what was entered originally and why it will not work.   This version tells the user that ‘l’ is not a number and asks for the user to try again.  Then the while loop repeats the request for the user to input number. 

![exceptionError](https://user-images.githubusercontent.com/59658526/91678174-af7a3700-eaf9-11ea-92de-4e57532ab3e9.png)
*Figure 3: Try-Except Set Error*

### Pickle Module
The pickle module allows for data to be compressed into binary data.  This can be used to transfer data quickly.  “Python pickle module is used for serializing and de-serializing a Python object structure.” (“Geeks for Geeks”, Resource 1, URL).  Another format that is often used is the JSON module.  For this case the pickle method was used.  As seen in Figure 4: Import Pickle, a file was created with data delimited by a comma.  The file is opened, and the data is read into a list of tuples separated by commas.  Then the pickle method is called to compress the data into a binary file.  Since the files are opened, they must be closed.  

![Pickle](https://user-images.githubusercontent.com/59658526/91680019-cbcca280-eafe-11ea-9137-924a2e75d1f6.png)
*Figure 4: Import Pickle*

#### Running Pickle
As shown in figure 5: Running Pickle, not much appears on the command shell.  Just a question if the user would like to convert to binary file.  Figure 6: .DAT file, shows the work done in the pickle process.  The data is now only machine readable, but the data is still included and available after the file is unpickled.

![RunningPickle](https://user-images.githubusercontent.com/59658526/91680039-db4beb80-eafe-11ea-8134-6e19dad6249e.png)
*Figure 5: Running Pickle*

![datfile](https://user-images.githubusercontent.com/59658526/91680048-e43cbd00-eafe-11ea-9e1d-44ad2ad4e64e.png)
*Figure 6: .DAT file*

## Summary
In summary, exception handling is a way to prevent a script from ending too soon due to user error.  The error messages can be more clear to a user that possibly did not fully understand the script’s expectation.  
There are many different modules that can be added on to the Python package.  Pickle is a way to store large objects of data into binary files.  Those files can be transmitted more easily than a large file of data in English. 

### Resources

1.	“Geeks for Geeks” 
https://www.geeksforgeeks.org/understanding-python-pickling-example/#:~:text=Python%20pickle%20module%20is%20used,serializing%20a%20Python%20object%20structure.&text=Pickling%20is%20a%20way%20to,object%20in%20another%20python%20script.
2.	Python Documentation
https://docs.python.org/3/library/pickle.html

### Code

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
