# controle_acesso.py — a classe ControleAcesso guarda os usuários e cuida do login
# É a mesma ideia da Almoxarifado: uma classe que guarda uma lista de objetos.
import secrets
from usuarios.papeis import papeis_validos
# A mesma mensagem para matrícula que não existe e senha errada:
# se fossem diferentes, daria para descobrir quais matrículas existem.
CREDENCIAL_INVALIDA = "Matrícula ou senha inválida."
class ControleAcesso:
 # Construtor: começa sem usuários e sem ninguém logado
 def __init__(self):
    self.usuarios = []
    self.sessoes = {} # token → matrícula de quem está logado
 # Devolve o Usuario com essa matrícula, ou None
 def buscar(self, matricula):
    for u in self.usuarios:
        if u.matricula == matricula:
            return u
    return None
