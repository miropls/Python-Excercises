# Ask for users name and year of birth, then print out their name and their age in 100 years.

name = input("What is your name?: ")
birth_year = int(input("And which year were you born?: "))
age_in_100_yrs = birth_year + 100

print("So, your name is " + name + " and your birthyear was " + str(birth_year) + ". You will be 100 years old in the year " + str(age_in_100_yrs))