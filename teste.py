from sqlite3.dbapi2 import connect
from Estudo.Python.Classes.Trabalho import *
from Estudo.Python.Classes.Funcionario import *
from Estudo.Python.Classes.ConexaoDb import *


banco = Conexao.connect("bancoTeste")
cursor = Conexao.criarCursor(banco)



''' credito = Trabalho("credito",8,15)
f1 = Funcionario("Rodolfo", credito)

print(f1.getNome())
print(f1.getTrabalho())
print(f1.calcularSalario()) '''

