# FarmTech Solutions - Análise Estatística
# Culturas: Café e Milho

options(scipen = 999)

# Leitura do CSV
dados <- read.csv("C:\\Users\\yanaz\\OneDrive\\Documents\\VSCode\\FIAP\\dados_fazenda.csv")

print(dados)

AreaTotal <- as.numeric(dados$AreaTotal)
Ruas1 <- as.numeric(dados$Ruas1)
Ruas2 <- as.numeric(dados$Ruas2)
Pulv1 <- as.numeric(dados$Pulv1)
Pulv2 <- as.numeric(dados$Pulv2)

cat("\n📊 RESULTADOS ESTATÍSTICOS\n")

cat("\nMÉDIAS:\n")
cat("Área Total:", mean(AreaTotal), "\n")
cat("Ruas Cultura 1:", mean(Ruas1), "\n")
cat("Ruas Cultura 2:", mean(Ruas2), "\n")
cat("Pulverização Cultura 1:", mean(Pulv1), "\n")
cat("Pulverização Cultura 2:", mean(Pulv2), "\n")

cat("\nDESVIO PADRÃO:\n")
cat("Área Total:", sd(AreaTotal), "\n")
cat("Ruas Cultura 1:", sd(Ruas1), "\n")
cat("Ruas Cultura 2:", sd(Ruas2), "\n")
cat("Pulverização Cultura 1:", sd(Pulv1), "\n")
cat("Pulverização Cultura 2:", sd(Pulv2), "\n")