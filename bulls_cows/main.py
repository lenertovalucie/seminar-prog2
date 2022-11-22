<<<<<<< HEAD
import random


def hide():
  for i in range(50):
    print("")
def test(kod):
  erej = []
  for i in kod:
    erej.append(i)
  erej.sort()
  for i in range(len(erej)-1):
    if erej[i] == erej[i+1]:
      return False
  return True
def setup():
  kod = input("Enter secret code: ")
  hide()
  while test(kod) == False:
    kod = input("Enter secret code with unique numbers: ")
    hide()
  return kod
def pozdrav():
  print("-"*60)
  print("-"," "*25,"GLHF"," "*25,"-")
  print("-"*60)

def guess(kodek,kod,pocet):
  buls = 0
  cows = 0
  if kodek == kod: 
    print(f"YOU WON! after {pocet+1} moves.")
    quit()
  else:
    for i in range(4):
      for j in range(4):
        if i == j and kodek[i] == kod[j]:
            buls+=1
            continue
        elif kodek[i] == kod[j]:
          cows+=1
          continue
  return[buls,cows]

def play(kodik, pocet):
  bulskaus = [0,0]
  bulskaus = guess(input("Zadej kod:"),kodik,pocet)
  print(f"You have {bulskaus[0]} bulls and {bulskaus[1]} cows.")
  pocet+=1
  play(kodik, pocet)

def main():
  volba = input("Chces hrát s PC (A), nebo s jiným hráčem (N)")
  if volba == "A":
    cislicka = []
    kod = ""
    for i in range(10):
      cislicka.append(str(i))
    random.shuffle(cislicka)
    while cislicka[0] == 0:
      random.shuffle(cislicka)
    for i in range(4):
      kod += cislicka[i]
  else:
    kod = setup()
  pozdrav()
  play(kod, 0)

if __name__=="__main__":
    main()
=======
print("ahoj", "cau", sep= ",")
>>>>>>> main
