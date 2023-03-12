def defineDirection():
    # Get initial direction and input command
    direction = int(input("Enter the initial direction [it may be 11, 12, 13, 14]: "))
    command = int(input("Enter the command [0, 1, -1]: "))

    # Throw an error for wrong input
    if direction < 11 or direction > 14 or command < -1 or command > 1:
        raise Exception('You\'ve wrote wrong initial direction or command')

    # Result is just a sum of direction and command
    result = direction + command

    # But some cases should be considered.
    # We have only 4 sides, so result 10 is definitely 15
    if result == 10:
        result = 14
    elif result == 15:
        result = 11

    # Return the result
    return result
