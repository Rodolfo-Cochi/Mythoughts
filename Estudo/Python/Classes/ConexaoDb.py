import sqlite3
class Conexao:
    banco = sqlite3.connect("bancoTeste.db")               # Conectar com o DB                      
    cursor = banco.cursor()

    def criarNaTabela(cursor,nome):
        cursor.execute("CREATE TABLE "+nome+" (nome text,nota integer)")         # Criar Banco de Dados


    #Funcionando INSERT
    def addTabela(banco,cursor,nomeTabela,nomeJogo,nota): 
        cursor.execute("INSERT INTO "+nomeTabela+" VALUES('"+nomeJogo+"','"+str(nota)+"')")  # Inserir Dados no Banco
        banco.commit()             # Confirmar a Insercao no Banco

    #Funcionando SELECT
    def selecionarDados(cursor,nomeTabela):
        cursor.execute(f"SELECT * from {nomeTabela}")      # Selecionar Dados do Banco 
        print(cursor.fetchall())    # Printar oq foi selecionado

    #Funcionando DELETE
    def deletarDados(cursor,banco,nomeTabela):
        cursor.execute(f"DELETE from {nomeTabela}")   # Deletar conteudo do banco 
        banco.commit()      # Confirmar o Comando SQL no Banco

    #Funcionando UPDATE
    def alterarNome(cursor,banco,nomeTabela,novoJogo,antigoJogo):
        cursor.execute(f"UPDATE {nomeTabela} SET nome = '{novoJogo}' WHERE nome = '{antigoJogo}'") # Digitar Nome novo e de onde deseja
        banco.commit()  # Confirmar comando SQL no Banco

    # Testando 
    def alterarNotaDoJogo(cursor,banco,nomeTabela,nomeJogo,novaNota):
        cursor.execute(f"UPDATE {nomeTabela} SET nome = '{novoJogo}' WHERE nome = '{antigoJogo}'")

