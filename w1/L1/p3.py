import pylab
import numpy as np


def loadFile():
    highs = []
    lows = []

    with open('./julyTemps.txt', 'r', encoding='UTF-8') as inFile:
        for line in inFile:
            field = line.split()
            if len(field) != 3 or 'Boston' == field[0] or 'Day' == field[0]:
                continue
            else:
                highs.append(field[1])
                lows.append(field[2])
    return (lows, highs)


def producePlot(lowTemps, highTemps):
    # refer http://stackoverflow.com/questions/10492283/error-multiplying-two-numpy-arrays
    #diffTemps = np.array(highTemps, np.int) - np.array(lowTemps, np.int)
    diffTemps = np.array(highTemps, np.float) - np.array(lowTemps, np.float)
    pylab.plot(range(1, 32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()

(low, high) = loadFile()
producePlot(low, high)
