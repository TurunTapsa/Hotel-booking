#Hotel booking system


#Data Storage here
#Each room is stored as a dictionary with type, price, availability, and guest name



# Add a room function here



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





