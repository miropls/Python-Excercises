# Take a sentence as string input from the user, then print it out in reverse order.

def reverse_sentence():
    user_input = input("Please give me a sentence: ")
    user_input = user_input.split()
    user_input.reverse()
    print(" ".join(user_input))

reverse_sentence()
