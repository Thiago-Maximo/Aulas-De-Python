# Crie um programa que leia o nome de uma cidade e diga se ela começa com o Nome "Santo".

# Leitura do nome da cidade
cidade = input("Digite o nome de uma cidade: ")

# Verificando se o nome da cidade começa com "Santo"
# Primeira forma de resolver
if cidade.strip().lower().startswith("santo"):
    print("A cidade começa com 'Santo'.")
else:
    print("A cidade NÃO começa com 'Santo'.")