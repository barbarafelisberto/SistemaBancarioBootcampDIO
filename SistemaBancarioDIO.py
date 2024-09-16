print("SISTEMA BANCÁRIO - BOOTCAMP DIO")
#SACAR = Limite de 3 saques diarios de 500 reais cada um, caso o usuario não tenha limite em conta o sistema deve mostrar
#uma mensagem informando não ser possivel efetuar o saque por falta de saldo. Todos os saques devem ser armazenados 
#em uma variável e exibido no extrato
#DEPOSITAR = Todos os depositos precisam ser guardados em uma variavel e ser exibido no extrato
#EXTRATO = Listar todos os saques e depositos realizados, os valores devem ser exibidos no formato R$XXX.XX

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
Limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
imprimir_extrato = []
while True:
    opcao = input(menu)

    if opcao == 'd':
        print("Depositar")
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"
            print(f"\nValor de R$ {valor} depositado com sucesso!")

        else:
            print("Valor inválido para depósito.")
    
    elif opcao == 's':
        print("Sacar")
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor > saldo:
            print("Você não pode sacar esse valor, tente novamente")
        
        elif excedeu_saques:
            print("Você excedeu a quantidade limite de 3 saques.")

        elif valor > 500:
            print("O seu limite é de R$500,00 por saque. Informe um valor menor")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(saldo)
            print("Saque realizado com sucesso")
            
    elif opcao == 'e':
        print("\n ============EXTRATO============ ")
        if not extrato:

            print("Não foram realizadas movimentações.")
        else:
            print(f"Seu extrato é: R$ {extrato}")
            print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n =============================== ")
        print(imprimir_extrato)
        print("Extrato")
        
    
    elif opcao == 'q':
        print("Agradecemos por confiar em nosso sistema. Até a próxima!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")