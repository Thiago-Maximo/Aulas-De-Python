# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
cateto_oposto = int(input('Digite o valor do cateto oposto: '))
cateto_adjacente = int(input('Digite o valor do cateto adjacente: '))
# math.hypot() Calcula a Hipotenusa
hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)
print(f'A Hipotenusa é: {hipotenusa}')