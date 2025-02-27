# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# EX: Digite um numero: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

# Leitura do número
numero = int(input("Digite um número de 0 a 9999: "))

# Separando as unidades, dezenas, centenas e milhar
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# Exibindo os resultados
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")


# Explicação:
# Unidade: O resto da divisão do número por 10 (numero % 10).
# Dezena: Primeiro dividimos o número por 10, depois pegamos o resto da divisão por 10 ((numero // 10) % 10).
# Centena: Primeiro dividimos o número por 100, depois pegamos o resto da divisão por 10 ((numero // 100) % 10).
# Milhar: Primeiro dividimos o número por 1000, depois pegamos o resto da divisão por 10 ((numero // 1000) % 10).