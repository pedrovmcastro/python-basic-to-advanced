"""
Exercise:

(PT-BR)
Exercício:

"""
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


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowel(fruit)]

print(fruits_with_more_than_two_vowels)
