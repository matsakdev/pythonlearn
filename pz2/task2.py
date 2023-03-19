# validator with list of validators which should be processed
def validator(*validators):
    # function for which parameters validators should be processed
    def decorator(func):
        # wrap for any count of args.
        # wrapper will call fun if all is ok
        # else the error would be thrown
        def wrapper(*args, **kwargs):
            # check if argument is valid
            for i, arg in enumerate(args):
                if i < len(validators):
                    validate = validators[i]
                    # else throw error with arg name
                    if not validate(arg):
                        raise ValueError(f"Invalid argument: {arg}")
            # the same for kwargs (as dictionary)
            for key, value in kwargs.items():
                if key in validators:
                    validate = validators[key]
                    if not validate(value):
                        raise ValueError(f"Invalid argument: {value}")
            # all is valid, call func
            return func(*args, **kwargs)
        return wrapper
    return decorator

def positive(value):
    return value > 0

def integer(value):
    return isinstance(value, int)

@validator(positive, integer)
def create_user(id, age):
    print(f"Creating user with id={id}, age={age}")

