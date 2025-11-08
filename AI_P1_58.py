def smart_light_agent():
    print("Smart Light Control System")
    outside = input("Is there outside light? (yes/no): ").lower()
    human = input("Is a human present in the room? (yes/no): ").lower()

    if human == "yes" and outside == "no":
        print("Light ON")
    else:
        print("Light OFF")

smart_light_agent()
