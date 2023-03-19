import random
import string

def generateRandomString():
    # Generate a string of characters of length from 6 to 13
    length = random.randint(6, 13)
    result = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    # Choose 5 random positions to insert the exclamation marks
    positions = random.sample(range(length), 5)

    # Insert the exclamation marks at the chosen positions
    for pos in positions:
        result = result[:pos] + '!' + result[pos+1:]

    # Print the resulting string with exclamation marks
    print(result)