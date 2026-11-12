import mysql.connector
from mysql.connector import Error

def conectar():
    try: #teste executar
        conexao = mysql.connector.connect(
        host="localhost", # endereço, nesse caso é localhost, que está na minha máquina
        user="root", # usuário
        password="senai", # senha
        database="estodolist" # database criado anteriormente
        )

        cursor = conexao.cursor(dictionary=True) # dictionary=True devolve as informações no formato Dict
        # retorna duas informações: conexão e cursor
        return conexao, cursor
    
    except Error as erro: #erro
        print(f"ERRO! Falha ao se conectar com o banco de dados: {erro}")
        return None, None

#esse código se conecta com o banco de dados e o cursor é o operador que vai manipular o banco de dados 
# quando for fazer o crud(cadastrar, vizualizar, editar, excluir), temos que abrir a porta, deixar o cursor entrar, tirar o curso, fechar a porta 

# FUNÇÃO INSERIR TAREFA --------------------------
def inserir_tarefa(nome_tarefa,descricao,categoria,data_prazo,prioridade):
    conexao, cursor = conectar() # se conectar com o db

    # verifica se a conexão funcionou 
    if conexao is None:
        return False 

    try:
        # %s = SQL parametrizado para evitar SQL injection
        sql = "INSERT INTO tarefa (nomeTarefa,descricao,categoria,dataPrazo,prioridade) VALUES (%s, %s, %s, %s, %s)"
        # executa o SQL parametrizado e passa os parâmetros da função
        cursor.execute(sql,(nome_tarefa,descricao,categoria,data_prazo,prioridade))
        # confirma as alterações
        conexao.commit()
        # retornar TRUE para a função principal
        return True

    except Error as erro:
        print(f"ERRO! Falha ao inserir a tarefa: {erro}")
        return False
    
    finally: #encerra dando certo ou não
        cursor.close()
        conexao.close()

# ------------------------------------------------------------
#retorna todas as tarefas cadastradas no banco de dados
def consultar_tarefas():

    #chama a função conectar
    conexao, cursor = conectar() 

    # verificar se a conexão falhou 
    if conexao is None:
        return [] # lista vazia 

    try: # tente executar o comando sql
        # selecione todas as colunas da(origem) tabela tarefa
        sql = """
            SELECT 
                idTarefa AS idtarefa,
                dataPrazo AS data_prazo,
                nomeTarefa AS nome_tarefa,
                status,
                descricao,
                categoria,
                prioridade
            FROM tarefa
            """
        
        # executa o comando da variável SQL
        cursor.execute(sql)

        # buscar todas as linhas da consulta executada
        tarefas = cursor.fetchall()

        # retorna para a programação principal as tarefas
        return tarefas # lista de dicionários (DICT)
        
    except Error as erro: # se der errado
        print(f"ERRO! Falha ao listar as tarefas: {erro}")
        return # retorna lista vazia em caso de erro 

    finally: # finalize dando certo ou errado
        cursor.close() # encerra o cursor
        conexao.close() # encerra a conexão

# ---------------------------------------------------
# essa função marca como concluída a tarefa indicada
def concluir_tarefa(idtarefa):
    conexao, cursor = conectar()

    if conexao is None:
        return False 

    try:
        sql = "UPDATE tarefa SET status = 'Concluída' WHERE idTarefa = %s"
        cursor.execute(sql,(idtarefa,))
        conexao.commit() # confirma a alteração nos dados 

        return True 

    except Error as erro:
        print(f"ERRO! Falha ao concluir a tarefa: {erro}")
        return False # retorna Falso em caso de erro 

    finally:
        cursor.close()
        conexao.close()

# ----------------------------------------------------
# essa função irá EDITAR as informações da tarefa indicada
def alterar_tarefa(idtarefa,nome_tarefa,descricao,categoria,data_prazo,prioridade):
    conexao, cursor = conectar()

    if conexao is None:
        return False 

    try:
        sql = "UPDATE tarefa SET nomeTarefa = %s, descricao = %s, categoria = %s, dataPrazo = %s, prioridade = %s WHERE idTarefa = %s"
        cursor.execute(sql,(nome_tarefa, descricao, categoria, data_prazo, prioridade, idtarefa))
        conexao.commit() # confirma a alteração nos dados 

        return True 

    except Error as erro:
        print(f"ERRO! Falha ao editar a tarefa: {erro}")
        return False # retorna Falso em caso de erro 

    finally:
        cursor.close()
        conexao.close()

# ----------------------------------------------------
# essa função irá EXCLUIR as informações da tarefa indicada
def apagar_tarefa(idtarefa):
    conexao, cursor = conectar()

    if conexao is None:
        return False 

    try:
        sql = """
        DELETE FROM tarefa WHERE idTarefa = %s
        """
        cursor.execute(sql,(idtarefa,))
        conexao.commit() # confirma a exclusão nos dados 

        return True 

    except Error as erro:
        print(f"ERRO! Falha ao excluir a tarefa: {erro}")
        return False # retorna Falso em caso de erro 

    finally:
        cursor.close()
        conexao.close()