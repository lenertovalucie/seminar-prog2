<<<<<<< HEAD
import random
numbers = ["1","2","3","4","5","6","7","8","9"]
secret_code = []
while len(secret_code) < 4:
  secret_code.append(random.choice(numbers))
  numbers.remove(secret_code[-1])
secret_code_string = secret_code[0] + secret_code[1] + secret_code[2] + secret_code[3]


guess = input("Try to guess the code: ")
cows = 0
bulls = 0
while guess != secret_code_string:
  cows = 0
  bulls = 0
  for i in range (0,len(guess)):
    if guess[i] == secret_code[i]:
      bulls += 1
    elif guess[i] in secret_code:
      cows += 1
    else:
      None  
  if bulls == 1:
    bulls = "1 Bull"
  else:
    bulls = str(bulls) + " Bulls"
  if cows == 1:
    cows = "1 Cow"
  else:
    cows = str(cows) + " Cows"
  print(f"{bulls} and {cows}")
  guess = input("Guess: ")
print("You cracked the code")
=======
print("ahoj", "cau", sep= ",")
>>>>>>> origin
