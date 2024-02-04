# Exercise 3:
# Write a Python program that creates a generator function that generates all prime numbers between two given numbers. 

import math

def primes_generator(start, end):
    for i in range(start, end+1):
        if i > 1:
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    break
            else:
                yield i

start = int(input('Enter the start value:'))
end = int(input('Enter the end value:'))

for num in primes_generator(start, end):
    print(num)
    