import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randrange(0, 100, 2)

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 22, 2)


    

def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)