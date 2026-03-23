# Projeto: Farm Tech Fase 1 - IA

print("🚀 VERSAO NOVA RODANDO")

import math
import csv

# Vetores de armazenamento
registros_cultura = []
registros_area = []
registros_ruas = []
registros_pulverizacao = []

def entrada_dados():
    Cultura1 = input("Digite a cultura 1: ")
    Cultura2 = input("Digite a cultura 2: ")
    comprimentoArea = float(input("Digite o comprimento da área da fazenda em metros: "))
    larguraArea = float(input("Digite a largura da área da fazenda em metros: "))
    Pulverizacao = float(input("Digite a quantidade de pulverização em ML por rua: "))
    espacamentoRuas = 4.0
    areaTotal = comprimentoArea * larguraArea
    print(f"Area total {areaTotal:.2f} em metros quadrados.")

    areaPorParte = areaTotal / 3
    larguraCultura = areaPorParte / comprimentoArea
    numeroRuas1 = math.ceil(larguraCultura / espacamentoRuas)
    pulverizacao1 = (numeroRuas1 * Pulverizacao) / 1000
    numeroRuas2 = math.ceil(larguraCultura / espacamentoRuas)
    pulverizacao2 = (numeroRuas2 * Pulverizacao) / 1000
    print("\resultado da pulverizacao:")
    print(f"{Cultura1}: {numeroRuas1} ruas | {pulverizacao1:.2f} L")
    print(f"{Cultura2}: {numeroRuas2} ruas | {pulverizacao2:.2f} L")

    registros_cultura.append((Cultura1, Cultura2))
    registros_area.append(areaTotal)
    registros_ruas.append((numeroRuas1, numeroRuas2))
    registros_pulverizacao.append((pulverizacao1, pulverizacao2))

    print("dados salvos")

def saida_dados():
    if len(registros_cultura) == 0:
        print("Nenhum registro encontrado.")
        return

    for i in range(len(registros_cultura)):
        c1, c2 = registros_cultura[i]
        r1, r2 = registros_ruas[i]
        p1, p2 = registros_pulverizacao[i]

        print(f"""
ID {i}
Cultura 1: {c1} | Ruas: {r1} | Pulverização: {p1:.2f} L
Cultura 2: {c2} | Ruas: {r2} | Pulverização: {p2:.2f} L
Área total: {registros_area[i]:.2f} m²
""")

def atualizar_dados():
    saida_dados()
    if len(registros_cultura) == 0:
        return

    idx = int(input("Digite o ID do registro que deseja atualizar: "))

    if idx < 0 or idx >= len(registros_cultura):
        print("ID invalido.")
        return

    registros_cultura.pop(idx)
    registros_area.pop(idx)
    registros_ruas.pop(idx)
    registros_pulverizacao.pop(idx)

    print("Digite os novos dados:")
    entrada_dados()

def deletar_dados():
    saida_dados()
    if len(registros_cultura) == 0:
        return

    idx = int(input("Digite o ID do registro que deseja deletar: "))

    if idx < 0 or idx >= len(registros_cultura):
        print("ID invalido.")
        return

    registros_cultura.pop(idx)
    registros_area.pop(idx)
    registros_ruas.pop(idx)
    registros_pulverizacao.pop(idx)

    print("Registro deletado com sucesso!")

def exportar_csv():
    if len(registros_cultura) == 0:
        print("Nenhum dado para exportar.")
        return

    with open("dados_fazenda.csv", mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Cultura1", "Cultura2",
            "AreaTotal",
            "Ruas1", "Ruas2",
            "Pulv1", "Pulv2"
        ])

        for i in range(len(registros_cultura)):
            c1, c2 = registros_cultura[i]
            r1, r2 = registros_ruas[i]
            p1, p2 = registros_pulverizacao[i]
            area = registros_area[i]

            writer.writerow([c1, c2, area, r1, r2, p1, p2])

    print("📁 Dados exportados para 'dados_fazenda.csv'")

# Menu principal
while True:
    print("\n1. Entrada de dados")
    print("2. Visualizar dados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Sair")
    print("6. Exportar dados para CSV")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        entrada_dados()
    elif opcao == "2":
        saida_dados()
    elif opcao == "3":
        atualizar_dados()
    elif opcao == "4":
        deletar_dados()
    elif opcao == "5":
        print("Encerrando... Ate logo!")
        break
    elif opcao == "6":
        exportar_csv()
    else:
        print("Opcao invalida.")