#Logan Teats
#Calculator
#It let you makes mathimatical functions
#The pogils in class
# * multiplies the same stringle 10 times
smile = ":)" * 10
angry = ">:( " * 10
print("Hello welcome to",sep=" ")
print("Calculator,",end= " ")
print("have fun")
attempts = 0
while attempts < 2:
    name = input("name?:")
    if name == "" or name == " ":
        print("That is not a name")
        attempts += 1
        name = input("name?:")
        if attempts == 2:
            print("Please try again with a real name")
            exit()
    else:
        break
#recieves the numbers
print("first number?")
num1 = float(input("Enter the 1st number: "))
print("oprator?")
#recieves opporator
for i in range(2):
    operator = input("(+,-,*,/,%,//,**,):")
    if operator not in ["+", "-", "*", "/" ,"%" ,"//", "**"]:
        print("not an operator, try again")
        continue
    print("Second number?")
    num2 = float(input("Enter the 2nd number: "))
    #adds the 2 numbers
    if operator == "+":
        result = num1 + num2
        print(result)
        break
    #subtracts the 2 numbers
    elif operator == "-":
        result = num1 - num2
        print(result)
        break
    #multiplies the 2 numbers
    elif operator == "*":
        result = num1 * num2
        print(result)
        break
    #divides the 2 numbers
    elif operator == "/":
        if num1 == 0 and num2 == 0:
            print("Doesnt exist")
            print (angry)
        elif num2 == 0:
            print("Can't divide by 0")
            print (angry)
        result = num1 / num2
        print(result)
        break
    #divides the 2 numbers and rounds to the nearest whole number
    elif operator == "//":
        result = num1 // num2
        print(result)
        break
    #puts the num1 to the power of num2
    elif operator == "**":
        result = num1 ** num2
        print(result)
        break
    #divides the 2 numbers and shows the leftover
    elif operator == "%":
        result = num1 % num2
        print(result)
        break
# + combines 2 strings
message = "results are in " + name
if operator == "+":
    print(message)
    print(smile)
elif operator == "-":
    print(message)
    print (smile)
elif operator == "*":
    print(message)
    print (smile)
elif operator == "/":
    print(message)
    print (smile)
elif operator == "%":
    print(message)
    print (smile)
elif operator == "//":
    print(message)
    print (smile)
elif operator == "**":
    print(message)
    print (smile)
else:
    print (angry)
if result <= 0:
    print("wow so negative")
elif result >= 0:
    print("wow so positive")
