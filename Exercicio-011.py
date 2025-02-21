# Faça um Programa que Leia a altura e Largura de uma parede em metros, calcule a sua area e a quantidade de tina necessária
#  Para Pinta-lá, Sabendo que cada litro de tinta pinta uma area de 2m².

# Entrando com os dados
largura = float(input('Digite a Largura da Parede (Em Metros): '))
altura = float(input('Digite a Altura da Parede (Em Metros): '))

# Calculo da area da parede
area = largura * altura

# Exibindo as informações
print(f'A Área da parede é de: {area} metros quadrados')

# Resolvendo a Questão da Tinta
rendimento_tinta = 2
quantidade_tinta_litros = area / rendimento_tinta
quantidade_tinta_litros = round(quantidade_tinta_litros, 2)

print('')
print(f'Para pintar uma parede que tem uma área de {area} m², é necessário {quantidade_tinta_litros} litros de tinta.')