from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def calculate(self):
        pass
num1 = 10
num2 = 6

class Adunare(Calculator):
     def calculate(self):
         return (f'Operatia de adunare are rezultatul {num1 + num2} ')

class Scadere(Calculator):
    def calculate(self):
        return (f'Operatia de scadere are rezultatul {num1 - num2} ')

class Inmultire(Calculator):
    def calculate(self):
        return (f'Operatia de inmultire are rezultatul {num1 * num2} ')

class Impartire(Calculator):
    def calculate(self):
        return (f'Operatia de impartire are rezultatul {num1 / num2} ')


adunare1 = Adunare()
print(adunare1.calculate())

scadere1 = Scadere()
print(scadere1.calculate())

inmultire1 = Inmultire()
print(inmultire1.calculate())

impartire1 = Impartire()
print(impartire1.calculate())