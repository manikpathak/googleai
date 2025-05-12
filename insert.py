from time import sleep
import os
answer = 0
while True:
    print("***** Insert newline *****")
    print("here are your options: ")
    print("Number 1")
    print("Number 2")
    print("Select a number:")
    number = int(input(":> "))
    if number == 1:
        print("Great! you have selected Super Mario Typing Game!!")
        print("Game is now starting: ")
        print("3..")
        sleep(1)
        print("2..")
        sleep(1)
        print("1..")
        sleep(1)
        print("Princess Peach was kidnapped by Bowser and brave Mario is going to rescue Peach")
        sleep(1)
        print("Mario sees a goomba coming towards him... what should Mario do?")
        print("Options: 1: Jump over goomba 2: Stomp on Goomba")
        while True:
            answer = int(input(":> "))
            if answer == 1:
                print("sorry, you got killed ... Game Over..")
                break
            if answer == 2:
                print("well done, you are safe, now carry on on your quest")
                break
        if answer == 1: 
            break
        print("There is a question mark block up next. Hit it with your head and see what you get.")
        print ("Option 1: Mario hits the block with his head. Option 2: Nevermind, lets keep going on.")
        while True:
            answer = int(input(":> "))
            if answer == 1:
                print("Well done brave Mario, you get a mushroom powerup!")
                break
            if answer == 2:
                print("Sorry, you got killed by a koopa troopa. You will have to start over.")
                break
        if answer == 2: 
            break
        print("Now there is a koopa troopa in from you. What do you want to do")
        print("Option 1: Jump on it and kick it. Option 2: Just Leave..")
        while True:
            answer = int(input(":> "))
            if answer == 1:
                print("Well Done Mario! you have completed all the tasks.. ")
                break
            if answer == 2:
                print("Sorry we are finishing now, you can now try the second game.")
                break
        if answer == 2: 
            break
    if number == 2:
        print("Great! you have selected Super Mario Typing Game part 2!!")
        print("Game is now starting: ")
        print("3..")
        sleep(1)
        print("2..")
        sleep(1)
        print("1..")
        sleep(1)
        print("You are now in Bowser's scary castle to rescue princess Peach.")
        print("There is a spikey coming at you. what will you do?")
        print("Option 1: Jump over. Option 2: Go through")
        while True:
            answer = int(input(":> "))
            if answer == 1:
                print("Well done, you dodged the danger. Now you are safe. Carry on..")
            if answer == 2:
                print("Sorry, spikey just killed you with its spikes, you need to start again. Game Over")
                break
        if answer == 2: 
            break
        print("There is now a question mark block up next. Hit it with your head and see what you get")
        print("Option   1: Hit the question mark block and see whats inside. 2. Nevermind, keep on going.")
        while True:
            answer = int(input(":> "))
            if answer == 1:
                print("Correct, now we are going inside for our final boss fight with bowser.")
                break
            if answer == 2:
                print("Sorry, you are wrong, Bowser will kill you with his fire breath.. and he did not even brush today")
                break
        if answer == 2: 
            break
        print("Now you are fighting with the bowser to save your lovely Peach.")
        print("Option 1: Throw some fireballs at Bowser. Option 2: Walk away from Bowser.")
        while True:
            answer = int(input(":> "))
            if answer == 1:
                print("Correct, but you still need to fight with Bowser. He is so strong and evil..")
                break
            if answer == 2:
                print("Sorry, you died, try again... Game Over")
        if answer == 2: break
        print("Bowser took some fireballs but he is still quite strongly guarding the bridge.")
        print("Option 1: Now, jump over Bowser and get the axe. 2. Walk away from Bowser")
        while True:
            answer = int(input(":> "))
            if answer == 1:
                print("Correct, now you are finished with the game.")
            if answer == 2:
                print("Sorry, you lost. But you try again later...")

