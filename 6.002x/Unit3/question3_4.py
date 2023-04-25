def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    sameColor = 0
    for i in range(numTrials):
        balls = ['r','r','r','g','g','g']
        draw = []
        for j in range(3):
            draw.append(random.choice(balls))
            balls.remove(draw[j])
        if draw[0] == draw[1] == draw[2]:
            sameColor += 1
    return float(sameColor)/numTrials
    