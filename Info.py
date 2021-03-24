def comparacao_salarios(funcionario1,funcionario2):     #Funcao que compara o salario de dois funcionarios
    if qnt_ganha(funcionario1) > qnt_ganha(funcionario2):
        return funcionario1
    elif qnt_ganha(funcionario1) < qnt_ganha(funcionario2):
        return funcionario2
    else:
        print("Nao trabalha aqui")

def qnt_ganha(nome):       #Funcao que calcula o salario baseado no nome do funcionario
        if nome in estagiarios:
            #print("Funcionario %s encontrado" % nome)
            return calculo_de_pagamento(40,18)
        
        elif  nome in efetivados:
            #print("Funcionario %s encontrado" % nome)
            return calculo_de_pagamento(50,22)
           
        else:
            print("nao trabalha aqui")

def addLista(cargo,nome_funcionario):
    if cargo == "estagiario":
       estagiarios.append(nome_funcionario)
       print(estagiarios)
    elif cargo == "efetivado":
       efetivados.append(nome_funcionario)
       print(efetivados)
    else:
        while cargo !="estagiario" or cargo != "efetivado":
              cargo = input("Digite o cargo corretamente:")
              break
        return addLista(cargo,nome_funcionario)
        

def addDic(nome):
    if nome in estagiarios or nome in efetivados:
        print("ta na lista")
        func_salario[nome] = qnt_ganha(nome)
        return func_salario
    else: 
        addLista(input("Cargo: "), nome)
        func_salario[nome] = qnt_ganha(nome)
        return func_salario
        
    
   
estagiarios = [ "Julia","Lucia","Guilherme","Bruno"]    #Criar lista de estagiarios
efetivados = ["Alexandre", "Fernando"]                  #Criar lista de efetivados
estagiario = "estagiario"                               #usar em add na lista de Estagiario
efetivado = "efetivado"                                 #usar para add na lista deEfetivado
errado = "nada"                                         #teste para erro
func_salario = {'Julia':10, 'Lucia':15}                                       #Criar dicionario
func_interesse = "Thiago"                               #Funcionario de interesse


def __init__(self):
    self

def acessar_nome(nome):
    print(func_salario[nome])


acessar_nome("Julia")















