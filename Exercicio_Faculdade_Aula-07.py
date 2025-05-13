# Dada a lista abaixo, escreva um código que retorna uma outra lista cujos elementos são os índices de ocorrência da palavra "jose".

alunos = ["joao","maria","jose","tais","jose","gilberto","jose"]
quantidade = []

for i in range(len(alunos)):
    if alunos[i] == "jose":
        quantidade.append(i)
print(quantidade)
print(alunos)