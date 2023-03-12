def findUniqueNumbers(first, last):
    # Iterate through array of numbers from first to last
    for num in range(int(first), int(last)):
        # Make a string from the number
        digits = str(num)
        # It has unique value by default but can be changed in the next loop
        unique = True
        # For each digit
        for i in range(len(digits)):
            # For each digit after i
            for j in range(i+1, len(digits)):
                # If they are eq, number will not be printed
                if digits[i] == digits[j]:
                    unique = False
                    break
        if unique:
            print(num)
