contacts = () 
print(contacts)

while True:
    print("\nContact Book Menu: ")
    print("1. add contact? ")
    print("2. remove contact? ")
    print("3. view contact? ")
    print("4. exit")

    choice = input("choose options 1-4: ")

    if choice == "1":
        contact = input("enter contact name and number: ")
        contacts.append(contact)

    elif choice == "2":
        if not contacts:
            print("No contacts to remove.")
        else:
            contact_number = int(input("enter contact number to remove: "))
            if 0 < contact_number <= len(contacts): 
                del contacts[contact_number - 1]
            else:
                print("wrong contact number.")

    elif choice == '3':
        if not contacts:
            print("No contacts available.")
        else:
            print("Current contacts:")
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact}")
    elif choice == "4":
        break

    else:
        print("type a proper option and try again")
