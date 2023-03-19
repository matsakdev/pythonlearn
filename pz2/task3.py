import re


def isEven(string):

    zeroesEvenString = "Рядок містить парну кількість нулів\n"
    zeroesOddString = "Рядок містить НЕпарну кількість нулів\n"
    onesEvenString = "Рядок містить парну кількість одиинць\n"
    onesOddString = "Рядок містить НЕпарну кількість одиниць\n"

    result = f'Поданий рядок: {string}\n'

    # Check if zeroes count is even
    match = re.search(r'^(?:1*01*01*)*$', string)

    # update result string
    result += zeroesEvenString if match else zeroesOddString

    # Check if zeroes count is even
    match = re.search(r'^(?:0*10*10*)*$', string)

    # update result string
    result += onesEvenString if match else onesOddString

    return result



