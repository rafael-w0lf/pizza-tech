import sqlite3
conexao = sqlite3.connect('tabela.db')
cursor = conexao.cursor()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS cardapio (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL
               )
                ''')
conexao.commit()
conexao.close()
print("Banco de dadaos e tabela criados com sucesso!")

def adicionar_pizza(nome, preco):
    conexao = sqlite3.connect('pizzaria.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO pizzas (nome, preco) VALUES (?, ?)", (nome, preco))
    conexao.commit()
    conexao.close()

    #pizzas salgadas
    adicionar_pizza("Mussarela", 39.90)
    adicionar_pizza("Calabresa", 42.90)
    adicionar_pizza("Portuguesa", 46.90)
    adicionar_pizza("Frango com Catupiry", 50.90)
    adicionar_pizza("Marguerita", 45.90)
    adicionar_pizza("Quatro Queijos", 52.90)
    adicionar_pizza("Cane Seca com Queijo", 50.90)
    adicionar_pizza("Atum com Cebola", 48.90)
    adicionar_pizza("Pepperoni", 53.90)

    #pizzas doces
    adicionar_pizza("Chocolate", 45.90)
    adicionar_pizza("Banana com Canela", 42.90)
    adicionar_pizza("Romeu e Julieta", 46.90)
    adicionar_pizza("brigadeiro", 47.90)
    adicionar_pizza("Nutella", 56.90)

    

    

