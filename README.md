# Sistema de Controle de Estoque — Almoxarifado

- **Autor:** Arthur Moreira
- **Turma:** Técnico em Desenvolvimento de Sistemas (SENAI) Noturno

## Sobre o Projeto
Este projeto é um sistema de gerenciamento de estoque e controle de acessos em Python que gerencia produtos, almoxarifados, usuários, cargos e permissões de forma encapsulada e modularizada.

## Estrutura de Pastas
- `produtos/`: Contém as classes lógicas do domínio de mercadorias (`produto.py` e `almoxarifado.py`).
- `usuarios/`: Contém o mapeamento de papéis e permissões (`papeis.py`) e a classe de controle de perfis, senhas e segurança (`usuario.py`).
- `testes/`: Concentra os scripts de validação automatizada do sistema (`teste_almoxarifado.py` e `teste_usuario.py`).

## Como Rodar os Testes
Para executar os testes automatizados garantindo o reconhecimento correto dos pacotes via módulo, utilize os comandos na raiz do repositório:

```bash
python -m testes.teste_almoxarifado
python -m testes.teste_usuario

