# Exercise 1:
# Write a Python program that creates a generator function that yields cubes of numbers from 1 to n. Accept n from the user. 

def cubes(n):
    count = 1
    while count <= n:
        yield count**3
        count += 1

n = int(input('Enter a number:'))
for num in cubes(n):
    print(num)
