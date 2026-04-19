#Hotel booking system


#Data Storage here
#Each room is stored as a dictionary with room type, price, availability, and guest name
rooms = {
    101: {"type": "single",  "price": 60,  "available": True, "guest": None},
    102: {"type": "single",  "price": 60,  "available": True, "guest": None},
    103: {"type": "double",  "price": 90,  "available": True, "guest": None},
    104: {"type": "double",  "price": 90,  "available": True, "guest": None},
    105: {"type": "suite",   "price": 150, "available": True, "guest": None},
}


# Add a room function here



#View available rooms here




#Book a room here





#Check out a customer here






#Remove a room here






#Main menu
# This function prints the main menu options for the hotel booking system
def print_menu():       
    print_line()
    print("  HOTEL BOOKING SYSTEM")
    print_line()
    print("  1. Add a room")
    print("  2. View available rooms")
    print("  3. Book a room")
    print("  4. Check out a guest")
    print("  5. Remove a room")
    print("  6. Quit")
    print_line()

# This function prints a line of dashes for formatting purposes
def main():

    print("Welcome to the Hotel Booking System!")
    
# The main loop of the program that displays the menu and processes user input
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_room()
        elif choice == "2":
            view_available_rooms()
        elif choice == "3":
            book_room()
        elif choice == "4":
            checkout()
        elif choice == "5":
            remove_room()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")




