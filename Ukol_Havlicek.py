
 

import math


def anagramy(*a):
    anagrams = []
    for i in a:
      anagrams.append(sorted(i))
      if sorted(i)!= anagrams[0]:
        return False
    return True 
      
      
 

print(anagramy("ahoj","hoja","hjoa"))



def delitel(a,b):
  return math.gcd(a,b)

print(delitel(120,60))


