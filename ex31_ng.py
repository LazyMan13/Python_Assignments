print("""You enter a room and approach
a machine with a microphone.
You speak a single question into the machine.
1. What is the meaning of life?
2. What is your favorite color?
3. Who is the fairest of them all?""")

machine = input("> ")

if machine == "1":
    print("The machine asks you what do you think it is?")
    print("1. 42")
    print("2. Happiness")
    print("3. Legacy")

    life = input("> ")

    if life == "1":
        print("Ever notice what the ACSII code for 42 is?")
    elif life == "2":
        print("Happiness is good to have, but you will never know")
        print("it without it's other side. There must always be")
        print("a balance.")
    elif life == "3":
        print("Legacy is great to have for the short term,")
        print("however in the long term, many details will be forgotten")
        print("until eventually the legacy will fade away.")
        print("Life is not going to care about the achievements you leave behind.")
    else:
        print("You start to mumble and the machine gets impatient.")
        print("The machine fills the room with toxic gas to which you")
        print("cannot escape from. Better luck next time.")

elif machine == "2":
    print("The machine asks you to name your favorite first.")
    print("1. Black")
    print("2. Blue, no Yellow")
    print("3. White")

    color = input("> ")

    if color == "1":
        print("Just like the endless void.")
        print("The machine teleports you into the darkness of space.")
        print("You worry about death since you are not in a space suit,")
        print("but you soon learn of a worse fate.")
        print("The absence of light where you should see stars indicates")
        print("that you are now entering a black hole.")
        print("BAD END")
    elif color == "2":
        print("You are catapulted off the Bridge of Death... ")
        print("Where did this even come from!!!.....")
    elif color == "3":
        print("White is a fine color, perhaps when you wake from your dream")
        print("you will see more of it.")
        print("At this point you do not understand the words of the strange machine")
        print("as you sit in the corner of your padded room.")
    else:
        print("I grow weary of people just saying whatever they want to me.")
        print("And in a flash, everything was ended. It happened so quick")
        print("that nobody could realize the end of the world.")

elif machine == "3":
    print("I'm not a magic mirror you idiot.")
    print("The machine shocks you into a coma.")
    print("Now you may dream of your fantasy world.")

else:
    print("You slip and fall head first into the machine.")
    print("Bad luck works again, the blunt force instantly")
    print("kills you. Better luck next time.")
