import random
number = []
number.append(random.randint(1,9))
for n in range(3):
    add = 0
    while add == 0:
        number_to_add = random.randint(0,9)
        if number_to_add not in number:
            number.append(number_to_add)
            add = 1
            
answer = 0
while answer == 0:
    bulls = 0
    bulls_pos = []
    cows = 0
    user_list = []
    user = input("Answer:")
    for n in range(4):
        user_list.append(int(str((user)[n])))
    for n in range(4):
        if number[n]==user_list[n]:
            bulls += 1
            bulls_pos.append(n)
        elif number[n] in user_list and user_list.index(number[n]) not in bulls_pos:
            cows +=1
    print(f"bulls:{bulls}")
    print(f"cows:{cows}")
    if bulls == 4:
        print("You have won!")
        answer = 1


        
        
    


