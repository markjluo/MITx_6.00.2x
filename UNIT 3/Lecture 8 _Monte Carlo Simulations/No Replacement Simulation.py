import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''

    class Sim(object):
        def __init__(self):
            self.balls = []
            for i in range(3):
                self.balls.append('g')
                self.balls.append('r')
        def getBalls(self):
            return self.balls
        def DrawThree(self):
            """Draw three balls from self.balls, return 1 if three balls of the same color are drawn"""
            balls_copy = self.balls.copy()
            for i in range(3):
                draw = random.choice(balls_copy)
                balls_copy.remove(draw)
            if balls_copy == ['g', 'g', 'g'] or balls_copy == ['r', 'r', 'r']:
                return True
            else:
                return False

    n = 0
    a = Sim()
    for trial in range(numTrials):
        n += int(a.DrawThree())
    return n/numTrials


print(noReplacementSimulation(10000))