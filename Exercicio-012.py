# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_original = float(input('Digite o Valor do Produto R$: '))
percentual_desconto = 5
valor_desconto = preco_original * (percentual_desconto / 100)
preco_desconto = preco_original - valor_desconto  # Correção aqui: subtrair o desconto do preço original
print(f'Esse produto teve um desconto de {valor_desconto}. O valor dele com desconto é de: {preco_desconto}')
