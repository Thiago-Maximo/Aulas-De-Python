# Crie um programa que leia um triangulo o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo.
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('1°-Primeiro Segmento: '))
r2 = float(input('2°-Segundo Segmento: '))
r3 = float(input('3°-Terceiro Segmento: '))
print('-='*20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima podem formar um TRIÂNGULO')
else:
    print('Os Segmentos acima NÃO podem formar um TRIÂNGULO')
print('-=' * 20)