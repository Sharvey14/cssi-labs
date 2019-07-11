print("welcome to the Calculator")

def count_spaces(s):
    return s.count(" ")

def count_vowels(cs):
    numA = s.count("a") #number of a's in the string
    numE = s.count("e") #number of e's in the string
    numI = s.count("i") #number of i's in the string
    numO = s.count("o") #number of o's in the string
    numU = s.count("u") #number of u's in the string
    numY = s.count("y") #number of y's in the string
    sumVowels = numA + numE + numI + numO + numU + numY
    return sumVowels

def count_total(s):
    return count_spaces(s) + count_vowels(s)

print(count_spaces("hello there, you are the best!"))

countNum = count_vowels("hello there, you are the best!")
print(countNum)

print(count_total("hello there, you are the best!"))
