import math

class PrimeFactor:

    def __init__(self, number):
        self.n = number

    def calculatePrimes(self):

        primes = []

        for x in xrange(2, int(math.floor(math.sqrt(self.n)))):

            if (self.n % x == 0):
                primes.append(x)


        return primes


n = PrimeFactor(13195)

print n.calculatePrimes()