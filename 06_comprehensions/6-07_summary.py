# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits
# to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
print('1 ', uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce
# output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.title() for fruit in fruits]
print('2 ', capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# Hint: You'll need a way to check if something is a vowel.


def count_vowel(fruit):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for char in fruit:
        if char in vowels:
            vowels.remove(char)
            vowel_count += 1
    if vowel_count > 2:
        return 1
    return 0


fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowel(fruit)]
print('3 ', fruits_with_more_than_two_vowels)
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_5_char = [fruit for fruit in fruits if len(fruit) > 5]

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
print('8 ', [len(fruit) for fruit in fruits])

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits
# that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print('9 ', fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers
print('10 ', [number for number in numbers if number % 2 == 0])

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
print('11 ', [number for number in numbers if number % 2 != 0])

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
print('12 ', [number for number in numbers if number > 0])

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
print('13 ', [number for number in numbers if number < 0])

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
print('14 ', [number for number in numbers if 10 <= number <= 99])

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared.
# Output is [4, 9, 16, etc...]
numbers_squared = [number**2 for number in numbers]
print('15 ', numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are
# both odd and negative.
odd_negative_numbers = [number for number in numbers if number % 2 != 0 and number < 0]
print('16 ', odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
numbers_plus_5 = [number+5 for number in numbers]
print('17 ', numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list.
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
from math import sqrt


def ehprimo(number):
    if number < 0:
        number *= -1
    for i in range(1, int(sqrt(number))):
        if number % i == 0 and i != number:
            return 0
    return 1


primes = [number for number in numbers if ehprimo(number)]
print('18 ', primes)
