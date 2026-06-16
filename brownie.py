import json
import os

ARQUIVO_PEDIDOS = "pedidos.json"

def salvar_pedidos(pedidos):
    with open(ARQUIVO_PEDIDOS, "w", encoding="utf-8") as arquivo:
        json.dump(pedidos, arquivo, ensure_ascii=False, indent=4)

def carregar_pedidos():
    if os.path.exists(ARQUIVO_PEDIDOS):
        with open(ARQUIVO_PEDIDOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def adcionar_pedido():
    pedidos = carregar_pedidos()
    nome = input ("digite o nome do cliente: ")
    print("escolha o doce:")
    print("1- Brownie")
    print("2- palha italiana")
    print("3- outro")
    escolha = input("digite a opção desejada: ")
    match escolha:
        case "1":
            doce = "Brownie"
            brownie = {}
            brownie["Nome"] = input("Digite o nome do cliente: ").capitalize()
            brownie["quantidade"] = float(input("Digite a quantidade: "))
            pedidos.append(brownie)
            salvar_pedidos(pedidos)
        case "2":
            doce = "palha italiana"
        case "3":
            doce = input("digite o nome do doce: ")
        case _:
            print("opção inválida, tente novamente")
            




print("1- adcionar pedido")
print("2- ver pedidos")
print("3- editar pedido")
print("4- excluir pedido")
print("5- sair")
escolha = input("digite a opção desejada: ")

while True:
    match escolha:
        case "1":
            adcionar_pedido()
        case "2":
            ver_pedidos()
        case "3":
            editar_pedido()
        case "4":
            excluir_pedido()
        case "5":
            print("saindo...")
            break
        case _:
            print("opção inválida, tente novamente")
