#!/usr/bin/env python
import random
import time

city = {"Zagreb":"Croatia", "Ljubljana":"Slovenia", "Rome":"Italy", "Oslo":"Norway", "Baku":"Azerbaijan", "Moscow":"Russia", "Washington D.C": "USA", "Paris":"France"}
name = raw_input("What is your name? ")
print("Hello, "+name+". You will be completing a quiz that will ask you 8 questions which will test you on capital cities. Try your best at each question and good luck! \nIf you get stuck please enter 'hint' to get the first letter. If you are still lost, enter 'I am lost' for a complete answer.")
points = 0
time.sleep(5)

for cities in random.sample(list(city), 8):
    while True:
        hint = "hint"
        hint2 = "I am lost"
        capital = city[cities]
        print "What is the capital of " + capital + "?"
        answer = raw_input("Please enter your answer: ")
        if cities==answer:
            print "You are correct"
            points +=2
            break
        elif answer == hint.lower():
            print "Hint is " + cities[:1]
            points -= 5
            answer2 = raw_input("Please enter your answer: ")
            if cities==answer2:
                print "You are correct"
                points += 2
                break
            else:
                print "You are wrong, please try again"
                points -= 1
        elif answer == hint2:
            print "The correct answer is " + cities
            points -= 10
            break
        else:
            print "You are wrong, please try again"
            points -= 1
print "Your total number of points is " + str(points)
if points < 5 and points > 0:
    print "Go back to school!!"
elif points <= 0:
    print "There is no hope for you!"
elif points >=5 and points < 10:
    print "Not bad"
elif points > 10:
    print "Wow, you are good"









