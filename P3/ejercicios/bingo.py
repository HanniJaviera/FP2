import random

bingo=[]
for i in range(6):
    bingo.append(random.randint(1,99))

num=1

lista="Los numeros del bingo son"

with open(f'lista')