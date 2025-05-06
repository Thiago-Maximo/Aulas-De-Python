
######################### COMEÇO DAS QUESTÕES ###########################################################

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# 1) print(fruits.count('apple'))
# ( ) 3  ( ) 1  ( ) 0  (x) 2

# 2) print(fruits.count('tangerine'))
# ( ) 1  (x) 0  ( ) 2  ( ) 3

# 3) print(fruits.index('banana'))
# ( ) 4  ( ) 1  ( ) 2  (x) 3

# 4) print(fruits.index('banana', 4))
# (x) 6  ( ) 2  ( ) 1  ( ) 4

# 5)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
print(fruits)
# ( ) ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# ( ) ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# ( ) ['pear', 'orange', 'kiwi', 'banana', 'banana', 'apple', 'apple']
# (x) ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# 6)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grape')
print(fruits)
# ( ) ['apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# ( ) ['grape', 'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple']
# (x) ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# ( ) ['grape', 'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# 7)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grape')
fruits.sort()
print(fruits)
# ( ) ['grape', 'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# ( ) ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# (x) ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# ( ) ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

# 8)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grape')
fruits.sort()
print(fruits.pop())
# (x) pear
# ( ) grape
# ( ) ['orange', 'kiwi', 'grape', 'banana', 'banana', 'apple', 'apple']
# ( ) ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

# 9)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grape')
fruits.sort()
print(fruits)
# (x) ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
# ( ) grape
# ( ) ['orange', 'kiwi', 'grape', 'banana', 'banana', 'apple', 'apple']
# ( ) pear

# 10)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.extend(['morango', 'abacaxi'])
print(fruits)
# (x) ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'morango', 'abacaxi']
# ( ) ['morango', 'abacaxi', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# ( ) ['pear', 'banana', 'kiwi', 'apple', 'banana', 'morango', 'abacaxi']
# ( ) ['morango', 'abacaxi', 'orange', 'apple', 'pear', 'banana', 'kiwi']


################################# FIM DAS QUESTÕES ###################################################################

##################### INICIO DOS TESTES #################################################
# Teste 1
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))  # Saída: 2

# Teste 2
print(fruits.count('tangerine'))  # Saída: 0

# Teste 3
print(fruits.index('banana'))  # Saída: 3

# Teste 4
print(fruits.index('banana', 4))  # Saída: 6

# Teste 5
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
print(fruits)  # Saída: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# Teste 6
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grape')
print(fruits)  # Saída: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

# Teste 7
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grape')
fruits.sort()
print(fruits)  # Saída: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

# Teste 8
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grape')
fruits.sort()
print(fruits.pop())  # Saída: pear

# Teste 9
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grape')
fruits.sort()
print(fruits)  # Saída: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

# Teste 10
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.extend(['morango', 'abacaxi'])
print(fruits)  # Saída: ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'morango', 'abacaxi']

#################################### FIM DOS TESTES ################################################################