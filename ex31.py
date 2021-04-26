print("""You enter a dark room with three doors.
Do you go through door #1, door #2, or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear comments on your rudeness and procedes to chase after you.")
        print("You see a path on the left and a path on the right.")
        print("Which will you take? 1. Left -or- 2. Right")

        path = input("> ")

        if path == "1":
            print("Left is never right. You fall into a pit and die.")
        elif path == "2":
            print("Right path it is. You would usually feel good about your choice")
            print("if it wasn't for the dead end. You heard the bear now, it's only a")
            print("matter of time.... The bear eats your face. Good job!")
        else:
            print("Not knowing what path to take, you stop at the fork.")
            print("Bad idea. You don't see the man-eating plant above you.")
            print("Better luck next time.")

    elif bear == "2":
        print("The bear eats you legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Meeting the ancient one.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    elif insanity == "3":
        print("You have finally met the Ancient One.")
        print("You slam to the ground on your knees and shout \"All Hail our Lord Cthulhu!\"")
        print("Not knowing what happened next your conscious is now in and endless void")
        print("as Cthulhu has selected a new avatar to roam the Earth.")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You open the door and see a large mirror.")
    print("You start to see an image. What do you see?")
    print("1. A young boy reading a book in an attic.")
    print("2. The personification of the mirror itself.")
    print("3. Yourself but different... somehow...")

    mirror = input("> ")

    if mirror == "1":
        print("Terrified as you realize this is your true self,")
        print("you hesitate before gathering yourself and stepping into the mirror gate.")
        print("You appear in a desert, there is much more for you to do.")
        print("But that is a tale for another story, perhaps a neverending one.")
    elif mirror == "2":
        print("You ask the mirror who is the fairest of them all. The mirror responds that it isn't you.")
        print("Enraged you smash the mirror. Too bad you didn't see the large shard")
        print("at the top that comes down on you. Better luck next time.")
    elif mirror == "3":
        print("You stare into the mirror of yourself until you realize your image is smirking.")
        print("Afraid, you turn away from the mirror. But now you fully understand what has happened.")
        print("You see the world as it was, but mirrored. You have swapped with your other self in the mirror.")
        print("Enjoy your life in the alternate world.")
    else:
        print("You close the door before you can realize what the image is and walk away.")
        print("You've seen enough horror movies to figure out where this could go.")

else:
    print("You stumble around and fall on a knife and die. Good job!")
