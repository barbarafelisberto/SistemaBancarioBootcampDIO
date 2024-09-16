# 🏦 Sistema Bancário em Python

Este projeto faz parte do bootcamp de Ciência de Dados da [DIO.me](https://www.dio.me/). O objetivo é desenvolver um sistema bancário simples em Python com três operações principais: **Depósito**, **Saque** e **Extrato**.

## 📋 Descrição do Desafio

Você foi contratado por um grande banco para desenvolver a primeira versão de seu novo sistema bancário. Para isso, deverá implementar operações básicas de depósito, saque e extrato, considerando algumas regras de negócio.

---

### ⚙️ Funcionalidades Implementadas

1. **Depósito**: O sistema permite realizar depósitos de valores positivos. Todos os depósitos são armazenados e exibidos no extrato.
2. **Saque**: É possível realizar até 3 saques diários, com limite de R$ 500,00 por saque. O sistema checa se o saldo é suficiente antes de permitir o saque.
3. **Extrato**: O extrato lista todos os depósitos e saques realizados, além de exibir o saldo atual. Se não houver movimentações, o sistema informa que não foram realizadas operações.

---

### 📊 Regras de Negócio

| Operação    | Regras                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------|
| **Depósito**| - Permite depósitos de valores positivos<br>- Armazenados e exibidos no extrato                 |
| **Saque**   | - Limite de 3 saques por dia<br>- Limite máximo de R$ 500,00 por saque<br>- Saldo insuficiente impede saque |
| **Extrato** | - Lista todos os depósitos e saques<br>- Exibe o saldo final<br>- Exibe mensagem caso não haja movimentações |

---
###  Projeto de melhoria

No futuro, a minha intenção é desenvolver uma interface gráfica para esse projeto, visando melhorar a utilização e visualização do sistema para o usuário final. Podendo usar alguma biblioteca em Python como a Tkinter ou PySimpleGui.
---
### 📂 Estrutura do Projeto

```bash
sistema-bancario/
├── SistemaBancarioDIO.py          # Código principal do sistema bancário
└── README.md         # Instruções e descrição do projeto
