class CalculatorSimplu():

    def adunare(x, y): #Initiem functia de adunare
        return x + y

    def scadere(x, y): # initiem functia de impartire
        return x - y

    def inmultire(x, y): # Initiem functia de inmultire
        return x * y

    def impartire(x, y): # Initiem functia de scadere
        return x / y

    print("Alegeti operatia :")
    print("1.Adunare")
    print("2.Scadere")
    print("3.Inmultire")
    print("4.Impartiere")

    while True:

        choice = input("Alegeti optiunea(1/2/3/4): ")       # Folosim date introduse de utilizator

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Introduceti primul numar: "))
                num2 = float(input("Introduceti al doilea numar: "))
            except ValueError:
                print("Ati introdus un numar nevalid. Va rog introduceti un numar valid.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", adunare(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", scadere(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", inmultire(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", impartire(num1, num2))


            next_calculation = input("Doriti executarea unei noi operatii? (Da/Nu): ")
            if next_calculation == "Nu":
                break
        else:
            print("Ati introdus un numar invalid")