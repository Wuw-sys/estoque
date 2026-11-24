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

#Guarda um usuário novo; False se a matrícula já existe
 def cadastrar(self, usuario):
        achado = self.buscar(usuario.matricula)
        if achado is not None:
            return False
        self.usuarios.append(usuario)
        return True

    # Confere matrícula, senha e situação ativa; gera token de 32 chars hex (16 bytes)
 def entrar(self, matricula, senha):
        usuario = self.buscar(matricula)
        if usuario is None:
            return None
        if usuario.situacao != "ativo":
            return None
        if not usuario.conferir_senha(senha):
            return None

        token = secrets.token_hex(16)
        self.sessoes[token] = usuario.matricula
        return token

 # Devolve o Usuario dono do token, ou None se não estiver logado
 def usuario_logado(self, token):
        matricula = self.sessoes.get(token)
        if matricula is None:
            return None
        return self.buscar(matricula)

    # Encerra a sessão apagando o token; True se existia, False se não existia
 def sair(self, token):
        if token not in self.sessoes:
            return False
        del self.sessoes[token]
        return True

    # Altera os papéis de um usuário; retorna None se ok ou mensagem com o motivo
 def mudar_papeis(self, quem, matricula, papeis):
        if not quem.pode("mudar_papeis"):
            return "Você não tem permissão para mudar papéis."

        alvo = self.buscar(matricula)
        if alvo is None:
            return "Usuário não encontrado."

        if len(papeis) == 0:
            return "Escolha pelo menos um papel."

        validos = papeis_validos()
        for papel in papeis:
            if papel not in validos:
                return f"Papel inválido: {papel}"

        alvo.papeis = list(papeis)
        return None