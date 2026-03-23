#FarmTech Solutions, solução para as culturas de Café e milho
#Área retangular com 12000X7000 metros
#Fazenda dividida em 3 partes iguais, sendo 2 para as culturas e 1 para descanso como é a melhor prática para o solo
#Pulverização de 500 ML por Rua
#Calculo de quantos litros de pulverização são necessários para cada cultura
#Área total da fazenda

#input de dados
Cultura1 = input("Digite a cultura 1: ")
Cultura2 = input("Digite a cultura 2: ")
cumprimentoArea = input("Digite o comprimento da área da fazenda em metros: ")
larguraArea = input("Digite a largura da área da fazenda em metros: ")
Pulverizacao = input("Digite a quantidade de pulverização em ML por rua: ")
espacamentoRuas = (4.0)  # em metros

#Calculo de área total da fazenda
areaTotal = int(cumprimentoArea) * int(larguraArea)  # em metros quadrados
print(f"A área total da fazenda é de {areaTotal} metros quadrados.")

#Calculo de área para cada cultura
areaCultura1 = areaTotal / 3  # Supondo que as culturas sejam plantadas em áreas iguais
areaCultura2 = areaTotal / 3  # Supondo que as culturas sejam plantadas em áreas iguais
areaDescanso = areaTotal / 3  # Supondo que haja uma área de descanso igual para as culturas

#Calculo área de pulverização para cada cultura, desconsidera a área de descanso
areaPulverizacaoCultura1 = areaCultura1  # A área de pulverização é igual à área da cultura
areaPulverizacaoCultura2 = areaCultura2  # A área de pulverização
areapulverizacaototal = areaPulverizacaoCultura1 + areaPulverizacaoCultura2  # A área total de pulverização é a soma das áreas de pulverização das duas culturas

#Calculo largura de pulverização
larguraPulverizacao = areaPulverizacaoCultura1 / int(cumprimentoArea)  # A largura de pulverização é a área de pulverização dividida pelo comprimento da área

#Calculo de ruas necessárias para pulverização
numeroRuas = int(larguraPulverizacao) / espacamentoRuas
print(f"O número de ruas necessárias para a pulverização é de {numeroRuas:.2f} ruas.")

#Calculo de pulverização total
totalPulverizacao = (numeroRuas * int(Pulverizacao)) / 1000  # Convertendo ML para Litros
print(f"A quantidade total de pulverização necessária é de {totalPulverizacao:.2f} litros.")