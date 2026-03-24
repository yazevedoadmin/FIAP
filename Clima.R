# Arquivo R para obter dados climáticos usando a API Open-Meteo
# Coordenadas de Machado - MG

library(httr)
library(jsonlite)

# Coordenadas (Machado - MG)
latitude <- -21.67
longitude <- -45.92

cat("Local: Machado - MG\n")

# URL da API Open-Meteo
url <- paste0(
  "https://api.open-meteo.com/v1/forecast?",
  "latitude=", latitude,
  "&longitude=", longitude,
  "&current_weather=true"
)

# Fazer requisição
resposta <- GET(url)

# Converter resposta para JSON
dados <- fromJSON(content(resposta, "text"))

# Extrair informações
temperatura <- dados$current_weather$temperature
vento <- dados$current_weather$windspeed
tempo <- dados$current_weather$weathercode

# Exibir resultados
cat("\nTemperatura atual:", temperatura, "°C\n")
cat("Velocidade do vento:", vento, "km/h\n")
cat("Código do clima:", tempo, "\n")