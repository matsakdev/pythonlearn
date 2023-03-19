class Final(type):
    def __new__(cls, name, bases, classdict):
        for base in bases:
            if isinstance(base, Final):
                raise TypeError("Cannot be inherited from final class")
        return super().__new__(cls, name, bases, classdict)

class MyClass(metaclass=Final):
    pass