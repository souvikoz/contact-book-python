import os

print("Python is running this file:")
print(os.path.abspath(__file__))
print("Contacts file Python will use:")
print(os.path.abspath("contacts.txt"))


while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    print("==================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        file = open("contacts.txt", "a")

        file.write("Name: " + name + "\n")
        file.write("Phone: " + phone + "\n")
        file.write("Email: " + email + "\n")
        file.write("-------------------------\n")

        file.close()

        print("Contact added successfully!")

    elif choice == "2":
        file = open("contacts.txt", "r")

        data = file.read()

        file.close()

        print("\n========== SAVED CONTACTS ==========")
        print(data)

    elif choice == "3":
        print("Search option")

    elif choice == "4":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice.")