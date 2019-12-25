# Create a list of random numbers, and then in a second function print out a set with no duplicates.

import random

list_of_numbers = []

def create_a_random_list():
    for _ in range(20):
        list_of_numbers.append(random.randint(1,50))
    return list_of_numbers

def make_list_into_set(listofnumbers):
    # Turn the list given as an argument into a list, which removes duplicates.
    list_of_numbers = set(listofnumbers)
    # Turn the set back into a list and return it.
    list_of_numbers = list(list_of_numbers)
    return list_of_numbers

create_a_random_list()
make_list_into_set(list_of_numbers)

print(list_of_numbers)