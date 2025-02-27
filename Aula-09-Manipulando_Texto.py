# Fatiamento de String simples, Fatiamento o ultimo valor é sempre ignorado pelo python, então ele não aparece
from itertools import count

print('Para Exibir os comandos eu Utilizei o "" para poder comentar e não dar erro no codigo')

frase ='Curso em Video Python'
print(frase[9:14])

# Fatiamnto pulando de 2 em 2
frase_nova = 'Curso em Video Python'
print(frase_nova[9:21:2])

# Fatiamento de apartir de um ponto até outro
print(frase[:5]) #Começa do 0 e vai até o 5, ou seja, vai escrever a palavra curso
print(frase[9:]) # Começa no 9 e vai até o final (só vai até o final por que não tem nenhum numero especificando o limite)

# Fatiamento pulando de 3 em 3
print(frase[9::3])

# Análise de String
print(len(frase), ' - len(frase)  len() vai mostrar quantos caracteres tem a string') # len() vai mostrar quantos caracteres tem a string
print(frase.count('o'), ' - frase.count("o") vai contar quantas vezes aparece a letra o, lembrando que o python diferencia o maiusculo do minusculo') # vai contar quantas vezes aparece a letra o, lembrando que o python diferencia o maiusculo do minusculo
print(frase.count('o',0,13), ' - frase.count("o",0,13) vai contar quantas vezes a letra o aparece no intervalo de caracteres, começando do 0 até 13, ou seja 1 só, "Curso em Video Python". Ele vai até a letra o do "Video" mas não exibe ela, para exibilo teria que ser 14') # vai contar quantas vezes a letra o aparece no intervalo de caracteres, começando do 0 até 13, ou seja 1 só, "Curso em Video Python". Ele vai até a letra o do "Video" mas não exibe ela, para exibilo teria que ser 14
print(frase.find('deo'), ' - frase.find("deo")  vai procurar aonde as letras começaram e até onde terminam') # vai procurar aonde as letras começaram e até onde terminam
print(frase.find('Android'), ' - frase.find("Android") vai receber o -1 por que a palavra não existe na variavel, então invés de dar erro ele irá exibir o -1') # vai receber o -1 por que a palavra não existe na variavel, então invés de dar erro ele irá exibir o -1
print('Curso' in frase, ' - "Curso" in frase vai verificar se a palavra digitada existe na variavel, diferente do find() que exibe os numeros onde começam e terminam, o in vai exibir uma saida booleana (True, False) True = Verdadeiro,sim | False = Falso, Não') # vai verificar se a palavra digitada existe na variavel, diferente do find() que exibe os numeros onde começam e terminam, o in vai exibir uma saida booleana (True, False) True = Verdadeiro,sim | False = Falso, Não

# Transformação
print(frase.replace('Python','Android'), ' - frase.replace("Python","Android")  replace() substitui as palavras ou letras, primeiro digitamos a frase a ser trocada e depois a frase que queremos que substitua') # replace() substitui as palavras ou letras, primeiro digitamos a frase a ser trocada e depois a frase que queremos que substitua
print(frase.upper(), ' - frase.upper() Vai deixar toda a frase em Maiuscula') # Vai deixar toda a frase em Maiuscula
print(frase.lower(), ' - frase.lower() vai deixar toda a frase em minuscula') # vai deixar toda a frase em minuscula
print(frase.capitalize(), ' - frase.capitalize() Vai Deixar a primeira letra em Maiuscula e o resto em minusculo') # Vai Deixar a primeira letra em Maiuscula e o resto em minusculo
print(frase.title(), ' - frase.title() O começo de cada frase fica em Maiusculo, a primeira letra') # O começo de cada frase fica em Maiusculo, a primeira letra

teste = '   Aprenda Python'
print(teste, ' - Frase com espaços no começo e final')
print(teste.strip(), '- teste.strip() o strip remove os espaços no começo e no fim, o do meio não pois separa as duas palavras.') # o strip remove os espaços no começo e no fim, o do meio não pois separa as duas palavras.
print(teste.rstrip(), '- teste.rstrip() vai remover somente os espaços da direita e manter os da esquerda') # vai remover somente os espaços da direita e manter os da esquerda
print(teste.lstrip(), '- teste.lstrip() Vai remover os espaços da esquerda e manter os da direita') # Vai remover os espaços da esquerda e manter os da direita

# Divisão
print(frase.split(), ' - frase.split() split vai gerar uma lista com cada palavra, ou seja a string é dividida e vira uma lista, onde cada palavra é exibida separadamente') # split vai gerar uma lista com cada palavra, ou seja a string é dividida e vira uma lista, onde cada palavra é exibida separadamente

# Junção
l1 = "Junção"
l2 = "Curso"
l3 = "em"
l4 = "Video"
lista = [l1,l2,l3,l4]
print('-'.join(lista), '"-".join(variavel do tipo lista) vai juntar todas as strings dessa lista e separalas com o -, exibindo como se fosse um texto unico, se não tiver nada vau deixar tudo junto') # "-".join(variavel do tipo lista) vai juntar todas as strings dessa lista e separalas com o -, exibindo como se fosse um texto unico, se não tiver nada vau deixar tudo junto
