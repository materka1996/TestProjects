
NumbersList = [5,6,7,8,9,10,11,12,13,14,15]

print("Dlugosc listy: ",len(NumbersList))
del NumbersList[3]
print("Dlugosc listy: ",len(NumbersList))

for value in NumbersList:
    print(value)

if 9 in NumbersList:
    print("Wartosc 9 jest w zbiorze")

for value2 in NumbersList:
    print(value2 - 5)

for value3 in NumbersList:
    print(value3 / 3)


