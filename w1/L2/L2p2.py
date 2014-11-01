import random


def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    return random.randrange(0, 100, 2)
if __name__ == '__main__':
    for _ in range(100):
        print(genEven())
