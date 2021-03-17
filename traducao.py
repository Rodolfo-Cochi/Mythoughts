from Estudo.Python.Classes.Calculos import *

try:
    Num1 = float(input("Digite o numero: "))
    Num2 = float(input("Digite o numero: "))
    c = Calculos()
    Operacao = input("O que deseja fazer (+; -; /; *)")
except print("Eh obrigatorio os valores"):
    pass 


if Operacao == "+":
    resultado = c.somar(Num1,Num2)
    print (resultado)

elif Operacao == "-":
    resultado = c.subtrair(Num1, Num2)
    print(resultado)

elif Operacao == "*":
    resultado = c.multiplicar(Num1, Num2)
    print(resultado)

elif Operacao == "/":
    resultado = c.dividir(Num1,Num2)
    print(resultado)

elif Operacao == "^":
    resultado = c.elevar(Num1,Num2)
    print(resultado)

else:
    print("Voce finalizou o programa")



