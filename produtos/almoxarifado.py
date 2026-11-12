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

    # 3. saida(codigo, qtd): tenta tirar produto do estoque se tiver bastante
    def saida(self, codigo, qtd):
        produto = self.buscar(codigo)
        if produto is None:
            return False # se o codigo nao existe da falso
        return produto.saida(qtd) # usa o metodo la do produto pra ver se consegue tirar

    # 4. listar(): devolve uma lista com o dicionario de cada produto
    def listar(self):
        lista = []
        for p in self.produtos:
            lista.append(p.listar_produtos())
        return lista

    # 5. solicitacao_compra(): pega so o que ta em Repor ou Em falta pra comprar mais
    def solicitacao_compra(self):
        pedido = []
        for p in self.produtos:
            situacao_atual = p.situacao()
            if situacao_atual == "Repor" or situacao_atual == "Em falta":
                pedido.append({
                    "codigo": p.codigo,
                    "nome": p.nome,
                    "situacao": situacao_atual
                })
        return pedido

    # 6. valor_estoque(): calcula quanto dinheiro tem parado no total somando qtd vezes preço
    def valor_estoque(self):
        total = 0.0
        for p in self.produtos:
            total = total + (p.quantidade * p.preco)
        return total

    # 7. para_dicionario(): monta um dicionario grandao com os dados da unidade inteira
    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }