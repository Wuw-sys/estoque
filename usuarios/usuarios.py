import hashlib
import secrets
from usuarios.papeis import PERMISSOES

class Usuario:
    # Construtor: matrícula, nome, senha e a lista de papéis
    def __init__(self, matricula, nome, senha, papeis, supervisor=None):
        self.matricula = matricula
        self.nome = nome
        self.papeis = papeis  # ex.: ["solicitante", "supervisor"]
        self.supervisor = supervisor  # matrícula de quem aprova os pedidos dele
        self.situacao = "ativo"  # pendente, ativo, recusado ou inativo
        
        # O _ na frente avisa: atributo interno, ninguém de fora mexe
        self._sal = secrets.token_hex(8)
        self._senha_hash = self._resumir(senha)

    # Transforma a senha em um resumo que não dá para desfazer
    def _resumir(self, senha):
        texto = (self._sal + senha).encode("utf-8")
        return hashlib.sha256(texto).hexdigest()

    # True se a senha digitada bate com a guardada
    def conferir_senha(self, senha):
        return self._resumir(senha) == self._senha_hash

    # True se a pessoa tem esse papel
    def tem_papel(self, papel):
        return papel in self.papeis

    # 1. pode(permissao): confere se algum cargo tem a permissão e se o usuário está ativo
    def pode(permissao):
        # Nota: preenchido logo abaixo na estrutura correta do método da instância
        pass

    # 1. (Implementação correta)
    def pode(self, permissao):
        # Se a situação não for ativa, barra qualquer permissão
        if self.situacao != "ativo":
            return False
        
        # Varre cada papel que a pessoa possui
        for papel in self.papeis:
            # Verifica se o papel existe no dicionário oficial de permissões
            if papel in PERMISSOES:
                # Se a permissão procurada estiver na lista daquele papel, retorna True
                if permissao in PERMISSOES[papel]:
                    return True
        return False

    # 2. permissoes(): junta todas as permissões dos cargos sem repetir nenhuma
    def permissoes(self):
        lista_permissoes = []
        for papel in self.papeis:
            if papel in PERMISSOES:
                for p in PERMISSOES[papel]:
                    # Adiciona apenas se já não estiver na lista para evitar duplicadas
                    if p not in lista_permissoes:
                        lista_permissoes.append(p)
        return lista_permissoes