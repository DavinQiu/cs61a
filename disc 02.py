
from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

#1.5
def keep_ints(cond, n):
    i=1
    while i<=n:
        if (cond(i)):
            print(i)
        i+=1

#1.6
def weird_keep_ints(n):
    def keep_ints(cond):
        i = 1
        while i <= n:
            if (cond(i)):
                print(i)
            i+=1
    return keep_ints

#2.1
def multiply(m,n):
    if n==1:
        return m
    return (m+multiply(m,n-1))


#2.2
def countdown(n):
    if n==1:
        return (n)
    print (n)
    return (countdown(n-1))

#2.3
def countup(n):
    print(n)
    return (countup(n + 1))

#2.4
def sum_every_other_digit(n):
    if n < 10:
        return n
    return (n%10+sum_every_other_digit(n/100))

def is_even(x):
    return x % 2 == 0

keep_ints(is_even, 5)

weird_keep_ints(5)(is_even)

print (multiply(5,3))

countdown(5)

countup(5)

print(sum_every_other_digit(1234567))