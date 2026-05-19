from funcoes import *

rendas, despesas = carregar_dados()

###Loop Principal###
while True:

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        adicionar_renda(rendas, despesas)

    elif opcao == "2":

        adicionar_despesa(rendas, despesas)

    elif opcao == "3":

        mostrar_saldo(rendas, despesas)

    elif opcao == "4":

        mostrar_historico(rendas, despesas)

    elif opcao == "5":

        print("Saindo do sistema")

        break

    else:

        print("Opção inválida")