import random

def __main__():
    generate_password()

def generate_password():
    s = "abcdefghijklmnopqrstuvwxyzåäö!¤%&/()=?`*^"

    print("Hello, I am a password generator!")
    psw_strength = int(input("How strong of a password would you like(6-20 characters): "))

    password = "".join(random.sample(s, psw_strength))
    print(password)

    

if __name__ == "__main__":
    __main__()