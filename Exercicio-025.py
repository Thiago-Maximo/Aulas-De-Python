# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = input('Digite Seu Nome Completo: ')
nome_formatado = nome.lower()

print('silva' in nome_formatado)