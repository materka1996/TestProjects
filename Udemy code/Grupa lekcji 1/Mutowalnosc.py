
#NieMutowalne(zmiana tworzy nowy element): int, float, bool, str, tuple. frozenset
#Mutowalne(zmiana nie tworzy elementu): listy, zbiory, dict(slownik)

a = 10
addr1 = id(a)

a = a + 1

addr2 = id(a)
print(addr1)
print(addr2)

print (addr1 == addr2)

list = [0 ,1, 2]
addr1 = id(list)    

list += [3,4,5]
addr2 = id(list)
print (addr1 == addr2)