# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file and using Pickling and Structured Error Handling
# ChangeLog: (Who, When, What)
# T.Wang, 17 Nov 2019, Created Script
# <YourName>,<1.1.2030>,Created Script
# ------------------------------------------------- #

import pickle  # This imports code from another code file!

# Data--------------------------------------------- #
strFileName = 'HomeInventory.dat'
lstCustomer = []

# Processing--------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    while (True):
        try:
            intID = int(input("Enter an ID: "))
        except ValueError as e:
            print("Not a valid integer. Please Enter again.")
            print("Built-in python error info:")
            print(e, e.__doc__, type(e), sep='\n')
        try:
            strName = str(input("Enter a household item: "))
            if strName.isnumeric():
                raise Exception('Not a valid entry, need to be an item name')
            break
        except Exception as e:
            print("Built-in python error info:")
            print(e, e.__doc__, type(e), sep='\n')
    lstCustomer = [intID, strName]
    objFile = open(file_name, "wb")  # Now we store the data with the pickle.dump method
    pickle.dump(lstCustomer, objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    list_of_data = pickle.load(objFile)
    objFile.close()
    return (list_of_data)

# Presentation------------------------------------ #
while (True):
    print("""    
    Menu of Options    
    1) Add and Save Data to File    
    2) Show Current Data    
    3) Exit Program    
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 3] - "))
    print()  # adding a new line for look

    if (strChoice.strip() == '1'):
        save_data_to_file(strFileName, lstCustomer)
        print("Data Saved!")
    elif (strChoice.strip() == '2'):
        print(read_data_from_file(strFileName))
    elif (strChoice.strip() == '3'):
        print('Exit!')
        break
