<<<<<<< HEAD
running=True


import random
def generate_code(delka,minimum,maximum):
    kod=''
    for i in range(0,delka):
        kod+=str(random.randint(minimum,maximum))
    return kod

def get_player_code():
    kod=input("zadej kod: ")
    return kod

correct_code=generate_code(4,1,8)
#?print(correct_code)
while running:
    player_code=get_player_code()
    bulls=0
    cows=0
    for i in range(len(player_code)):
        if correct_code[i]==player_code[i]:
            bulls+=1

    no_dupe_p_code="";
    for i in range(0,len(player_code)):
        if player_code[i] not in no_dupe_p_code:
            no_dupe_p_code+=player_code[i]
        else:
            pass
    for i in range(0,len(no_dupe_p_code)):
        if no_dupe_p_code[i] in correct_code:
            cows+=1
    cows=cows-bulls
    if player_code==correct_code:
        print("you won")
        running=False
    else:
        print(f"Bulls: {bulls}")
        print(f"Cows {cows}")
        print("try again: ")

=======
print("ahoj", "cau", sep= ",")
>>>>>>> main
