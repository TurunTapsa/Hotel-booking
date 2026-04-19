#Hotel booking system


#Data Storage here
#Each room is stored as a dictionary with type, price, availability, and guest name



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





