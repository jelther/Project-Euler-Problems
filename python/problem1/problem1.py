# this is a naive approach, i guess.
# but the algorithm works

total_sum = 0

#numbers BELOW 1000, so the xrange will go only until 999
for i in xrange(1,1000):
    if (i % 3 == 0) or (i % 5 == 0):        
        total_sum = total_sum + i

print total_sum
