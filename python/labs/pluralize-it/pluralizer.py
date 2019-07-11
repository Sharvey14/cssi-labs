print("The Game you might Win")
name = raw_input("What's your name? ")
points = int(raw_input ("Enter a number: "))

if (points % 2 == 1:
    print (name + " you suck at this game, sorry loser")
else:
    print("congratulations " + name + "! You won " + str(points) + " points!")
