import random
n=random.randint(1,10)
p=int(input("Guess a number from 1 - 10: "))
while p!=n:
    if(p>n):
        p=int(input("Guess smaller please: "))
    else:
        p = int(input("Guess bigger please: "))
print("You got it!")
