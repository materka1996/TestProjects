
num = 0 
operation = None
reset = True
result = None
calcOperations = ["+","-","*","/","**",]

while True:
    if reset == True:
        num = int( input("Wpisz pierwsza liczbe: ") )
        reset = False

    operation = input("Podaj operacje arytmetyczna: " + str(calcOperations) + "lub exit jeśli koniec lub reset: ")

    if operation == "exit": break
    if operation == "reset":
        reset = True
        continue

    if not operation in calcOperations:
        print("Wprowadzona zostałą błędna operacja")
        continue

    secondNum = int(input("Wprowadz druga liczbe: "))

    if operation == "+":
        result = num + secondNum

    if operation == "-":
        result = num - secondNum

    if operation == "/":
        result = num / secondNum

    if operation == "*":
        result = num * secondNum
    
    if operation == "**":
        result = num ** secondNum

    print("Wynik operacji " + str(num) + " " + operation + " " + str(secondNum) + " = " + str(result))

    num = result
    result = None