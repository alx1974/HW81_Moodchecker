#Aufgabe 8.1 Moodchecker
mood = input("Enter your mood:")
if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous" or mood == "excited":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Think positive. Soon it will be better.")
elif mood == "relaxed":
    print("Fine. Enjoy your mood.")
else:
    print("I don't recognize this mood")


