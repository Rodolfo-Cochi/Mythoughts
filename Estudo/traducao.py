from Estudo.Classes.Calculos import *

try:
    Num1 = float(input("informe o primeiro valor: "))
    Num2 = float(input("Informe o segundo valor: "))
    Operacao = input("O que deseja fazer (+; -; /; *)")
except print("Eh obrigatorio os valores"):
    pass 

if Operacao == "+":
    resultado = Calculos.somar(Num1, Num2)
    print (resultado)

elif Operacao == "-":
    resultado = Calculos.subtrair(Num1, Num2)
    print(resultado)

elif Operacao == "*":
    resultado = Calculos.multiplicar(Num1, Num2)
    print(resultado)

elif Operacao == "/":
    resultado = Calculos.dividir(Num1,Num2)
    print(resultado)

elif Operacao == "^":
    resultado = Calculos.elevar(Num1,Num2)
    print(resultado)

else:
    print("Voce finalizou o programa")



