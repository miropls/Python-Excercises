# Fibonacci sequence is a never ending list of numbers, where the next number is the sum of two previous numbers.

def create_fibonacci_sequence():
    # Create a list to store the numbers
    fibonacci_sequence = [1, 1]
    # Sequence starts at number 1
    a = 1
    # Second number is also known, and it is 1 as well
    b = 1

    # Sequence is explained at start. Starts like 1,1,2,3,5,8...
    for _ in range(20):
        c = a + b
        fibonacci_sequence.append(c)
        a = b + c
        fibonacci_sequence.append(a)
        b = c + a
        fibonacci_sequence.append(b)

    print(fibonacci_sequence)

create_fibonacci_sequence()

# I believe there is a shorted and more logical way to accomplish this task but this is what I've come with, seems to work correctly.