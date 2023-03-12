import random

def fillArray(length):

    # Initialize an array of zeros with length argument
    arr = [0] * int(length)

    # Choose a random number of ones between n/2 and n
    ones_count = random.randint(len(arr) // 2 + 1, len(arr))

    # Set num_ones elements to 1 at random positions
    for i in random.sample(population=range(len(arr)), k=ones_count):
        arr[i] = 1

    # Print the resulting array
    print(arr)
