# Este código calcula a média e o desvio padrão do consumo de fertilizantes

# Definição das áreas em metros quadrados
quadrado <- 2 * 2
retangulo <- 0.8 * 0.3
triangulo <- (0.03 * 0.2) / 2
hexagono <- ((0.2 + 0.3) / 2) ^ 2 * (3 * sqrt(3) / 2)
linhas_paralelas <- 0.75 * 0.225

# Vetor com todas as áreas
areas <- c(quadrado, retangulo, triangulo, hexagono, linhas_paralelas)

# Taxas de aplicação (kg/m²)
taxa_nitrogenio <- 0.02  
taxa_npk <- 0.015  
taxa_potassio <- 0.01  

# Cálculo do consumo total para cada fertilizante
consumo_nitrogenio <- areas * taxa_nitrogenio
consumo_npk <- areas * taxa_npk
consumo_potassio <- areas * taxa_potassio

# Média de consumo por tipo de fertilizante
media_nitrogenio <- mean(consumo_nitrogenio)
media_npk <- mean(consumo_npk)
media_potassio <- mean(consumo_potassio)

# Desvio padrão de consumo por tipo de fertilizante
desvio_nitrogenio <- sd(consumo_nitrogenio)
desvio_npk <- sd(consumo_npk)
desvio_potassio <- sd(consumo_potassio)

# Exibir resultados
cat("Média de consumo de Nitrogênio:", media_nitrogenio, "kg/m²\n")
cat("Desvio padrão de consumo de Nitrogênio:", desvio_nitrogenio, "kg/m²\n")

cat("Média de consumo de NPK 4-14-8:", media_npk, "kg/m²\n")
cat("Desvio padrão de consumo de NPK 4-14-8:", desvio_npk, "kg/m²\n")

cat("Média de consumo de Potássio:", media_potassio, "kg/m²\n")
cat("Desvio padrão de consumo de Potássio:", desvio_potassio, "kg/m²\n")