import random


def rollDie():
    """roll the die"""
    return random.choice([1, 2, 3, 4, 5, 6])


def rollN(n):
    """roll the die, n times"""
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    return result

# print(rollN(5))


def getTarget(goal):
    """
    goal:string like '11111'
    return int
    roll the die, until reach the goal
    """
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries += 1
        result = rollN(numRolls)
        if result == goal:
            return numTries


def runSim(goal, numTrials):
    """
    simulate roll the die
    goal:string like '11111'
    numTrials:int
    return None, print out Average times = (roll total times)/(numTrials)
    make numTrials times, reach the goal
    """
    total = 0
    for i in range(numTrials):
        total += getTarget(goal)
    print('Average number of tries =', total / float(numTrials))

# runSim('11111', 100)  # 7776 possibilities
# runSim('54324', 100)


def atLeastOneOne(numRolls, numTrials):
    """
    numRolls:int how many die have
    numTrials:int how many time you want to reach the goal '1' contain 1
    possibility is 1 - (5/6)**5 if numRolls is 5
    """
    numSuccess = 0
    for i in range(numTrials):
        rolls = rollN(numRolls)
        if '1' in rolls:
            numSuccess += 1
        fracSuccess = numSuccess / float(numTrials)
    print(fracSuccess)

atLeastOneOne(10, 1000)

# if classroom have 100 student, how much possibility student's birthday
# is today?

# every student's birthday is today, possibility is 1/365

# if today is not first student's birthday, possibility is 364/365
# if today is not first and second student's birthday,
# possibility is (364/365)**2, and so on...

# so today is someone's birthday possibility is 1-(364/365)**100
