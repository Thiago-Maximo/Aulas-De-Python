# Faça um programa que leia um angulo qualquer e mostra na tela o valor do seno e cosseno e tangente, desse angulo
import math

# Leitura do ângulo em graus
angulo_em_graus = float(input("Digite o ângulo em graus: "))

# Convertendo para radianos
angulo_em_radianos = math.radians(angulo_em_graus)

# Calculando seno, cosseno e tangente
seno = math.sin(angulo_em_radianos)
cosseno = math.cos(angulo_em_radianos)
tangente = math.tan(angulo_em_radianos)

# Exibindo os resultados
print(f"O ângulo de {angulo_em_graus}° tem:")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")

