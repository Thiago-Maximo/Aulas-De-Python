# Crie um programa que Leia a Velocidade de um carro.
# Se ela ultrapassar 80km/h, mostre uma dizendo que foi multado.
# A Multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input('Digite a Velocidade do Carro Km/h ?: '))

if velocidade > 80: # Verifica se a velocidade é maior que o limite permitido
    excesso = velocidade - 80  # Calcula o excesso de velocidade
    multa = excesso * 7  # Calcula a multa (R$7 por cada km acima do limite)
    print('Você Foi Multado por exceder o limite de velocidade')
    print(f'Valor da Multa: R$ {multa:.2f}')
else: # Se não for, exibe uma mensagem
    print('Você Não Foi multado, Continue no Limite de Velocidade')