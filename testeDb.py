from sqlite3.dbapi2 import connect
from Estudo.Python.Classes.Trabalho import *
from Estudo.Python.Classes.Funcionario import *
from Estudo.Python.Classes.Trabalho import *
from Estudo.Python.Classes.ConexaoDb import Conexao

# Conectividade Banco de Dados
db = Conexao.banco
cr = Conexao.cursor

# Variaveis de teste
nomeTabela = "jogos"
nomeJogo = "RE"
nomeJogoNovo = "DMC"
nota = 8

''' try:
    Conexao.criarTabela(cr,nomeTabela)    #Criar o Db
except:
    print("Algo deu errado")
 '''
#Conexao.addTabela(db,cr,nomeTabela,nomeJogo,nota)  # Adcionar jogo na tabela
Conexao.selecionarDados(cr,nomeTabela)  # selecionar e mostrar os dados selecionado do Db

#Conexao.alterarNome(cr,db,nomeTabela,nomeJogoNovo,nomeJogo) # Alterar nome de algum jogo no Db
Conexao.selecionarDados(cr,nomeTabela) # selecionar e mostrar os dados selecionado do Db

#Conexao.alterarNotaDoJogo(cr,db,nomeTabela,nomeJogo,novaNota=5) # Aterar nota de algum jogo
Conexao.selecionarDados(cr,nomeTabela) # selecionar e mostrar os dados selecionado do Db

#Conexao.deletarDados(cr,db,nomeTabela) # Deletar a tabela inteira (Por enquanto)
Conexao.selecionarDados(cr,nomeTabela) # selecionar e mostrar os dados selecionado do Db


