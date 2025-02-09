import sqlite3
#a cima importamos a biblioteca sqlite3 para trabalhar com banco de dados


#definimos uma função chamada criar_banco(), que será responsavel por criar o banco de dados e as tabelas 
def criar_banco():
    
    #criamos uma conexão com o banco de dados. se o arquivo "cadastro.db" nao existir ele será criado automaticamente.
    conexao =  sqlite3.connect('cadastros.db')
    
    #um cursor que é um objeto que permite execuitar comandos SQL no banco de dados
    cursor  = conexao.cursor()

    #cria tabela "serviços" se ela ainda nao existir
    #essa tabela armanezrá informações sobre os clientes cadastrados
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS clientes (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        whatsapp TEXT NOT NULL,
                        endereco TEXT NOT NULL
                        )
                    """)
    #cria tabela "serviços" se ela ainda nao existir
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS servicos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,   
                        nome_servico TEXT NOT  NULL, 
                        valor REAL NOT NULL,
                        forma_pagamento TEXT NOT NULL,
                        data TEXT NOT NULL
                        
                        )
                    """)
    #cria a tabela "ordens_servico" que liga clientes e serviços em um historico de serviços prestados
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ordens_servico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        servico_id INTEGER NOT NULL, 
        FOREIGN KEY (cliente_id) REFERENCES clientes (id), 
        FOREIGN KEY (servico_id) REFERENCES servicos (id) 
                        )
                    """)
    #salvamos as alterações no banco de dados 
    conexao.commit()
    #fechamos a conexão com o banco de dados
    conexao.close()
    
    
    
if __name__ == '__main__':
    criar_banco() #chamamos a função para criar as tabelas no banco de dados
    print('Banco de dados criado com sucesso!') 
    #se esse arquivo for executado diretamente, (e nao importado como modulo), criamos o banco de dados