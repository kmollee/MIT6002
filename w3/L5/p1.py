import random


def oneTrial():
    '''
    Simulates one trial of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns True if all three balls are the same color,
    False otherwise.
    '''
    balls = ['r', 'r', 'r', 'g', 'g', 'g']

    chosenBalls = []
    for t in range(3):
        # For three trials, pick a ball
        ball = random.choice(balls)
        # Remove the chosen ball from the set of balls
        balls.remove(ball)
        # and add it to a list of balls we picked
        chosenBalls.append(ball)
    # If the first ball is the same as the second AND the second is the same as the third,
    #  we know all three must be the same color.
    if chosenBalls[0] == chosenBalls[1] and chosenBalls[1] == chosenBalls[2]:
        return True
    return False


def P2():
    '''
    Assume we have a bucket with 2 red, 1 green, and 5 blue balls.
    Two balls are drawn with replacement. What is the probability that
    the first ball is blue and the second ball is red?
    '''
    #balls = ['r', 'r', 'r', 'g', 'g', 'g']
    balls = ['r', 'r', 'g', 'b', 'b', 'b', 'b', 'b']
    chosenBalls = []
    for t in range(2):
        # For three trials, pick a ball
        ball = random.choice(balls)
        # Remove the chosen ball from the set of balls
        balls.remove(ball)
        # and add it to a list of balls we picked
        chosenBalls.append(ball)
    # If the first ball is the same as the second AND the second is the same as the third,
    #  we know all three must be the same color.
    if chosenBalls[0] == 'b' and chosenBalls[1] == 'r':
        return True
    return False


def noReplacementSimulation(numTrials, func):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    numTrue = 0
    for trial in range(numTrials):
        if func():
            numTrue += 1

    return float(numTrue) / float(numTrials)

print(noReplacementSimulation(10000, oneTrial))
print(noReplacementSimulation(10000, P2))
