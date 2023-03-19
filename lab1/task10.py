import re

def findDigitsSum(text):
    # find words consisting of numbers
    numbers = re.findall(r'\b\d+\b', text)

    # calculate the sum of numbers
    total = sum(int(number) for number in numbers)

    print("Words consisting of numbers: ", numbers)
    print("Sum of numbers: ", total)