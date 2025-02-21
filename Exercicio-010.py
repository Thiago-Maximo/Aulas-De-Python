# Crie um Programa que leia qunato diheiro uma pessoa tem na carteira e mostre quantos Dólares ela Pode Comprar. Considerando a cotação atual.

# Função para converter Reais em Dólares
def converter_reais_para_dolares(valor_reais, taxa_cambio):
    return valor_reais * taxa_cambio

# Solicita ao usuário o valor em Reais
print('#'*10)
valor_reais = float(input("Digite o valor em Reais (BRL): "))

# Defina a taxa de câmbio atual (exemplo, 1 BRL = 0,19 USD)
taxa_cambio = 0.1753555  # Alterar conforme a taxa atual

# Converte o valor em Reais para Dólares
valor_dolares = converter_reais_para_dolares(valor_reais, taxa_cambio)

# Exibe o resultado
print('#'*40)
print(f"Com R$ {valor_reais:.2f}, você pode comprar ${valor_dolares:.2f} Dólares")
