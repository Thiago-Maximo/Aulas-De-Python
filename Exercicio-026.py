# Crie um programa que leia a frase pelo teclado e mostre:
# 1°: Quantas Vezes a letra "A" aparece.
# 2°: Em que posição ela aparece a primeira vez.
# 3°: Em que posição ela aparece a ultima vez

letraA = input('Digite Uma Frase: ')
letraA_formatada = letraA.lower()
# Encontrando a primeira e última posição de "a"
primeira_posicao = letraA_formatada.find('a')
ultima_posicao = letraA_formatada.rfind('a')
print(f'A letra "A" aparece: {letraA_formatada.count("a")} vezes.')
print(f'A primeira vez que a letra "A" aparece é na posição: {primeira_posicao}.')
print(f'A última vez que a letra "A" aparece é na posição: {ultima_posicao}.')