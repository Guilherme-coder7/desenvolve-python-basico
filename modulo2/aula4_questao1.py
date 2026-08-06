# Lê o comprimento do terreno
comprimento = int(input())

# Lê a largura do terreno
largura = int(input())

# Lê o preço do metro quadrado
preco_m2 = float(input())

# Calcula a área do terreno
area_m2 = comprimento * largura

# Calcula o preço total
preco_total = area_m2 * preco_m2

# Mostra o resultado formatado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")