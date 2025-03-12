# Crie um programa que pergunte a distancia de uma viagem em KM.
# Calcule o preço da passgem, cobrando R$ 0,50 por KM para Viagens de até 200Km.
# e R$ 0,45 para viagens mais longas.

km_viagem = int(input('Digite a Distância da Sua Viagem em KM! :'))

if km_viagem <= 200:
    tarifa = km_viagem * 0.50  # Para viagens até 200 km ele calcula a distancia total e multiplica por 0.50
    print(f'A tarifa para uma viagem de {km_viagem} km é R$ {tarifa:.2f}')
else:
    tarifa = km_viagem * 0.45  # Para viagens maiores que 200 km ele calcula a distancia total e multiplica por 0.45
    print(f'A tarifa para uma viagem de {km_viagem} km é R$ {tarifa:.2f}')