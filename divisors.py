# Ask the user for a number and find all it's divisors between values of 1 and 1000.

list_of_numbers = range(1,1000)

users_number = int(input("Please input a number: "))

def FindDividors(users_number):
    for num in list_of_numbers:
        if num % users_number == 0:
            print(num)

FindDividors(users_number)