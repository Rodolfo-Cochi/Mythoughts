import sqlite3
class Conexao:
    def __init__(self):
        self

    def connect(nome):
        banco = sqlite3.connect(nome +".db")               # Conectar com o DB                      
        return banco

    def criarCursor(banco):
        cursor = banco.cursor()       # Possibilita manipulacao do banco
        return cursor

    




    
# cursor.execute("CREATE TABLE jogos (nome text,nota integer)")         # Criar Banco de Dados



#cursor.execute("INSERT INTO jogos VALUES('"+nomeJogo+"',"+str(nota)+")")     # Inserir Dados no Banco
#banco.commit()  # Confirmar a Insercao no Banco

#cursor.execute("SELECT * from jogos WHERE nota >= 8")   # Selecionar Dados do Banco 
#print(cursor.fetchall()) # Printar oq foi selecionado 

#cursor.execute("DELETE from jogos")   # Deletar conteudo do banco 
#banco.commit()  # Confirmar o Comando SQL no Banco

#cursor.execute("SELECT * from jogos")   # Selecionar Dados do Banco 
#print(cursor.fetchall())    # Printar Selecionado

