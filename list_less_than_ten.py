import random

number_list = []

def CreateList():
    for num in range(20):
        num = random.randint(1,25)
        number_list.append(num)

def PrintListWithNumbersLessThanFive():
    CreateList()
    for x in number_list:
        if x <= 5:
            print(x)

PrintListWithNumbersLessThanFive()