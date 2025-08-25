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
        devam = int(input("Do you want to continue? 1 Yes 2 No: "))
        if devam == 2:
            print("Exiting...")
            return False
        elif devam == 1:
            print("Welcome back!")
            return True
while True:
    islem = input("Which operation would you like to perform? + - * / **: ")
    if islem not in ["+", "-", "*", "/", "**"]:
        print("Invalid operation")
        continue
    else:
        try:
            sayi1 = float(input("Please enter the first number: "))
        except ValueError:
            print("Invalid entry. Please enter a number.")
            continue

        try:
            sayi2 = float(input("Please enter the second number: "))
        except ValueError:
            print("Invalid entry. Please enter a number.")
            continue



        if islem == "+":
            print("conclusion:", topla(sayi1, sayi2))
        elif islem == "-":
            print("conclusion:", çıkar(sayi1, sayi2))
        elif islem == "*":
            print("conclusion:", çarp(sayi1, sayi2))
        elif islem == "/":
            print("conclusion:", böl(sayi1, sayi2))
        elif islem == "**":
            print("conclusion:", üs_al(sayi1, sayi2))
        else:       
            print("Invalid operation")
            continue
        if not devam():
            break
