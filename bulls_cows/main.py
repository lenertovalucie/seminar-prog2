import random

numbers = [0,1,2,3,4,5,6,7,8,9]
sec0 = 0
while sec0 == 0:
    sec0 = numbers[random.randint(0,9)]
numbers.remove(sec0)
sec1 = numbers[random.randint(0,len(numbers)-1)]
numbers.remove(sec1)
sec2 = numbers[random.randint(0,len(numbers)-1)]
numbers.remove(sec2)
sec3 = numbers[random.randint(0,len(numbers)-1)]

print(sec0, sec1, sec2, sec3)