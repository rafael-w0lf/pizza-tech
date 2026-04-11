from datetime import datetime

def sugerir_combo():
    dia_semana = datetime.now().weekday() # 0 = Segunda-feira, 6 = Domingo

    combos = {
        0: "Segunda Light: Pizza Margherita + Suco Natural",
        1: "Terça em Dobro: Compre uma Calabresa e ganhe outra",
        2: "Quarta: Pizza Quatro Queijos + Refrigerante 2L",
        3: "Quinta Recheada: Pizza Frango com Catupiry + Borda recheada",
        4: "Sextou: Desconto de 20% na Pizza de Atum com Cebola",
        5: "Sábado em família: Combo família - 2 Pizzas Grandes + 1 Refrigerante 2L",
        6: "Domingo Kids: Pizza Doce Grátis na compra de uma salgada"
    }

    return combos.get(dia_semana, "Confira nossas ofertas no balcão!")
print(f"Sugestão de hoje: {sugerir_combo()}")