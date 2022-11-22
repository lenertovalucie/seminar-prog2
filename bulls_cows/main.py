import random


code = random.choice(range(1,10))
ones = 9*"1"
listek = [int(i) for i in ones]
index = range(10).index(code)
listek.insert(index, 0)
code = random.sample([0,1,2,3,4,5,6,7,8,9], counts=listek, k=3)
code.insert(0, random.choice(range(1,10)))
codenum = ''.join(str(x) for x in code)

inputie = ''
while inputie != codenum:
    while True:
        inputie = str(input("Guess a 4-digit number with no repeats: "))
        if len(set(inputie)) == len(inputie) and len(inputie) == 4:
            break
        else:
            print("Doesnt satisfy")
    bulls = 0
    cows = 0
    for i in inputie:
        if i in codenum:
            if inputie.index(i) == codenum.index(i):
                bulls+=1
            else:
                cows+=1
    print(f"Bulls : {bulls}, Cows: {cows}")

print("You got it")


print(codenum)

