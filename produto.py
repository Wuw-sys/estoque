class Produto:
    def _init_(self, nome=None, preco=0,quantidade=0,categoria=None,peso=0,codigo=None):
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade
        self.categoria=categoria
        self.peso=peso
        self.codigo=codigo
        
    def situacao(self):
        if self.quantidade == 0:
            return "Em falta"
        elif self.quantidade < 8:
            return "Repor"
        else:
            return "Ok"
    def listar_produtos (self):
        return{
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "categoria": self.categoria,
            "peso": self.peso,
            "codigo": self.codigo
        }