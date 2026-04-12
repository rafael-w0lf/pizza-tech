import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title = "Gerenciador Pizza-Tech"
    page.window_width = 450
    page.window_height = 700
    page.theme_mode = ft.ThemeMode.LIGHT

#manipular o banco de dados
def adicionar_pizza_ao_banco(nome, preco):
    conexao = sqlite3.connect('tabela.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO cardapio (nome, preco) VALUES (?, ?)', (nome, preco))
    conexao.commit()
    conexao.close()

#componentes de interface
    txt_nome = ft.TextField(label="Nome da Pizza", hint_text="Ex: Portuguesa")
    txt_preco = ft.TextField(label="Preço (R$)", keyboard_type=ft.KeyboardType.NUMBER)

    lista_pizzas = ft.Column(spacing=10, scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    #função que atualiza a lista na tela
    def  carregar_pizzas():
         lista_pizzas.controls.clear()
         conexao = sqlite3.connect('tabela.db')
         cursor = conexao.cursor()
         cursor.execute('SELECT nome, preco FROM cardapio ORDER BY id DESC')

         for nome, preco in cursor.fetchall():
                lista_pizzas.controls.append(
                     ft.ListTile(
                          title=ft.Text(nome),
                          subtitle=ft.Text(f"R$ {preco:.2f}"),
                          loading=ft.Icon(ft.icons.LOCAL_PIZZA, color="red")
                     )
                )
                conexao.close()
                page.update()

#função do botão cadastrar
def cadastrar_clicado(e):
    if txt_nome.value == "" or txt_preco.value == "":
         page.show_snack_bar(ft.SnackBar(ft.Text("Por favor, preencha todos os campos!")))
         return
    
    try:
         #salva no banco de dados
         adicionar_pizza_ao_banco(txt_nome.value, float(txt_preco.value.replace(',', '.')))

         #limpa os campos e avisa o usuário
         txt_nome.value = ""
         txt_preco.value = ""
         page.show_snack_bar(ft.Snackbar(ft.Text("Pizza cadastrada com sucesso!")))

         #atualiza a lista de pizzas na tela
         carregar_pizzas()
    except ValueError:
         page.show_snack_bar(ft.SnackBar(ft.Text("Erro: O preço deve ser um número.")))
         
    btn_cadastrar = ft.ElevatedButton(
        "Cadastrar Pizza",
        icon=ft.icons.ADD,
        on_click=cadastrar_clicado,
        style=ft.ButtonStyle(color="white", bgcolor="red")
    )
    
    #montagem da página
    page.add(
        ft.Text("Painel de Cadastro", 
style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        txt_nome,
        txt_preco,
        btn_cadastrar,
        ft.Divider(),
        ft.Text("Cardápio Atual:",
style=ft.TextThemeStyle.TITLE_MEDIUM),
        lista_pizzas
    )

    # carrega os dados assim que o app abre
    carregar_pizzas()

ft.app(target=main)
