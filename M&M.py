import random

def M_M (amount):
    list = {
        'Green' : 0,
        'Blue' : 0,
        'Orange': 0,
        'Brown' : 0
    }
    colers = ['Orange', 'Blue', 'Green', 'Brown']
    for x in range(amount):
        list[random.choice(colers)] += 1
    return list
How_much = int(input('How much M & M do u want ? : '))
print(M_M(How_much))

