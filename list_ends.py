import random

rand_num_list = []

def random_num_list():
    for _ in range(20):
        rand_num_list.append(random.randint(1,50))
    print(rand_num_list)

def create_new_list_with_first_and_last():
    random_num_list()

    new_list = []
    new_list.append(rand_num_list[0])
    new_list.append(rand_num_list[-1])
    print(new_list)

create_new_list_with_first_and_last()