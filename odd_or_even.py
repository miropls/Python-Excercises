

def checkOddOrEven():
    num = int(input("Please insert a number: "))
    if num % 2 == 0 and num % 4 == 0:
        print("The number you inserted is dividable by both 2 and 4 and is therefor even.")
    elif num % 2 == 0:
        print("The number you inserted is dividable by 2 and is therefor even.")
    elif num % 2 != 0:
        print("The number you inserted is not dividable by 2 and is there for odd.")
        
checkOddOrEven()