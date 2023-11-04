#
#
# *****************    TIPAGEM    ****************
#
# Tipagem em programação refere-se ao sistema 
# que define como os tipos de dados são tratados
# em uma linguagem. Existem dois principais 
# sistemas de tipagem:
#
# 1 - Tipagem Estática: Requer que os tipos de dados
# sejam declarados explicitamente e verifica os
# tipos em tempo de compilação. Linguagens como
# C, Java e C# usam tipagem estática.
#
# 2 -Tipagem Dinâmica: Permite que os tipos de dados 
# sejam verificados em tempo de execução e pode mudar
# durante a execução. Linguagens como Python, 
# JavaScript e Ruby usam tipagem dinâmica.
#
# Existe a distinção entre tipagem forte e fraca
#
# Tipagem forte: Não permite operações entre tipos incompatíveis
#
# Tipagem fraca: ermite conversões implícitas entre tipos
#
# OBS -> Conversões implícitas :
# capacidade de uma linguagem de programação de realizar 
# automaticamente a conversão de um tipo de dado para outro, sem a
# necessidade de intervenção explícita do programador.
#
#
# *****************    TIPO INTEIRO    ****************
#
# Também conhecido como "int", é um tipo de dado numérico usado em programação 
# para representar números inteiros, ou seja, números sem parte decimal. 
# Os inteiros podem ser positivos, negativos ou zero.
#
print("Exemplo 1 - Numeros inteiros")
a = 5
b = -3
soma = a + b  
multiplicacao = a * b  
print("a = 5 e b = -3")
print("a + b = ",a+b)
print("a * b = ",a*b)
print()
#
# APLICAÇÃO:
#
# Os inteiros são usados em uma ampla variedade 
# de aplicativos, desde cálculos matemáticos 
# simples até o controle de índices de listas 
# e arrays em programação, manipulação de datas 
# e muitos outros cenários.
#
#
# *****************    TIPO FLOAT    ****************
#
# Um tipo "float," abreviação de "ponto flutuante," é um 
# tipo de dado numérico usado em programação para 
# representar números de ponto flutuante, ou seja, números 
# que podem ter uma parte fracionária. Os números em ponto 
# flutuante são usados para representar valores reais ou 
# aproximações de valores reais, incluindo números racionais 
# e irracionais.
#
print("Exemplo 2 - Numeros flutuantes")
a = 3.5
b = -1.25
soma = a + b  
multiplicacao = a * b  
print("a = 3.5 e b = -1.25")
print("a + b = ",a + b)
print("a * b = ",a * b)
print()
#
# APLICAÇÃO:
# Os números de ponto flutuante são amplamente utilizados em áreas
# que envolvem medições precisas, como física, engenharia, finanças
# e muitas outras disciplinas. Eles são essenciais para cálculos 
# científicos e financeiros, bem como para representar qualquer 
# valor que possa ter uma parte fracionária.
#
#
# *****************    TIPO BOOL    ****************
#
#O tipo bool em programação é uma abreviação de "boolean" e é 
# usado para representar valores lógicos, ou seja, valores que 
# podem ser verdadeiros ou falsos. Em muitas linguagens de 
# programação, incluindo Python, o tipo bool é uma parte 
# fundamental e é frequentemente usado para controle de fluxo e 
# tomada de decisões em programas.
#
# Aqui estão alguns pontos-chave sobre o tipo bool:
#
# 1 - Valores Booleanos: O tipo bool possui apenas dois valores 
# possíveis: True (verdadeiro) e False (falso). Esses valores 
# representam a lógica binária básica, onde algo pode ser 
# verdadeiro ou falso.
#
# 2 - Operadores Lógicos: Os valores booleanos são frequentemente 
# usados em expressões lógicas, onde operadores lógicos, como and 
# (e), or (ou) e not (não), são usados para combinar valores 
# booleanos e tomar decisões com base nesses valores.
#
print("Exemplo 3 - BOOL")
print("a = True, b = False")
a = True
b = False
resultado = a and b  # Isso resulta em False (False se ambos são False)
print("resultado", resultado)
print()
#
# 3 - Comparação: Valores booleanos também são usados em comparações. 
# Operadores de comparação, como == (igual a), != (diferente de), 
# < (menor que), > (maior que), entre outros, comparam valores e retornam 
# True ou False com base na condição.
print("Exemplo 4") 
numero1 = 5
numero2 = 10
resultado1 = numero1 < numero2  # Isso resulta em True (5 é menor que 10)
print(resultado1)
print()
#
# 4 - Controle de Fluxo: Valores booleanos são amplamente usados em 
# estruturas de controle de fluxo, como condicionais (if/else) e 
# loops. Eles permitem que seu programa tome decisões e execute código 
# com base em condições lógicas.
#
print("idade = 18")
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
#
# 5 - Lógica e Tomada de Decisões: O tipo bool é essencial para a 
# programação, pois permite que programas realizem tarefas complexas 
# tomando decisões com base em valores lógicos. Isso é fundamental em 
# muitos aplicativos, desde jogos até aplicativos da web e sistemas 
# de controle.
#
# OBS -> BOOL
#   O tipo bool desempenha um papel fundamental na escrita de código 
#   e na criação de programas que podem responder a condições e realizar 
#   ações com base nessas condições.

