import random

# secret = str(random.randint(1000, 9999))
# sec0 = int(secret[0])
# sec1 = int(secret[1])
# sec2 = int(secret[2])
# sec3 = int(secret[3])

# if sec0 == sec1 or sec2 or sec3:
#     secret = str(random.randint(1000, 9999))
#     sec0 = int(secret[0])
#     sec1 = int(secret[1])
#     sec2 = int(secret[2])
#     sec3 = int(secret[3])

sec0 = random.randint(1,9)
sec1 = sec0
while sec1 != sec0:
    sec1 = random.randint(0,9)
sec2 = sec1
while sec2 != sec1 or sec2 == sec0:
    sec2 = random.randint(0,9)
sec3 = sec2
while sec3 != sec2 or sec3 == sec1 or sec3 == sec0:
    sec3 == random.randint(0,9)

print(sec0, sec1, sec2, sec3)