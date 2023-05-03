def addNumberToElementsInArray(array):
    # Input
    num = int(input("Enter a number: "))
    # Add the number to each element in list
    new_lst = list(map(lambda x: x + num, array))
    # Return new list
    return new_lst
