import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
numSteps = 200

CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # probability of rabbit reproduction is 1 - current rabbit population / max rabbit population
    probReproduction = 1 - CURRENTRABBITPOP / MAXRABBITPOP
    # for each rabbit
    for rabbit in range(CURRENTRABBITPOP):
        # if probability of reproduction is greater than random number
        if probReproduction > random.random():
            # increment rabbit population
            CURRENTRABBITPOP += 1
    # if rabbit population exceeds max rabbit population
    if CURRENTRABBITPOP > MAXRABBITPOP:
        # set rabbit population to max rabbit population
        CURRENTRABBITPOP = MAXRABBITPOP
    # if rabbit population is less than 10
    if CURRENTRABBITPOP < 10:
        # set rabbit population to 10
        CURRENTRABBITPOP = 10
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # it the fox population is less than 10, should do nothing
    if CURRENTFOXPOP < 10:
        return
    # probability of fox eating rabbit is current rabbit population / max rabbit population
    probEatRabbit = CURRENTRABBITPOP / MAXRABBITPOP
    # for each fox
    for fox in range(CURRENTFOXPOP):
        # if probability of eating rabbit is greater than random number
        if probEatRabbit > random.random():
            # decrement rabbit population
            CURRENTRABBITPOP -= 1
            # if probability of fox giving birth is greater than random number
            if 1/3 > random.random():
                # increment fox population
                CURRENTFOXPOP += 1
        # if probability of fox dying is greater than random number
        elif 1/10 > random.random():
            # decrement fox population
            CURRENTFOXPOP -= 1
    # if fox population is less than 10
    if CURRENTFOXPOP < 10:
        # set fox population to 10
        CURRENTFOXPOP = 10

    # if rabbit population is less than 10
    if CURRENTRABBITPOP < 10:
        # set rabbit population to 10
        CURRENTRABBITPOP = 10

    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbitPopulations = []
    foxPopulations = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitPopulations.append(CURRENTRABBITPOP)
        foxPopulations.append(CURRENTFOXPOP)
    return (rabbitPopulations, foxPopulations)

rabbitPopulations, foxPopulations = runSimulation(numSteps)
pylab.plot(rabbitPopulations, label = 'Rabbit Population')
pylab.plot(foxPopulations, label = 'Fox Population')
pylab.xlabel('Time Steps')
pylab.ylabel('Population')
pylab.title('Rabbit and Fox Populations')
pylab.legend()
pylab.show()

coeff = pylab.polyfit(range(len(rabbitPopulations)), rabbitPopulations, 2)

pylab.plot(pylab.polyval(coeff, range(len(rabbitPopulations))))

foxCoeff = pylab.polyfit(range(len(foxPopulations)), foxPopulations, 2)

pylab.plot(pylab.polyval(foxCoeff, range(len(foxPopulations))))
