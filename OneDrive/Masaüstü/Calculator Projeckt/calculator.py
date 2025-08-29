import math

print("Welcome to the Calculator!")
print("Available operations: + - * / ** √ % log sin cos tan")

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

def sqrt(sayi1):
    if sayi1 < 0:
        return "Cannot take the square root of a negative number"
    return sayi1 ** 0.5

def yüzde(sayi1, sayi2):
    return(sayi1 * sayi2) / 100

def logaritma(sayi, taban=math.e):
    if sayi <= 0:
        return "Logarithm undefined for non-positive numbers"
    if taban <= 0 or taban == 1:
        return "Logarithm base must be positive and not equal to 1"
    return math.log(sayi, taban)

def sin(sayi):
    return math.sin(sayi)

def cos(sayi):
    return math.cos(sayi)

def tan(sayi):
    return math.tan(sayi)

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
    islem = input("Which operation would you like to perform? (+ - * / ** √ % log sin cos tan) or C to Clear: ")
    if islem.upper() == "C":
        cevap = None
        print("Calculator cleared.")
        continue
    if islem not in ["+", "-", "*", "/", "**", "√", "%", "log", "sin", "cos", "tan"]:
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

    if islem == "√":
                    sonuç = sqrt(sayi1)
                    print("Current result:", sonuç)
                    cevap = sonuç
                    if not devam():
                        break
                    continue
    
    elif islem == "log":
                taban = input("Enter the base for logarithm (default is e): ")
                taban = float(taban) if taban != "" else math.e
                sonuç = logaritma(sayi1, taban)
                print("Current result:", sonuç)
                cevap = sonuç
                if not devam():
                    break
                continue

    elif islem == "sin":
                sonuç = sin(sayi1)
                print("Current result:", sonuç)
                cevap = sonuç
                if not devam():
                    break
                continue

    elif islem == "cos":
                sonuç = cos(sayi1)
                print("Current result:", sonuç)
                cevap = sonuç
                if not devam():
                    break
                continue

    elif islem == "tan":
                sonuç = tan(sayi1)
                print("Current result:", sonuç)
                cevap = sonuç
                if not devam():
                    break
                continue

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
    elif islem == "%":
        sonuç = yüzde(sayi1, sayi2)

    print("Current result:", sonuç)
    cevap = sonuç

    if not devam():
        break