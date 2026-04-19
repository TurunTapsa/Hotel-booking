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

#Formatting helper -> prints a line of dashes to separate sections in the console
def print_line():
    print("-" * 40)


# Add a room function here
def add_room():
    print_line()
    print("ADD A NEW ROOM")

    number_input = input("Room number: ").strip()
    if not number_input.isdigit():
        print("Invalid input. Room number must be a number.")
        return
    number = int(number_input)

    if number in rooms:
        print(f"Room {number} already exists.")
        return

    room_type = input("Room type (single / double / suite): ").strip().lower()
    if room_type not in ("single", "double", "suite"):
        print("Unknown room type. Use: single, double, or suite.")
        return

    price_input = input("Price per night (euros): ").strip()
    if not price_input.isdigit():
        print("Invalid price. Please enter a whole number.")
        return
    price = int(price_input)

    rooms[number] = {"type": room_type, "price": price, "available": True, "guest": None}
    print(f"Room {number} added successfully!")



#View available rooms here
def view_available_rooms():
    print_line()
    print("AVAILABLE ROOMS")
    found = False
    for number, room in rooms.items():
        if room["available"]:
            print(f"  Room {number} | {room['type']:6} | {room['price']} euros/night")
            found = True
    if not found:
        print("  No rooms available at the moment.")



#Book a room here
def book_room():
    print_line()
    print("BOOK A ROOM")
    view_available_rooms()

    number_input = input("Enter room number to book: ").strip()
    if not number_input.isdigit():
        print("Invalid input. Room number must be a number.")
        return
    number = int(number_input)

    if number not in rooms:
        print(f"Room {number} does not exist.")
        return

    if not rooms[number]["available"]:
        print(f"Room {number} is already booked by {rooms[number]['guest']}.")
        return

    guest = input("Guest name: ").strip()
    if guest == "":
        print("Guest name cannot be empty.")
        return

    rooms[number]["available"] = False
    rooms[number]["guest"] = guest
    print(f"Room {number} booked successfully for {guest}!")




#Check out a customer here
def checkout():
    print_line()
    print("CHECK OUT")

    print("Occupied rooms:")
    found = False
    for number, room in rooms.items():
        if not room["available"]:
            print(f"  Room {number} | {room['type']:6} | Guest: {room['guest']}")
            found = True
    if not found:
        print("  No rooms are currently occupied.")
        return

    number_input = input("Enter room number to check out: ").strip()
    if not number_input.isdigit():
        print("Invalid input. Room number must be a number.")
        return
    number = int(number_input)

    if number not in rooms:
        print(f"Room {number} does not exist.")
        return

    if rooms[number]["available"]:
        print(f"Room {number} is already free.")
        return

    guest = rooms[number]["guest"]
    rooms[number]["available"] = True
    rooms[number]["guest"] = None
    print(f"Guest '{guest}' checked out from room {number}. Room is now free.")






#Remove a room here
def remove_room():
    print_line()
    print("REMOVE A ROOM")
    print("All rooms:")
    for number, room in rooms.items():
        if room["available"]:
            status = "free"
        else:
            status = f"booked - {room['guest']}"
        print(f"  Room {number} | {room['type']:6} | {status}")

    number_input = input("Enter room number to remove: ").strip()
    if not number_input.isdigit():
        print("Invalid input. Room number must be a number.")
        return
    number = int(number_input)

    if number not in rooms:
        print(f"Room {number} does not exist.")
        return

    if not rooms[number]["available"]:
        confirm = input(f"Room {number} is occupied by {rooms[number]['guest']}. Remove anyway? (yes/no): ")
        if confirm.lower() != "yes":
            print("Removal cancelled.")
            return

    del rooms[number]
    print(f"Room {number} removed successfully.")





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




