room_a = input("Is Room A dirty? (y/n): ").lower() == "y"
room_b = input("Is Room B dirty? (y/n): ").lower() == "y"

current_room = "A"

while room_a or room_b:
    if current_room == "A":
        if room_a:
            print("Cleaning Room A")
            room_a = False
        else:
            print("Room A is clean, moving to Room B")
            current_room = "B"
    else:
        if room_b:
            print("Cleaning Room B")
            room_b = False
        else:
            print("Room B is clean, moving to Room A")
            current_room = "A"

print("Both rooms are clean!")
