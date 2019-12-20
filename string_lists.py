# Program asks the user for a word and checks whether it is a palindrome.

given_word = input("Please submit a word and I will check if it's a palindrome: ")
given_word_list = []
reversed_word = []

for character in given_word:
    given_word_list.append(character)
    reversed_word.append(character)

reversed_word.reverse()

def CheckIfEqual(given_word_list, reversed_word):
    if reversed_word == given_word_list:
        print("The given word is a palindrome!")
    else:
        print("The given word is not a palindrome!")

CheckIfEqual(given_word_list, reversed_word)
