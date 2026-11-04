# produtos/almoxarifado.py — a classe Almoxarifado guarda os produtos de uma unidade
class Almoxarifado:
 # Construtor: o almoxarifado nasce com o nome da unidade e sem produtos
 def __init__(self, unidade):
    self.unidade = unidade
    self.produtos = []
 # Guarda um objeto Produto no fim da lista
 def adicionar(self, produto):
    self.produtos.append(produto)