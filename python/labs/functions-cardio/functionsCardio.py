
# print ("Welcome to the Crib")
#
# word1 = raw_input("Enter a word: ")
# word2 = raw_input("Enter another word: ")
# word3 = raw_input("Enter a third word: ")
#
# def longWord (w1, w2, w3):
#     if len(w1) > len(w2) and len(w1) > len(w3):
#         longest = w1
#         print(longest + " is the longest word.")
#         return longest
#     elif len(w2) > len(w1) and len(w2) > len(w3):
#         longest = w2
#         print(longest + " is the longest word.")
#         return longest
#     else:
#         longest = w3
#         print(longest + " is the longest word.")
#         return longest
#
# longWord(word1, word2, word3)

#-----------------------------------------------------------------------------------------------------------------------------------

print("exercise #2")

word = raw_input("Enter a word: ")

def reverseWord(w):
    return w[::-1]

print("This is your word backwards: " + reverseWord(word))

#------------------------------------------------------------------------------------------------------------------------------------

# num1 = int(raw_input("Give me side 1 length: "))
# num2 = int(raw_input("Give me side 2 length: "))
# num3 = int(raw_input("Give me side 3 length: "))
#
# def is_triangle(s1, s2, s3):
#     sum1 = s1 + s2 #test if greater than s3
#     sum2 = s2 + s3 #test if greater than s1
#     sum3 = s3 + s1 #test if greater than s2
#     if sum1 > s3 and sum2 > s1 and sum3 > s2:
#         print("you have a traingle!")
#         return True #I have a triangle!
#     else:
#         print("No triangler for you!")
#         return False
#
# is_triangle(num1, num2, num3)
