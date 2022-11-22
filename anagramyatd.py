def anagram(*args):
    """
    funkce vezme vsechny veci v args a sortne je a da je do noveho listu, ten pak zmeni na set (cimz znici duplikaty)
    """
    newlist=[]
    for i in args:
        newlist.append(''.join(sorted(i)))
    setik = set(newlist)
    if len(setik) == 1:
        return True
    else:
        return False

print(anagram("ahoj", "joha"))

import math
def greatestdiv(a: int, b: int) -> int:
    return math.gcd(a,b)