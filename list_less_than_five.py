# Program where a function creates a list of 20 random numbers between 1 and 25, and a second function prints out a list with all the numbers under the value of 5.

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