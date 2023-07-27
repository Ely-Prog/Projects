from secrets import compare_digest 
import password_gen_vault





#method to view vault.
def vault(): 
    print("vault option")


#method to create passwords
def create(): 
    print("Create Option\n\nWelcome to the password creation. A stong password will now be created within a specified character limit.")
    
    charlim = input("Please enter in a character limit: \n\nCharacter Limit: ")


    
#Just incase you change your mind 
def quitprogram(): 
    exit()

# Variable which will help to reference the index of the dictionary which contains the methods 
var: int = 3
#dictionary varibale which contains the methods above.
initref = {
           1:create,
           2:vault,
           3:quit
           }







#A while true loop is set so we can reitterate the proccess of user input if the desired input is not enetered
init = True

while init:
    print("welcome to password vault. \nHere, you can view stored passwords, or create new, strong ones. \nWhat would you like to do? (Enter 1 or 2) \n\n1. Create New password \n2. View password vault\n3. Exit Program\n\n")
    

    #Taking the input in from the user 
    var = int(input("Selection: "))
    # running an if statement to reference the inputs to the dictionary. 
    if var <= 2:
        init = False
        #starting the input acquisition.
        call = initref.get(var, quit)
        call()

    elif var == 3: 
        #escape option 
        print("Exiting Program. ")
        quitprogram()

    else:
        print("invalid option, please select one of the following options\n\n")
        continue
   

