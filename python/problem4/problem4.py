#using brute force (not smart at all)

def is_palindrome(number):
    if (str(number) == str(number)[::-1]): return True
    return False


maximum_palindrome = 0
for i in xrange(100,1000):
    for j in xrange(100,1000):
        if (is_palindrome(i*j)):
            maximum_palindrome = max(maximum_palindrome,i*j)

print maximum_palindrome