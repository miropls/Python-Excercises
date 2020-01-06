<<<<<<< HEAD
# Take a sentence as string input and print it in backwords order.

def reverse_sentence():
    user_str = input("Give me a sentence: ")

    sentece_list = user_str.split(" ")
    sentece_list.reverse()
    print(" ".join(sentece_list))

reverse_sentence()
=======
# Take a sentence as string input from the user, then print it out in reverse order.

def reverse_sentence():
    user_input = input("Please give me a sentence: ")
    user_input = user_input.split()
    user_input.reverse()
    print(" ".join(user_input))

reverse_sentence()
>>>>>>> ba1ba7f7100c594cf1612f385bcafbb8dc8fe4b1
