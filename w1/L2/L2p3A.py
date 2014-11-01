import random


def deterministicNumber():
    random.seed(0)  # This will be discussed in the video "Drunken Simulations"
    return 2 * random.randint(5, 10)


def stochasticNumber():
    """
    Stochastically generates and returns a uniformly distributed even number
    between 9 and 21
    """
    return random.randrange(10, 22, 2)


if __name__ == '__main__':

    print('=====deterministicNumber=====')
    for _ in range(50):
        print(deterministicNumber())

    print('=====stochasticNumber=====')

    for _ in range(50):
        print(stochasticNumber())
