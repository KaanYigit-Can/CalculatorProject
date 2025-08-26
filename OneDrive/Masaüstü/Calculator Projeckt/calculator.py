print("Welcome to the Calculator!")
print("Available operations: + - * / **")

def topla(sayi1, sayi2):
    return sayi1 + sayi2

def çıkar(sayi1, sayi2):
    return sayi1 - sayi2

def çarp(sayi1, sayi2):
    return sayi1 * sayi2

def böl(sayi1, sayi2):
    if sayi2 == 0:
        return "Cannot divide by zero"
    return sayi1 / sayi2

def üs_al(sayi1, sayi2):
    return sayi1 ** sayi2

def devam():
    while True:
        try:
            devam = int(input("Do you want to continue? 1 Yes 2 No: "))
            if devam == 2:
                print("Exiting...")
                return False
            elif devam == 1:
                print("Welcome back!")
                return True
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

cevap = None
while True:
    islem = input("Which operation would you like to perform? (+ - * / **) or C to Clear: ")
    if islem.upper() == "C":
        cevap = None
        print("Calculator cleared.")
        continue
    if islem not in ["+", "-", "*", "/", "**"]:
        print("Invalid operation")
        continue
    if cevap is None:
        while True:
            try:
                sayi1 = float(input("Please enter the first number: "))
                break
            except ValueError:
                print("Invalid entry. Please enter a number.")
    else:
        sayi1 = cevap
        print("Current result:", cevap)
    while True:
        try:
            sayi2 = float(input("Please enter the second number: "))
            break
        except ValueError:
            print("Invalid entry. Please enter a number.")
    if islem == "+":
        sonuç = topla(sayi1, sayi2)
    elif islem == "-":
        sonuç = çıkar(sayi1, sayi2)
    elif islem == "*":
        sonuç = çarp(sayi1, sayi2)
    elif islem == "/":
        sonuç = böl(sayi1, sayi2)
    elif islem == "**":
        sonuç = üs_al(sayi1, sayi2)
    cevap = sonuç
    print("conclusion:", cevap)
    if not devam():
        break