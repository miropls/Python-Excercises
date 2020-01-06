# Take a sentence as string input and print it in backwords order.

def reverse_sentence():
    user_str = input("Give me a sentence: ")

    sentece_list = user_str.split(" ")
    sentece_list.reverse()
    print(" ".join(sentece_list))

reverse_sentence()