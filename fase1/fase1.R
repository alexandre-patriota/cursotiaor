# Análise Estatística Básica em R dos Dados Agrícolas

# Vetores simulando os dados gerados pelo sistema Python
culturas <- c("Mandioca", "Feijão-caupi", "Mandioca")
areas_plantio <- c(1500.50, 2827.43, 1200.00)
insumos_litros <- asNumeric(c(45.00, 60.50, 35.20))

# Cálculo da Média e Desvio Padrão para a Área
media_area <- mean(areas_plantio)
desvio_area <- sd(areas_plantio)

# Cálculo da Média e Desvio Padrão para os Insumos
media_insumo <- mean(insumos_litros)
desvio_insumo <- sd(insumos_litros)

# Exibição dos resultados no console
cat("========================================\n")
cat("       RELATÓRIO ESTATÍSTICO (R)        \n")
cat("========================================\n")
cat(sprintf("Média da Área Plantada: %.2f m²\n", media_area))
cat(sprintf("Desvio Padrão da Área Plantada: %.2f\n", desvio_area))
cat(sprintf("Média de Insumos Utilizados: %.2f L\n", media_insumo))
cat(sprintf("Desvio Padrão de Insumos: %.2f\n", desvio_insumo))
cat("========================================\n")

