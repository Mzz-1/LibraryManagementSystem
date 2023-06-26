import datetime

#return information of books in a list
def store_in_list():
    file = open("stock.txt", "r")
    lines = file.readlines()
    book = []
    for line in lines:
        book.append(line.replace("\n","").split(","))
    return book
    file.close()
    
#Call function store_in_list()    
list_of_book = store_in_list()

#Returns the total bill amount of total fine
def return_total_amount(filename):
    file = open(filename, "r")
    lines = file.readlines()
    book = []
    for line in lines:
        book.append(line.replace("\n","").split("\t"))
    file.close()
    total=float(book[5][1].replace("$",""))
    for i in range(8,len(book)+1,3):
        amount = book[i][1].replace("$","")
        total += float(amount)
    return total
                       
#decrease stock of borrowed book
def decrease_stock(n):
    list_book = store_in_list() #call function store in list to get list of books
    file = open("stock.txt", "w")
    for i in range(len(list_book)):            
        for j in range(5):
            if j == 3 and i == n :
                a = int(list_book[i][3]) -1 #decrease the stock of book borrowed
                file.write(str(a))
                file.write(",")
            else:    
                file.write(list_book[i][j])
                if j!=4:
                    file.write(",")
        file.write("\n")
    file.close()
    
#increase stock of returned book
def increase_stock(n):
    list_book = store_in_list() #call function store in list to get list of books
    file = open("stock.txt", "w")
    for i in range(len(list_book)):            
        for j in range(5):
            if j == 3 and i == n :
                a = int(list_book[i][3]) +1 #increase stock of returned book
                file.write(str(a))
                file.write(",")
            else:    
                file.write(list_book[i][j])
                if j!=4:
                    file.write(",")
        file.write("\n")
    file.close()
    
#print available books
def display_books():
    print("\n----The available books are----\n")
    file = open("stock.txt", "r")
    print(file.read())
    file.close()
    
#Function to borrow book    
def borrow(book_num,random_number):
    name = input("Enter your full name: ")
    new_user = True 
    while True:
        try:
            num = int(input("Enter the book you want to borrow:(Enter item no) "))
            valid_check = True
        except:
            print("Enter a valid number")
            valid_check = False
        if valid_check == True and num >= 0 and num < len(list_of_book): #Checks if the selected book is available
            file = open(name+"_"+str(datetime.date.today())+"_"+str(random_number)+"_borrow.txt","a")
            for i in range(len(book_num)):
                try:
                    if i == num:
                        decrease = decrease_stock(num) # decrease stock of borrowed book
                        if new_user ==True: 
                            file.write("\nName of the borrower:\t")
                            file.write(name)
                            file.write("\nDate:\t")
                            file.write(str(datetime.datetime.now()))
                        file.write("\n---------------------------------")
                        file.write("\nBook borrowed:\t")
                        file.write(book_num[i][1])
                        print("The book you have borrowed is "+book_num[i][1])
                        file.write("\nAmount:\t")
                        file.write(book_num[i][4])
                        file.close()
                        valid = True
                except:
                    valid = False 
        elif valid_check == False:
            valid = False
        else:
            print("Please choose between the provided options.")
            valid = False
            valid_check = False
        if valid_check != False:   
            while True:
                borrow_next = input("Do you want to borrow another book(y/n)?")
                if borrow_next == "y":
                    valid = False
                    new_user = False
                    break
                elif borrow_next == "n":
                    file1 = open(name+"_"+str(datetime.date.today())+"_"+str(random_number)+"_borrow.txt","a")
                    file1.write("\n---------------------------------")
                    file1.write("\nTotal Amount:\t")
                    total_amount=return_total_amount(name+"_"+str(datetime.date.today())+"_"+str(random_number)+"_borrow.txt") # get total amount to be paid
                    file1.write("$"+str(total_amount))    
                    file1.close()
                    valid = True
                    new_user = True
                    break
                else:
                    print("Enter a valid option")
                    valid = False
                    new_user = True            
        if valid == True:
            #Display information of the book borrowed
            file = open(name+"_"+str(datetime.date.today())+"_"+str(random_number)+"_borrow.txt", "r")
            print(file.read())
            file.close()
            break
        
#Function to return book
def returns(book_num,random_num):
    name = input("Enter your full name: ")
    new_user = True
    while True:
        try:
            num = int(input("Enter the book you want to return:(Enter item no) "))
            valid_check = True
        except:
            print("Enter a valid number")
            valid_check = False
        if valid_check == True and num >= 0 and num < len(list_of_book): #Checks if the selected book is available
            while True:
                try:
                    r_day = int(input("Enter how long did you have the book(in days): "))
                    break
                except:
                    print("Enter number of days")
            file = open(name+"_"+str(datetime.date.today())+"_"+str(random_num)+"_return.txt","a")               
            for i in range(len(book_num)):
                try:
                    if i == num:
                        increase = increase_stock(num) #Increase stock of book returned 
                        if new_user ==True:
                            file.write("\nName of the borrower:\t")
                            file.write(name)
                            file.write("\nDate:\t")
                            file.write(str(datetime.datetime.now()))
                        file.write("\n---------------------------------")    
                        file.write("\nBook returned:\t")
                        file.write(book_num[i][1])
                        print("The book you have returned is "+book_num[i][1])
                        file.write("\nFine:\t") 
                        if r_day > 10: #Checks if fine is needed to be charged
                            fine = "$"+str(r_day-10)
                            file.write(fine)
                        else:
                            file.write("$0")
                        file.close()
                        valid = True
                except:
                    valid = False
        elif valid_check == False:
            valid = False
        else:
            print("Please choose between the provided options.")
            valid = False
            valid_check = False
        if valid_check != False:    
            while True:    
                return_next = input("Do you want to return another book(y/n)?")
                if return_next == "y":
                    valid = False
                    new_user = False
                    break
                elif return_next == "n":
                    file1 = open(name+"_"+str(datetime.date.today())+"_"+str(random_num)+"_return.txt","a")
                    file1.write("\n---------------------------------")
                    file1.write("\nTotal Amount:\t")
                    total_amount=return_total_amount(name+"_"+str(datetime.date.today())+"_"+str(random_num)+"_return.txt") # get total fine to be paid
                    file1.write("$"+str(total_amount))
                    file1.close()
                    new_user = True
                    valid = True
                    break
                else:
                    print("Enter a valid option")
                    valid = False
                    new_user = True
        if valid == True:
            #Display information of the book returned
            file = open(name+"_"+str(datetime.date.today())+"_"+str(random_num)+"_return.txt", "r") 
            print(file.read())
            file.close()
            break
