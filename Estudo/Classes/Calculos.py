class Calculos:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self,num1,num2):
        self.resultado = num1 + num2
        return self.resultado

    def subtrair(self,num1, num2):
        self.resultado = num1 - num2
        return self.resultado

    def multiplicar(self,num1,num2):
        self.resultado= num1*num2
        return self.resultado

    def dividir(self,num1,num2):
        self.resultado = num1/num2
        return self.resultado

    def elevar(self,num1,num2):
        self.resultado = num1**num2
        return self.resultado
