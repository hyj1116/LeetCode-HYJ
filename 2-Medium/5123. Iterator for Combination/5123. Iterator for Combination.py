from itertools import permutations


characters = 'abc'
combinationLength = 2
chars = list(characters)
print(chars)
perm = []
for i in list(  (chars, combinationLength)):
    perm.append(i)

print(perm)
print(perm.pop())
