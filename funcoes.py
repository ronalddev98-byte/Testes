import json


def salvar_dados(rendas, despesas):

    dados = {
        "rendas": rendas,
        "despesas": despesas
    }

    with open("dados.json", "w") as arquivo:

        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def carregar_dados():

    try:

        with open("dados.json", "r") as arquivo:

            dados = json.load(arquivo)

            return dados["rendas"], dados["despesas"]

    except FileNotFoundError:

        return [], []


def adicionar_renda(rendas, despesas):

    try:

        descricao = input("Descrição da renda: ")

        valor = float(input("Valor da renda: "))

        nova_renda = {
            "descricao": descricao,
            "valor": valor
        }

        rendas.append(nova_renda)

        salvar_dados(rendas, despesas)

        print("Renda cadastrada!")

    except ValueError:

        print("Digite apenas números")


def adicionar_despesa(rendas, despesas):

    try:

        descricao = input("Descrição da despesa: ")

        valor = float(input("Valor da despesa: "))

        nova_despesa = {
            "descricao": descricao,
            "valor": valor
        }

        despesas.append(nova_despesa)

        salvar_dados(rendas, despesas)

        print("Despesa cadastrada!")

    except ValueError:

        print("Digite apenas números")


def mostrar_saldo(rendas, despesas):

    total_rendas = 0

    for renda in rendas:
        total_rendas += renda["valor"]

    total_despesas = 0

    for despesa in despesas:
        total_despesas += despesa["valor"]

    saldo = total_rendas - total_despesas

    print(f"\nTotal rendas: R$ {total_rendas}")

    print(f"Total despesas: R$ {total_despesas}")

    print(f"Saldo atual: R$ {saldo}")


def mostrar_historico(rendas, despesas):

    print("\n===== RENDAS =====")

    for renda in rendas:

        print(
            f'{renda["descricao"]} - '
            f'R$ {renda["valor"]}'
        )

    print("\n===== DESPESAS =====")

    for despesa in despesas:

        print(
            f'{despesa["descricao"]} - '
            f'R$ {despesa["valor"]}'
        )


def mostrar_menu():

    print("\n1 - Adicionar renda")
    print("2 - Adicionar despesa")
    print("3 - Ver saldo")
    print("4 - Mostrar histórico")
    print("5 - Sair")

    