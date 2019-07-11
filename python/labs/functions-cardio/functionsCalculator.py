print("welcome to the Calculator")

num1=int(raw_input("Choose the 1st number: "))
num2=int(raw_input("Choose the 2nd number: "))

def myAddFunction(add1, add2):
    sum = add1 + add2
    return sum
def mySubFunction(sub1, sub2):
    sub = sub1 - sub2
    return sub

def myMultiFunction(multi1, multi2):
    multi = multi1 * multi2
    return multi
    def myDivFunction(div1, div2):
        div = div1 / div2
        if (div%2) == 1:
            R = div1%div2
        else:
            R = 0
        return div, R
print("The sum that is: " + str(myAddFunction(num1, num2)))
print("The differnce that is: " + str(mySubFunction(num1, num2)))
print("The product that is: " + str(myMultiFunction(num1, num2)))
print("The quotient that is: " + str(myDivFunction(num1, num2)))
print("WIth the remainder of " + str())
