import random
number=random.randint(1,10)
print (number)
a=0
count=0
while(a!=number):
    if(a!=number):
        a=int(input('Guess number from One to Ten\n'))
        count += 1
    else:
        break

print('You guessed the right number',number)
print('You took',count,'guesses to make the right guess')
