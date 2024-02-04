# Exercise 2:
# Write a Python program to implement a generator that generates random numbers within a given range.

from random import randint

def random_generator(n, first, last):
    for i in range(n):
       yield randint(first, last)

print('Enter the range:')
first = int(input('First:'))
last = int(input('Last:'))
n = int(input('How many times?'))

for num in random_generator(n, first, last):
    print(num)
