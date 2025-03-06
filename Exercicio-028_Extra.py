# Importando a biblioteca numpy para trabalhar com arrays (matrizes)
import numpy as np

# Criando a matriz de dados com informações de usuários (código, nome, senha, saldo)
dados = np.array([["1", "Maximo", "123", 2500],
                  ["2", "Barreto", "345", 4000],
                  ["3", "Henrique", "567", 1500]])

# Definindo o número máximo de tentativas de login
max_tentativas = 3

# Inicializando o contador de tentativas
tentativas = 0

# Inicializando a variável que vai controlar o status do login (se deu certo ou não)
login_ok = False

# Loop que executa enquanto o login não for bem-sucedido e o número de tentativas não atingir o máximo
while not login_ok and tentativas < max_tentativas:

    # Solicita o código de acesso ao usuário
    icodigo = input('Digite o Seu Código de Acesso: ')

    # Solicita a senha de acesso ao usuário
    isenha = input('Digite a Sua Senha de Acesso: ')

    # Loop que percorre cada linha da matriz de dados, ou seja, cada usuário
    for linha in range(dados.shape[0]):

        # Obtém o código do usuário na posição (linha, 0) da matriz
        codigo_na_posicao = dados[linha, 0]

        # Obtém a senha do usuário na posição (linha, 2) da matriz
        senha_na_posicao = dados[linha, 2]

        # Converte o saldo para float, pois inicialmente ele está como string na matriz
        saldo = float(dados[linha, 3])

        # Verifica se o código e a senha inseridos pelo usuário são iguais aos dados da matriz
        if icodigo == codigo_na_posicao and isenha == senha_na_posicao:

            # Exibe uma mensagem de boas-vindas e o saldo do usuário
            print('')
            print('#' * 40)
            print(
                f"Bem-vindo {dados[linha, 1]}, Seu Saldo é de R${saldo:,.2f}")  # A formatação permite exibir o saldo com 2 casas decimais

            # Atualiza a variável login_ok para True, pois o login foi bem-sucedido
            login_ok = True

            # Inicia o loop de saque, que ficará ativo até o usuário decidir não sacar mais
            while True:  # Loop de saque
                # Solicita ao usuário o valor do saque
                saque = int(input("Digite o Valor do saque: "))

                # Verifica se o valor do saque é maior que o saldo disponível
                if saque > saldo:
                    # Exibe uma mensagem de saldo insuficiente
                    print("Saldo Insuficiente")
                    # Pergunta se o usuário deseja tentar outro valor
                    if input("Deseja Informar outro valor?: ").capitalize() != "Sim":
                        break  # Sai do loop de saque, caso o usuário não queira tentar novamente
                else:
                    # Se o saque for possível, subtrai o valor do saque do saldo
                    saldo = saldo - saque

                    # Calcula a quantidade de notas que o usuário vai receber (notas de 100, 50, 20, 10, 5 e 1)
                    n100 = saque // 100
                    r100 = saque % 100
                    n50 = r100 // 50
                    r50 = r100 % 50
                    n20 = r50 // 20
                    r20 = r50 % 20
                    n10 = r20 // 10
                    r10 = r20 % 10
                    n5 = r10 // 5
                    r5 = r10 % 5
                    n1 = r5 // 1
                    r1 = r5 % 1

                    # Exibe o valor sacado e o saldo atualizado
                    print("")
                    print(f'Você sacou R${saque:,.2f} e seu saldo é de R${saldo:,.2f}')

                    # Exibe a quantidade de notas de cada valor que o usuário irá receber
                    if n100 != 0:
                        print(f"Notas de R$100: {n100}")
                    if n50 != 0:
                        print(f"Notas de R$50: {n50}")
                    if n20 != 0:
                        print(f"Notas de R$20: {n20}")
                    if n10 != 0:
                        print(f"Notas de R$10: {n10}")
                    if n5 != 0:
                        print(f"Notas de R$5: {n5}")
                    if n1 != 0:
                        print(f"Notas de R$1: {n1}")

                    # Pergunta se o usuário deseja realizar outro saque
                    if input("Deseja realizar outro saque?: ").capitalize() != "Sim":
                        break  # Sai do loop de saque caso o usuário escolha não realizar outro saque
    # Incrementa o contador de tentativas após cada tentativa de login
    tentativas += 1

    # Se o login não foi bem-sucedido, informa ao usuário quantas tentativas restam
    if not login_ok:
        print('')
        print('#' * 40)
        print(f"Login falhou! Você tem {max_tentativas - tentativas} tentativa(s) restante(s).")

# Caso o login falhe após as tentativas máximas, exibe uma mensagem de bloqueio de acesso
if not login_ok:
    print('')
    print('#' * 40)
    print("Número máximo de tentativas atingido. Acesso bloqueado.")




# Comentários Explicativos:
# Importação do numpy: O código importa a biblioteca numpy para trabalhar com matrizes (arrays), que são estruturas de dados bidimensionais. A matriz dados armazena as informações dos usuários, como código, nome, senha e saldo.
#
# Matriz dados: A matriz dados armazena as informações de usuários: o código, o nome, a senha e o saldo. O saldo, por exemplo, é armazenado como uma string e depois convertido para float para ser manipulado corretamente em cálculos.
#
# Contador de tentativas e controle de login:
#
# O código permite até 3 tentativas para o login. O loop while not login_ok continua até o login ser bem-sucedido ou até que o número de tentativas atinja o máximo (3 tentativas).
# O código verifica se o código e a senha digitados pelo usuário correspondem aos dados da matriz dados. Se corresponderem, o login é bem-sucedido, e o saldo do usuário é exibido.
# Loop de saque:
#
# Após o login, o usuário pode realizar múltiplos saques. O loop while True permite que o processo de saque se repita até o usuário escolher não realizar mais saques.
# O valor do saque é calculado e, caso o saldo seja insuficiente, o programa informa o erro e permite ao usuário tentar outro valor.
# Cálculo das notas:
#
# O código calcula quantas notas de 100, 50, 20, 10, 5 e 1 serão fornecidas ao usuário para o valor do saque solicitado. Isso é feito usando operações de divisão inteira e módulo (// e %), para dividir o saque nas notas correspondentes.
# Mensagens e Saída:
#
# Se o login falhar, o código informa ao usuário quantas tentativas restam. Caso o login seja bem-sucedido, o saldo é atualizado após cada saque e o usuário é informado das notas que receberá.
# Se o número máximo de tentativas for atingido sem sucesso no login, o acesso é bloqueado e o programa termina.