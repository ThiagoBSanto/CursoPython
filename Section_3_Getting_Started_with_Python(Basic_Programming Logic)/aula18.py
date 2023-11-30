#
import os
print('\nDETALHAMENTO DE LISTA EM PYTHON\n\n')

# Em Python, uma lista é uma estrutura de dados que
# permite armazenar uma coleção ordenada de elementos.
# Cada elemento pode ser de qualquer tipo, e as listas
# são mutáveis, o que significa que seus elementos
# podem ser alterados, adicionados ou removidos.
#
# *****    SINTAXE DE UMA LISTA    *****
#
# Para criar uma lista, utilizamos colchetes [] e separamos
# os elementos por vírgulas. Aqui está um exemplo:

# Exemplo:
# minha_lista = [1, 2, 3, "quatro", 5.0]

# *****    ACESSANDO ELEMENTOS    *****
#
# Os elementos de uma lista são acessados através de índices.
# O índice do primeiro elemento é 0, e índices negativos
# contam a partir do final da lista.

# Exemplo:
# primeiro_elemento = minha_lista[0]
# ultimo_elemento = minha_lista[-1]

# *****    MODIFICANDO ELEMENTOS    *****
#
# Os elementos de uma lista podem ser modificados atribuindo
# um novo valor a uma posição específica.

# Exemplo:
# minha_lista[1] = "dois"

# *****    ADICIONANDO ELEMENTOS    *****
#
# Podemos adicionar elementos ao final de uma lista usando
# o método append() ou inserir elementos em uma posição
# específica usando o método insert().

# Exemplos:
# minha_lista.append(6)
# minha_lista.insert(2, "inserido")

# *****    REMOVENDO ELEMENTOS    *****
#
# Elementos podem ser removidos com a declaração del ou
# usando métodos como remove() e pop().

# Exemplos:
# del minha_lista[3]              # Remove o elemento no índice 3
# minha_lista.remove("quatro")    # Remove o elemento com o valor "quatro"
# elemento_removido = minha_lista.pop(1)  # Remove e retorna o elemento no índice 1

# *****    OPERAÇÕES COM LISTAS    *****
#
# Algumas operações comuns incluem encontrar o comprimento
# de uma lista com len(), verificar a existência de um
# elemento com o operador in, e concatenar listas com o
# operador +.

# Exemplos:
# comprimento_da_lista = len(minha_lista)
# existe_elemento = "dois" in minha_lista
# nova_lista = minha_lista + [7, 8, 9]

# *****    ITERANDO SOBRE UMA LISTA    *****
#
# O loop for é frequentemente utilizado para iterar sobre
# os elementos de uma lista.

# Exemplo:
# for elemento in minha_lista:
#     print(elemento)


# *****    SLICING (FATIAMENTO) DE LISTA    *****
#
# Além do acesso a elementos individuais, podemos
# realizar o slicing em uma lista para obter
# subconjuntos dela. O slicing utiliza a notação
# [inicio:fim], onde 'inicio' é inclusivo e 'fim'
# é exclusivo.

# Exemplo:
# sublista = minha_lista[1:4]  # Retorna [2, 3, "quatro"]

# *****    FUNÇÕES E MÉTODOS ÚTEIS PARA LISTAS    *****
#
# Python oferece várias funções e métodos úteis para
# manipulação de listas. Alguns exemplos incluem:

# - sorted(): Retorna uma nova lista ordenada a partir
#   dos elementos da lista original.

# Exemplo:
# lista_original = [3, 1, 4, 1, 5, 9, 2]
# lista_ordenada = sorted(lista_original)

# - count(): Conta o número de ocorrências de um
#   elemento na lista.

# Exemplo:
# numero_de_uns = lista_original.count(1)

# - index(): Retorna o índice da primeira ocorrência
#   de um elemento.

# Exemplo:
# indice_do_cinco = lista_original.index(5)

# - extend(): Adiciona os elementos de uma lista ao
#   final de outra.

# Exemplo:
# outra_lista = [8, 6, 7, 5, 3, 0, 9]
# lista_original.extend(outra_lista)

# *****    LIST COMPREHENSIONS    *****
#
# List comprehensions são uma maneira concisa e poderosa
# de criar listas. Permitem gerar uma lista aplicando
# uma expressão a cada item em uma sequência.

# Exemplo:
# quadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# *****    FUNÇÃO MAP()    *****
#
# A função map() pode ser utilizada para aplicar uma
# função a cada item de uma lista.

# Exemplo:
# def dobrar(numero):
#     return numero * 2
# lista_dobrada = list(map(dobrar, minha_lista))

# Essas são apenas algumas das muitas funcionalidades e
# técnicas que envolvem o uso de listas em Python. Com a
# prática, você se tornará mais confortável ao manipular
# e trabalhar com essas estruturas de dados flexíveis e
# poderosas.
#
#
################# EXERCICIO 1 #########################
#
#
# nomes = [ "Ana Silva",  "Carlos Oliveira", "Renata Santos", "João Pereira",
#          "Mariana Costa", "Pedro Almeida", "Camila Lima", "Rafael Sousa",
#          "Isabela Fernandes",  "Lucas Barbosa","Thiago Barbosa" ]

# for i in range(len(nomes)):
#     print(f"{i} - {nomes[i]} ")
#
#
#
################# EXERCICIO 2 #########################
#
# #


a = 0.1
b = 0.7
c = a+b
print(c)
