bingo=[22,45,17,90,77]
import random
comodin=random.randint (10,99)


while comodin in bingo:
    comodin=random.randint (10,99)
bingo.append( comodin)
for num in bingo:
    print (num)