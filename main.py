import random
import functions
#Asks user to select option
def option():
    try:
        take_option = int(input("\nSelect an option[1-4]: "))
        valid = True
        if take_option < 1 or take_option > 4: #Checks if the selected option is valid
            valid = False
            print("Please choose between the provided options")
    except:
        print("Please choose between the provided options")
        valid=False
    if valid== True:    
        return take_option

exit_program = False
#Library management system
while(exit_program != True):
    list_of_book = functions.store_in_list() #Stores the information of the books in a list
    random_number = random.randint(1,99999)
    #Displays Menu
    def display():
        print("\n----Library Management System----\n")
        print("Enter 1: To display available books")
        print("Enter 2: To borrow a book")
        print("Enter 3: To return a book")
        print("Enter 4: To exit\n")
    display_option = display()
    
    selected_option = option()  #Asks the user to select an option

    #Executes the selected option

    #Displays available books
    if selected_option == 1:
        show = functions.display_books()

    #Borrow books selected by user    
    elif selected_option == 2:
        borrow_book = functions.borrow(list_of_book,random_number)
        
    #Returns book selected by user    
    elif selected_option == 3:
        returns_book = functions.returns(list_of_book,random_number)

    #Exits the program    
    elif selected_option == 4:
        exit_program = True
        exit()

