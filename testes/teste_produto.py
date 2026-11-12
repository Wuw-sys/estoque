from produtos.produto import Produto
from produtos.almoxarifado import Almoxarifado

p1 = Produto()
p1.nome = "Macarrão parafuso"
p1.quantidade = 5

p2 = Produto()
p2.nome = "Molho de tomate"
p2.quantidade = 3

print(p1.listar_produtos())
print(p2.listar_produtos())

p1.entrada(30)
print(p1.listar_produtos())

p1.retirada(10)
print(p1.listar_produtos())

if p1.retirada(100):
    print("Saída registrada")
else:
    print("Saída recusada")
    
print(p1.listar_produtos())