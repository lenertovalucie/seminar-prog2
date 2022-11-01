import random
game = 0
play = 1
while play != "n":
    game += 1
    if game != 1:
        print("")
        print("")
    include = ["0","1","2","3","4","5","6","7","8","9"]
    number1 = str(random.randint(1,9))
    include.remove(number1)
    number2 = str(random.choice(include))
    include.remove(number2)
    number3 = str(random.choice(include))
    include.remove(number3)
    number4 = str(random.choice(include))
    number = ""
    number += number1+number2+number3+number4

    print("super secret code: ",number)

    if game == 1:
        print("Bulls and cows")
    print("4-digit code. Take a guess!")
    bulls = 0
    cows = 0
    counter = 0
    while bulls != 4:
        counter += 1
        answer_number = int(input())
        answer = str(answer_number)
        if answer_number > 1000 and answer_number < 9999:
            answer1 = answer[0]
            answer2 = answer[1]
            answer3 = answer[2]
            answer4 = answer[3]
        else:
            answer1 = 1
            answer2 = 1
            answer3 = 1
            answer4 = 1
        while answer_number > 9999 or answer_number < 1000 or answer2 == answer1 or answer3 == answer2 or answer3 == answer1 or answer4 == answer3 or answer4 == answer2 or answer4 == answer1:
            print("Invalid code! Please pick a 4-digit code with no repeating numbers.")
            answer_number = int(input())
            answer = str(answer_number)
            if answer_number > 1000 and answer_number < 9999:
                answer1 = answer[0]
                answer2 = answer[1]
                answer3 = answer[2]
                answer4 = answer[3]
            else:
                answer1 = 1
                answer2 = 1
                answer3 = 1
                answer4 = 1

        bulls = 0
        cows = 0
        if answer1 == number1:
            bulls += 1
        if answer2 == number2:
            bulls += 1
        if answer3 == number3:
            bulls += 1
        if answer4 == number4:
            bulls += 1
        if answer1 == number2 or answer1 == number3 or answer1 == number4:
            cows += 1
        if answer2 == number1 or answer2 == number3 or answer2 == number4:
            cows += 1
        if answer3 == number1 or answer3 == number2 or answer3 == number4:
            cows += 1
        if answer4 == number1 or answer4 == number2 or answer4 == number3:
            cows += 1
        if bulls != 4:
            print(bulls," bulls,",cows," cows")

    print("Correct!")
    if counter == 1:
        print("First try!")
    else:
        print("You took ",counter," tries.")
    print("Play again? (y/n)")
    play = (str(input())).lower()
    while play != "y" and play != "n":
        print("Invalid choice!")
        play = (str(input())).lower()