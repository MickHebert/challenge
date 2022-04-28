#############################################################
# Name: Michael Hebert
# Date: 2/23/22
# Desc: A choose your own adventure game with 20 choices, 21 states, and 7 levels
#############################################################
from random import randint

def choices(choicestr, choice1, choice2, choice3):  # grabs player input to a question and returns certain paths
    choice = str(input(choicestr)).lower()  # gets player input in lowercase
    while True:
        if choice == choice1:
            return 1
        elif choice == choice2:
            return 2
        elif choice == choice3:
            return 3
        else:
            choice = str(input(f"Please type {choice1}/{choice2}/{choice3} "))  # makes the player type a valid answer

while True:  # main loop that keeps program running until the player quits
    boots = False  # initialization of variables
    staff = False
    sword = False
    loserend = False
    friEND = False
    end = False
    print("Your journey begins as an adventurer on a quest to retrieve the coveted Golden Shield of Excellence!"
          " You have with you a flimsy sword, a wooden shield, and no  armor."
          "\nYou arrive at your destination, a dark, dank cave filled with monsters, no doubt.")   # setting up story
    choicestr = "Do you enter? (y/n) "
    path = choices(choicestr, "y", "n", "  ")
    if path == 1:  # player enters the cave
        print("You enter the cave and before you lies an open chamber. Inside it you find three treasures!")
        choicestr = "Do you pick the sword, the staff, or the boots? "
        path = choices(choicestr, "sword", "staff", "boots")
        if path == 1:  # sword chosen
            print("You toss your old sword away for this much superior, lighter blade.")
        elif path == 2:  # staff chosen
            print("You grab the staff and it immediately starts to glow...")
            staff = True
        elif path == 3:  # boots chosen
            print("You pick up the boots and put them on. Immediately you feel a little lighter...")
            boots = True
        choicestr = "You come up to a massive ravine, open to the sky. Would you like to attempt to jump it? (y/n) "
        path = choices(choicestr,  "y", "n", "  ")
        if path == 1:
            madejump = randint(1, 3)
            if boots and madejump == 1:  # secret, funny ending
                print("The boots you are wearing suddenly begin to lift you higher and higher out of the cave! "
                      "You keep ascending, never to be seen again...")
                end = True
            elif madejump == 1 or madejump == 2:  # player makes the jump and continues the story
                print("You made the jump, and continue on into the cave!")
                print("You continue in the cave until you encounter a fierce fiend!")
                choicestr = "Fight the monster? (y/n) "
                path = choices(choicestr, "y", "n", "  ")
                if sword and path == 1:
                    print("You use your sword to fight the foe and defeat it!")
                elif staff and path == 1:
                    print("You attempt to use your staff against the foe, but your magic skills are not good enough! "
                          "You are slain...")
                    end = True
                elif boot and path == 1:
                    print("You run around the monster quickly with the help of your boots!")
                if path == 2:
                    print("You attempt to run away from the fiend, but you fall into the pit you jumped across! RIP!")
                    end = True
                print("Now that that monster is dealt with, you see before you a ramshackle wooden door. "
                      "You enter and find the Crypt of the Golden Shield of Excellence!")
                choicestr = "Enter? (y/n) "
                path = choices(choicestr, "y", "n", "  ")
                if path == 1:  # player enters, reaches the false ending
                    loserend = True
                elif path == 2:  # player leaves
                    friEND = True
            else:  # final jump condition, the player falls down the pit and is condemned to a dungeon forever
                print("You fall down the pit! You awake in a disgusting dungeon full of dastardly dwellers. "
                      "This is where you meet your end...")
                end = True
        elif staff and path == 2:  # player choses to turn away from the jump with their staff as a light
            print("You turn away from the pit and use your staff's light to lead the way until you reach a fancy door. "
                  "You open it to find the Chamber of Excellence!")
            choicestr = "Do you enter? (y/n) "
            path = choices(choicestr, "y", "n", "  ")
            if path == 1:  # player enters, reaches the false ending
                loserend = True
            if path == 2:  # player leaves
                friEND = True
        elif path == 2:  # player turns from the cliff with no light
            print("Without light or a staff of some kind, you fall down a hole and to your demise!")
            end = True
    elif path == 2:  # player leaves the cave
        print("Yeah, those monsters sure are scary. I'm sure another adventurer will get that shield. "
              "Let's head back to town.")
        choicestr = "Do you want a drink or to go home? "
        path2 = choices(choicestr, "drink", "home", "  ")
        if path2 == 1:  # player goes for a drink
            print("You decide to go for a drink to get your mind off of those scary monsters and your failed journey."
                  "\nAs the night goes on, you begin talking with a strange man. He mentions he has something really "
                  "awesome to show you")
            choicestr = "Follow the old man? (y/n) "
            path3 = choices(choicestr, "y", "n", "  ")
            if path3 == 1:  # player follows the old man, reaches the TRUE ENDING
                print("The man leads you to the back of the tavern where you see it! The Golden Shield of Excellence! "
                      "The man states that he used to be an adventurer as well and, in his old age, he cannot use this "
                      "shield anymore.\nThus he has been looking for someone to offload this heavy, solid gold shield "
                      "to. You gladly take it! Maybe leaving the cave wasn't such a bad idea after all")
                end = True
            elif path3 == 2:  # player does not trust the old man
                print("You decide not to follow the man, and he sighs sadly. You head on home and turn in for a "
                      "nice night of sleep. Maybe another adventure will come your way soon!")
                end = True
        elif path2 == 2:  # player goes home and to sleep
            print("You decide to go home and go to bed for sweet dreams of the adventures to come...")
            end = True

##### Endings #####
    if loserend:  # end text for the false ending
        print("You enter the chamber and gaze in awe at its beauty. Approaching the Stand of the "
              "Golden Shield of Excellence, you notice a small note written on a piece of McFarquad's "
              "napkin that reads:\n'HAHA' this Golden Shield of Excellence is mine! All mine!!!'\n"
              "Impossible! You've wasted all your time in this cave for no reason! What a disappointment!\n"
              "You turn around towards the Exit of Excellence and ascend the Stairs of Excellence back into"
              " the light of day (of Excellence). Better luck next time!")
        end = True

    if friEND: # end text for the no friends ending
        print("You know, maybe that shield isn't the real prize of this journey, it was the friends we made"
              " along the way! After realizing you have no friends, you turn back, sad, and go home.")
        end = True

    if end:
        choicestr = "Do you want to play again? (y/n) "
        ending = choices(choicestr, "y", "n", "  ")
        if ending == 1:
            print("\n\n\n\n\n")
        elif ending == 2:
            print("OK! See you next time!")
            break
