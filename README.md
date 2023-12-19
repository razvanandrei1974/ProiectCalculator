# :pushpin:  ProiectCalculator

## Nume proiect : CalculatorApp

## Varianta de implementare : Principii OOP ( clase si obiecte )

### Nume fisier Python : calculator_simplu.py
[calculator_simplu](https://github.com/razvanandrei1974/ProiectCalculator/blob/ProiecteTA/calculator_simplu.py)

## Pasi :

## 1. Initiem clasa Calculator
    class Calculator:
    pass

## 2. Initiem clasa CalculatorSimplu  
    class CalculatorSimplu():

### In cadrul clasei initiem functiile necesare operatiilor aritmetice : 

- Initiem functia ADUNARE :heavy_plus_sign:
* Initiem functia SCADERE :heavy_minus_sign:
+ Initiem functia INMULTIRE :heavy_multiplication_x:
- Initiem functia IMPARTIRE :heavy_division_sign:   


   def adunare(x, y): #Initiem functia de adunare
        return x + y

    def scadere(x, y): # initiem functia de impartire
        return x - y

    def inmultire(x, y): # Initiem functia de inmultire
        return x * y

    def impartire(x, y): # Initiem functia de scadere
        return x / y
  
### :pushpin: Cu ajutorul functiei "Print" afisam in consola si alegem de la tastatura tipul operatiei pe care dorim sa o efectuam
    print("Alegeti operatia :")
    print("1.Adunare")
    print("2.Scadere")
    print("3.Inmultire")
    print("4.Impartiere")

### :pushpin: Cu ajutorul functiei "Input" afisam in consola si sciem de la tastatura numerele pe care asupra carora dorim sa aplicam opeartia aritmetica aleasa anterior.
      if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Introduceti primul numar: "))
                num2 = float(input("Introduceti al doilea numar: "))

### :pushpin: Cu ajutorul conditionalului "If", "Elif" si "Else" executam operatiile aritmetice.
      if choice == '1':
                print(num1, "+", num2, "=", adunare(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", scadere(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", inmultire(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", impartire(num1, num2))


##  In consola va fi afisat rezultatul 
    

### :pushpin: In cazul in care dorim sa efectuam o alta operatie aritmetica vom alege acest lucru de la tastatura cu ajutorul functiei "Input" 
    next_calculation = input("Doriti executarea unei noi operatii? (Da/Nu): ")
            if next_calculation == "Nu":
                break
        else:
            print("Ati introdus un numar invalid")


