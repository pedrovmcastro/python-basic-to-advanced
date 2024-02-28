"""
Exercise 4:
Create a program that takes the user's date of birth in the format MM/DD/YYYY, and returns to the user how many days are 
left until the next birthday and how old the person will be.
Example: "There are x days left until your yth birthday."


(PT-BR)
Exercício 4:
Faça um programa que receba do usuário uma data de nascimento, no formato MM/DD/YYYY,
e retorne para o usuário quantos dias faltam para o próximo aniversário e quantos anos a pessoa vai fazer.
Ex: "Faltam x dias para o seu aniversário de y anos." 
"""

from datetime import datetime

date_birth = input("What is your date of birth (MM/DD/YYYY)? ")
date_birth = datetime.strptime(date_birth, "%m/%d/%Y")

age = datetime.today().year - date_birth.year

date_birth = date_birth.replace(year=datetime.today().year)
date_today = datetime.combine(datetime.now(), datetime.min.time())

if date_today > date_birth:
    date_birth = date_birth.replace(year=date_birth.year + 1)
    age += 1

delta = date_birth - date_today

if date_birth.day == date_today.day:
    print("Congratulations! Today is your birthday.")
else:
    print(f"There are {delta.days} days left until your {age}th birthday.")

