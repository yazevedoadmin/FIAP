#FarmTech Solutions, solução para as culturas de Café e milho
# Culturas1: Café cultura2: Milho (Escolhidas)
# Calcula média e desvio padrão dos dados da fazenda
#Criei para ele receber de um arquivo csv porque não consegui conectar direto com o banco de dados, mas a ideia é que ele receba os dados do banco e faça os cálculos, e depois exporte para um arquivo csv para o usuário visualizar

# CÁLCULOS ESTATÍSTICOS

dados <- read.csv("dados_fazenda.csv")

print(dados)

# Médias
cat("\nMédias:\n")
cat("Área:", mean(dados$AreaTotal), "\n")
cat("Ruas C1:", mean(dados$Ruas1), "\n")
cat("Ruas C2:", mean(dados$Ruas2), "\n")
cat("Pulv C1:", mean(dados$Pulv1), "\n")
cat("Pulv C2:", mean(dados$Pulv2), "\n")

# Desvio padrão
cat("\nDesvio padrão:\n")
cat("Área:", sd(dados$AreaTotal), "\n")
cat("Ruas C1:", sd(dados$Ruas1), "\n")
cat("Ruas C2:", sd(dados$Ruas2), "\n")
cat("Pulv C1:", sd(dados$Pulv1), "\n")
cat("Pulv C2:", sd(dados$Pulv2), "\n")

#Resultados
cat("\n📊 RESULTADOS ESTATÍSTICOS\n")