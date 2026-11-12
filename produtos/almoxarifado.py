# produtos/almoxarifado.py — a classe Almoxarifado guarda os produtos de uma unidade
class Almoxarifado:
 # Construtor: o almoxarifado nasce com o nome da unidade e sem produtos
 def __init__(self, unidade):
    self.unidade = unidade
    self.produtos = []
 # Guarda um objeto Produto no fim da lista
 def adicionar(self, produto):
    self.produtos.append(produto)

# conta quantos produto tao com quantidade zero (em falta)
    def contar_em_falta(self):
        total = 0 # começa o contador do zero
        for p in self.produtos: # passa por cada p que é um objeto Produto
            if p.situacao() == "Em falta":
                total = total + 1
        return total # devolve o total, nao da print

    # 1. buscar(codigo): procura na lista o produto com o codigo certo
    def buscar(self, codigo):
        for p in self.produtos:
            if p.codigo == codigo:
                return p # se acho devolve o produto
        return None # se nao acho devolve nada

    # 2. entrada(codigo, qtd): acha o produto e soma mais quantidade no estoque
    def entrada(self, codigo, qtd):
        produto = self.buscar(codigo)
        if produto is None:
            return False # se nao acho o produto retorna falso
        produto.entrada(qtd)
        return True # deu bom, retorna verdadeiro