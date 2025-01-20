from functools import reduce
import random

# lisik = [i for i in range(5)]
# lisik2 = [[i for i in range(5)],[i for i in range(5,10)],[i for i in range(10,15)]]
# print(lisik)
# listik = list(map(lambda x: x/2, lisik))
# print(listik)
# reducik = reduce(lambda x,y: x+y, lisik)
# print(reducik)
# reducik2 = list(map(lambda sublist :reduce(lambda x,y:x+y, sublist), lisik2))
# print(lisik2)
# print(reducik2)

# # two sum

# number = [ random.randint(-100,100) for i in range(100)]
number = [3,3]
print(number)
# target = random.randint(-100,100)
target = 6
print(target)
otvet = []
for i in range(len(number)):
    temp = target - number[i]
    if temp in number[i:len(number)-1]:
        otvet = [i, number.index(temp, i+1, len(number))]
        break
    else: 
        continue

print(otvet)
    