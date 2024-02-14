"""
Exercise 8:
Read the age and length of service of a worker and prints whether they can retire or not. The retirement conditions are:
    - Being at least 65 years old.
    - Or having worked at least 30 years.
    - Or being at least 60 years old and having worked at least 25 years.

Exercício 8 (PT-BR):
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
As condições para aposentadoria são
    - Ter pelo menos 65 anos.
    - Ou ter trabalhado pelo menos 30 anos,
    - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""

age = int(input("Age: "))
leng = int(input("Lenght of service: "))

if age >= 65 or leng >= 30 or (age >= 60 and leng >= 25):
    print("Can retire")
else:
    print("Can't retire")
    