print("""

The True or False GAME (version: 1.2.3)
=======================================

""")
print("do you want to play a game? The options are yes or no.")
while True:
    print()
    choice = input("Enter your choice carefully: ")
    if choice == "yes":
        print("good choice.... you chose well!!!")
        print("okay, the game is called true or false!!!")
        print()
        print("here are the options if you don't already know: ")
        print(" 1. somebody rode a bike to their school.")
        print(" 2. somebody loved games so they played with them.")
        print(" 3. somebody did a lots of maths and it was five pages daily")
        print()
        answer1= input("Question# 1: Somebody rode their bike to the mall. True or false: ")
        if answer1 != "false":
            print()
            print("sorry, Wrong Answer!!! 👎")
            print("try again next time 🥺")
            print()
            break
        if answer1 == "false":
            print()
            print("well done that is the right answer 👍")
            print("here is your next question")
            print()
        answer2 = input("somebody loved games so they played with them?")
        if answer2 == "true":
            print()
            print("Correct Answer!!! 🎉")
            print("here is your Final question")
            print()
        if answer2 != "true":
            print()
            print("Sorry wrong answer.")
            print("try again next time 🥺")
            break
        answer3 = input("somebody did a lot of games and it was five games daily.")
        if answer1 != "false":
            print()
            print("sorry, Wrong Answer!!! 👎")
            print("we are finishing now you can try again later 🥺")
            break
        if answer1 == "false":
            print()
            print("well done that is the right answer 👍")
            print("you have completed your game. Goodbye!!!")
            print()
        break
    if choice == "no":
        print()
        print("ok, bye... ")
        break
    else:
        print("Choice must be either yes or no.")