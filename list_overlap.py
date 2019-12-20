import random

list_a = []
list_b = []
common_item_list = []

def MakeARandomListAB():
    for num in range(50):
        num = random.randint(1,100)
        list_a.append(num)
        return list_a
    for num in range(50):
        num = random.randint(1,100)
        list_b.append(num)
        return list_b
        
MakeARandomListAB()

def PrintCommonNumbers(list_a, list_b, common_item_list):
    for common_item in list_a:
        if common_item in list_b and common_item not in common_item_list:
            common_item_list.append(common_item)
            print(common_item_list)
            return common_item_list

PrintCommonNumbers(list_a, list_b, common_item_list)
print(common_item_list)