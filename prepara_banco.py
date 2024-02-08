import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
conn = None  # Definindo a variável conn fora do bloco try


try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

if conn:
    cursor = conn.cursor()

    cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

    cursor.execute("CREATE DATABASE `jogoteca`;")

    cursor.execute("USE `jogoteca`;")

    # criando tabelas
    TABLES = {}
    TABLES['Jogos'] = ('''
        CREATE TABLE `jogos` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(50) NOT NULL,
        `categoria` varchar(40) NOT NULL,
        `console` varchar(20) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

    TABLES['Usuarios'] = ('''
        CREATE TABLE `usuarios` (
        `nome` varchar(20) NOT NULL,
        `nickname` varchar(8) NOT NULL,
        `senha` varchar(100) NOT NULL,
        PRIMARY KEY (`nickname`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

    for tabela_nome in TABLES:
        tabela_sql = TABLES[tabela_nome]
        try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Já existe')
            else:
                print(err.msg)
        else:
            print('OK')

    # Restante do código...

    # commitando se não nada tem efeito
    conn.commit()

    cursor.close()
    conn.close()
