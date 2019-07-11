print ("welcome to Shanshan's Mall")

myString = raw_input("give me a string loop through: ")

#create a program that will print each letter in the string individually
#using a for loop

letterNum = 1

for character in myString:
    print("This is letter number %s" % (letterNum))
    letterNum = letterNum + 1
    print(character)
