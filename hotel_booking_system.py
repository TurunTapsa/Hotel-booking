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





#Check out a customer here






#Remove a room here






#Main menu





