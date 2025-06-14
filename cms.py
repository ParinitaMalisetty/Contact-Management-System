import sys

def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")), 5
    phone_book = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[j].strip() == '':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            if j == 1:
                temp.append(int(input("Enter number*: ")))
            if j == 2:
                email = str(input("Enter e-mail address: "))
                temp.append(email if email.strip() else None)
            if j == 3:
                dob = str(input("Enter date of birth(dd/mm/yy): "))
                temp.append(dob if dob.strip() else None)
            if j == 4:
                category = str(input("Enter category(Family/Friends/Work/Others): "))
                temp.append(category if category.strip() else None)
        phone_book.append(temp)
    return phone_book

def menu():
    print("******************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY")
    print("******************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    return int(input("Please enter your choice: "))

def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        elif i == 1:
            dip.append(int(input("Enter number: ")))
        elif i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        elif i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        elif i == 4:
            dip.append(str(input("Enter category(Family/Friends/Work/Others): ")))
    pb.append(dip)
    return pb

def remove_existing(pb):
    query = str(input("Please enter the name of the contact you wish to remove: "))
    for i in range(len(pb)):
        if query == pb[i][0]:
            print(pb.pop(i))
            print("This query has now been removed")
            return pb
    print("Sorry, you have entered an invalid query. Please recheck and try again later.")
    return pb

def delete_all(pb):
    pb.clear()
    return pb

def search_existing(pb):
    choice = int(input("Enter search criteria\n\n1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\nPlease enter: "))
    temp = []
    check = -1
    if choice == 1:
        query = str(input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    elif choice == 2:
        query = int(input("Please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
    elif choice == 3:
        query = str(input("Please enter the e-mail ID of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
    elif choice == 4:
        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY) of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
    elif choice == 5:
        query = str(input("Please enter the category of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check = i
                temp.append(pb[i])
    else:
        print("Invalid search criteria")
        return -1

    if check == -1:
        return -1
    else:
        display_all(temp)
        return check

def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])

def thanks():
    print("******************************************************")
    print("Thank you for using our Smartphone directory system.")
    print("Please visit again!")
    print("******************************************************")
    sys.exit("Goodbye, have a nice day ahead!")

print("..................................................................")
print("Hello dear user, welcome to our smartphone directory system")
print("You may now proceed to explore this directory")
print("..................................................................")

ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        display_all(pb)
    else:
        thanks()
