import random
import numpy

def throwNeedles(numNeedles):
    inCircle = 0
    for needles in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        # If the distance of the point from the origin (of the circle) is <= than 1 (radius),
        # then the point is in the circle
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))


def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = numpy.std(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. = ' + str(curEst) + ', Std.dev = ' + str(round(sDev, 6)) + ', numNeedles = ' + str(numNeedles))
    return (curEst, sDev)

def estPi(precision, numTrials):

    numNeedles = 100
    sDev = precision
    # Calls get est with an ever-growing number of needles
    # until getEst returns an estimate that,
    # with a confidence of 95%, is within precision
    # of the actual values.
    while sDev >= precision/2:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst


estPi(0.005, 100)