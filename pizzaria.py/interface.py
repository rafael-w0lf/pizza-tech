import flet as ft
import sqlite3


def criar_tabela():
    conexao = sqlite3.connect('tabela.db')
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pizzas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()


def adicionar_pizza_ao_banco(nome, preco):
    conexao = sqlite3.connect('tabela.db')
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO pizzas (nome, preco) VALUES (?, ?)",
        (nome, preco)
    )
    conexao.commit()
    conexao.close()


def main(page: ft.Page):
    page.title = "Gerenciador Pizza-Tech"
    page.window_width = 450
    page.window_height = 700
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    txt_nome = ft.TextField(label="Nome da Pizza")
    txt_preco = ft.TextField(label="Preço (R$)", keyboard_type=ft.KeyboardType.NUMBER)

    lista_pizzas = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, expand=True)

    def carregar_pizzas():
        lista_pizzas.controls.clear()

        conexao = sqlite3.connect('tabela.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, preco FROM pizzas ORDER BY id DESC")

        dados = cursor.fetchall()

        for nome, preco in dados:
            lista_pizzas.controls.append(
                ft.ListTile(
                    title=ft.Text(nome),
                    subtitle=ft.Text(f"R$ {preco:.2f}"),
                    leading=ft.Icon(ft.Icons.RESTAURANT),  # ✔️ corrigido aqui
                )
            )

        conexao.close()
        page.update()

    def cadastrar_clicado(e):
        if not txt_nome.value or not txt_preco.value:
            page.snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"))
            page.snack_bar.open = True
            page.update()
            return

        try:
            preco = float(txt_preco.value.replace(",", "."))
            adicionar_pizza_ao_banco(txt_nome.value, preco)

            txt_nome.value = ""
            txt_preco.value = ""

            page.snack_bar = ft.SnackBar(content=ft.Text("Pizza cadastrada com sucesso!"))
            page.snack_bar.open = True

            carregar_pizzas()
            page.update()

        except ValueError:
            page.snack_bar = ft.SnackBar(content=ft.Text("Preço inválido!"))
            page.snack_bar.open = True
            page.update()

    btn_cadastrar = ft.ElevatedButton(
        content=ft.Text("Cadastrar Pizza"),
        icon=ft.Icons.ADD,
        on_click=cadastrar_clicado,
        style=ft.ButtonStyle(color="white", bgcolor="red"),
    )

    page.add(
        ft.Text("Painel de Cadastro", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        txt_nome,
        txt_preco,
        btn_cadastrar,
        ft.Divider(),
        ft.Text("Cardápio Atual:", style=ft.TextThemeStyle.TITLE_MEDIUM),
        lista_pizzas,
    )

    carregar_pizzas()


criar_tabela()
ft.run(main)