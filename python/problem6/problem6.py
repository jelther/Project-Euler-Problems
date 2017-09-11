import operator
import math

first_hundred = list(xrange(1,101))

print int(math.pow(reduce(operator.add,first_hundred),2) - reduce(operator.add,[x**2 for x in first_hundred]))

