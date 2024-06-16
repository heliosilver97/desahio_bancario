# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:46:52 2024

@author: Helio
"""

menu =  """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> 

"""

saldo = 0 
limite = 500
extrato =" "
numero_saque = 0
LIMITE_SAQUE = 3 

# Laço de repetição

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito:")
        valor = float(input("Digite o valor que deseja depositar: "))
        
        # Aqui estou armazenando o valor depositado, para assim poder mostrar no Extrato.
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R${valor:.2f}\n"  
   
        else:
            print("Erro, valor informado inválido!")
    
    elif opcao == "s":
        print("Saque")

        valor = float(input("Qual o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print(f"Erro, saldo insuficiente!\n")

        elif excedeu_limite:
            print("Erro, limite de saque excedido!")

        elif excedeu_saques:
            print("Erro, limite de saques diário excedido!")

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque += 1
        
        else:
            print("Erro, valor inválido!")
            

    elif opcao == "e":
        print("********** Extrato *************")
        print("Não houve movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("********************************")

    elif opcao == "q":
        break

    else:
        print("Operação invalidada, selecione outra opção!")
