# solicitacao.py — a classe SolicitacaoCompra: o pedido que vai para o setor de compras
# Cada mudança de status confere QUEM está mexendo. Os métodos devolvem None
# quando deu certo, ou um texto explicando por que foi recusado.
# Um recorte dos 10 status do sistema Almox, com os mesmos nomes
AGUARDANDO = "aguardando_aprovacao"
REPROVADO = "sem_aprovacao_gestor"
SOLICITADO = "solicitado" # aprovado e enviado para compras
RECEBIDO = "recebido"
ENTREGUE = "entregue"
CANCELADO = "cancelado"
# A ordem que o almoxarifado segue depois da aprovação
ANDAMENTO = [SOLICITADO, RECEBIDO, ENTREGUE]
ENCERRADOS = [ENTREGUE, CANCELADO]

class SolicitacaoCompra:
 # Construtor: o pedido nasce com número, unidade, quem pediu e quem aprova
 def __init__(self, numero, unidade, solicitante, supervisor):
    self.numero = numero
    self.unidade = unidade
    self.solicitante = solicitante # matrícula de quem abriu
    self.supervisor = supervisor # matrícula de quem aprova
    self.itens = []
    self.status = AGUARDANDO
    self.historico = []
    self._registrar(solicitante, "Solicitação aberta")
 # Guarda cada mudança: quem fez, para qual status e por quê
 def _registrar(self, quem, nota):
    self.historico.append({"status": self.status, "quem": quem, "nota": nota})
 # Acrescenta um item; só enquanto ninguém aprovou
 def adicionar_item(self, codigo, nome, quantidade):
    if self.status != AGUARDANDO:
        return "Depois de aprovada, a solicitação não recebe itens novos."
    if quantidade <= 0:
        return "A quantidade precisa ser maior que zero."
    self.itens.append({"codigo": codigo, "nome": nome, "quantidade": quantidade})
    return None
