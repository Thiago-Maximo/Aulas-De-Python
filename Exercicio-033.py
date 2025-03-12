# Faça um Programa que leia um ano qualquer e mostre se ele é bissexto
print('Vamos descobrir se o Ano é Bissexto?')
ano = int(input('Digite o Ano: '))

# Verificando as condições para um ano ser bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): #verifica se o ano é divisível por 4, mas não é divisível por 100. Ou seja, se ele é divisível por 4, mas não por 100, ele é bissexto.
    print(f'O Ano {ano} é Bissexto')
else: #verifica se o ano é divisível por 400, o que também faz o ano ser bissexto.
    print(f'O Ano {ano} não é Bissexto')
