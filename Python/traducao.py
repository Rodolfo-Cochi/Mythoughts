# function obrigatorio(parametro) { throw new Error(\`O parâmetro ${parametro} é obrigatório.\`); }

def obrigatorio(nome):
        return (print(nome))

try:
    obrigatorio("Rodolfo")
except print("O parametro nome eh obrigatorio"):
    pass

print("Testando so uma parada msm ")


listaNumero = [1,2,3,4,5]
i = 0
for numero in listaNumero:
    resultado = numero*i
    print(resultado)
    i+=1
else: 
    print("acabou a lista de numeros")


def somar(num1,num2):
    resultado = num1 + num2
    return resultado

def subtrair(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1,num2):
    resultado= num1*num2
    return resultado

def dividir(num1,num2):
    resultado = num1/num2
    return resultado


try:
    Num1 = float(input("informe o primeiro valor: "))
    Num2 = float(input("Informe o segundo valor: "))
    Operacao = input("O que deseja fazer (+; -; /; *)")
except print("Eh obrigatorio os valores"):
    pass 

numeros = [1,2,3,4,5]

if Operacao == "+":
    resultado = somar(Num1, Num2)
    print (resultado)

elif Operacao == "-":
    resultado = subtrair(Num1, Num2)
    print(resultado)

elif Operacao == "*":
    resultado = multiplicar(Num1, Num2)
    print(resultado)

elif Operacao == "/":
    resultado = dividir(Num1,Num2)
    print(resultado)



