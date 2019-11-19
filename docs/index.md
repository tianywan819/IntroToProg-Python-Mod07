# Home Inventory
*Tianyi Wang*  
*Nov 19, 2019*  
*Assignment 07*  
*Home inventory*  
## Introduction
This assignment is to create a simple script to demonstrate how Pickling and Structured error handling work. This simple script creates an interaction for the users to add data and display the data back to the user. 
## Pickling
Pickle function is used to sterilize and de-serialize an object structure in python. This function allows the user to write and save data into the file first and then pickle what is saved on disk.  In order to use the Pickle Function, I need to have the command “import pickle” to import through, shown in Figure 1. Some pre-defined data is also shown under Data Section in the script. 
![import pickle](https://github.com/tianywan819/IntroToProg-Python-Mod07/blob/master/docs/Screen%20Shot%202019-11-18%20at%202.22.41%20PM.png "Import command")
##### Figure 1. Import Pickle
In this script, I used pickle.dump and pickle.load functions to save and retrieve data from disk, shown in Figure 2.
![define data](https://github.com/tianywan819/IntroToProg-Python-Mod07/blob/master/docs/Screen%20Shot%202019-11-18%20at%202.22.54%20PM.png "Define Data")
#### Figure 2. define Pickle functions to save and get data
## Structured Error Handling
Structured error handling is included under the define function. In the script, ID only allows integers so that I added ValueError message in there and for the household item, numbers are not allowed in this case and if the user entered a number, a customized error message would pop up too shown in Figure 2.
## Presentation
In this section, the user would have the opportunity to choose between three options that would allow the user to write and save data, read current data and exit out. For each option, I can just call the Pickle function I created before to save and read data. 
![presentation](https://github.com/tianywan819/IntroToProg-Python-Mod07/blob/master/docs/Screen%20Shot%202019-11-18%20at%202.23.02%20PM.png "Presentation")
#### Figure 3. Presentation
