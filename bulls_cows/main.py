import random
numbers = [1,2,3,4,5,6,7,8,9]
secret_code = []

while len(secret_code) < 5:
   if random.choice(numbers) not in secret_code:
        random.choice(numbers)

print(secret_code)
print("kamarad")


