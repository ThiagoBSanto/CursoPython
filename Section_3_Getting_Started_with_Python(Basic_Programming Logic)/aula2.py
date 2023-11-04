#
#OBS -> Explicação de tipos primitivos na aula 3
#
#
# *****************    TIPO STRING    ****************
#
# Um tipo "string" out str é um tipo de dado usado em  
# programação para representar texto ou sequências de  
# caracteres.
# Strings são usadas para armazenar e manipular informações 
# de texto, como palavras, frases, nomes, endereços, mensagens
# e muito mais. As strings podem conter letras, números, 
# símbolos e espaços em branco.
#
# OBS -> As aplicações listada abaixo para a função print, serve 
#        perfeitamente para as strings   
print("TIPO STRINGS")
print()
print("Exemplo 1:")
primeiro_nome = "John"
sobrenome = "Doe"
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)
print()
#
#
# *****************    FUNÇÃO print()    ****************
#                      
# A função print() é usada para exibir informações na saída padrão,
# que geralmente é a tela do console. 
# Pode ser usada para imprimir texto, variáveis, expressões ou qualquer 
# coisa que você queira exibir enquanto estiver executando seu programa. 
#
print("FUNÇÃO PRINT()")
print()
#
# 1 - Uso básico:
print("Exemplo 1:")
print("Olá, mundo!")
print()
#Isso imprimirá "Olá, mundo!" no console.
#
# 2 - Imprimindo variáveis:
# Imprimir o valor de variáveis usando a função print():
print("Exemplo 2:")
nome = "Alice"
idade = 30
print("Nome:", nome)
print("Idade:", idade)
print()
#
# 3 - Concatenação de Strings:
# usar o operador + para concatenar strings na função print():
print("Exemplo 3:")
primeiro_nome = "João"
sobrenome = "Silva"
print("Nome completo:", primeiro_nome + " " + sobrenome)
print()
#
# 4 - Formatando a saída:
# usar formatação para controlar a aparência da saída. 
# usando a função format() ou f-strings 
print("Exemplo 4:")
print("Usando format():")
nome = "Maria"
idade = 25
print("Nome: {}, Idade: {}".format(nome, idade))
print()
#
print("Usando f-strings:")
nome = "João"
idade = 22
print(f"Nome: {nome}, Idade: {idade}")
print()
#
# 5 - Múltiplas saídas:
# Imprimir várias expressões em uma única chamada à 
# função print() separando-as por vírgulas:
print("Exemplo 5:")
a = 5
b = 10
c = a + b
print("Valor de a:", a, "Valor de b:", b, "Soma de a e b:", c)
print()
#
# 6 - Parâmetros adicionais:
#A função print() tem alguns parâmetros adicionais que você pode
#  usar para controlar o comportamento da saída, como sep 
# (o separador entre os argumentos) e end (o que é impresso 
# após os argumentos)
print("Exemplo 6:")
a = 5
b = 10
print("a", a, "b", b, sep=":", end="\tFim\n")
print()
#
# "sequências de escape" e são usados para representar caracteres 
# não imprimíveis ou para controlar o formato da saída
#
# 1 - \\ - Barra Invertida:
print("Exemplo 1 - escape:")
print("Usar uma barra invertida: \\")
print()
#
# \' - Aspa Simples:
print("Exemplo 2 - escape:")
print('Isso é uma aspa simples: \'')
print()
#
# \" - Aspa Dupla:
print("Exemplo 3 - escape:")
print("Isso é uma aspa dupla: \"")
print()
#
# \n - Nova Linha (quebra de linha):
print("Exemplo 4 - escape:")
print("Primeira linha\nSegunda linha")
print()
#
# \t - Tabulação Horizontal:
print("Exemplo 5 - escape:")
print("Item\tPreço")
print("Maçã\t$1.00")
print("Banana\t$0.75")
print()
#
# \r Retorno de Carro:
# Imprimi apenas o conteúdo após o \r
print("Exemplo 6 - escape:")
print("12345\rABCD")
print("1234\rABCDF")
print("123456\rABCDF")
print()
#
# \b Backspace apaga o caractere aterior
print("Exemplo 7 - escape:")
print("Apagando\b este\b t\bexto")
print()
#
# \f Avanço de formulário
print("Exemplo 8 - escape:")
# A sequência de escape \f (alimentação de
# formulário) é usada para controlar a 
# formatação de saída, mas seu uso prático é
# limitado em ambientes de programação 
# modernos. Geralmente, é mais associada à 
# formatação em impressoras, e seu uso direto
# em aplicativos de software é raro.
texto_formatado = "Relatório de Vendas\n\n"
texto_formatado += "Data\t\tProduto\t\tQtd\tPreço\n"
texto_formatado += "2023-11-01\tProduto A\t10\t$100.00\n"
texto_formatado += "2023-11-02\tProduto B\t5\t$50.00\n"
texto_formatado += "2023-11-03\tProduto C\t8\t$80.00\n"
#
# Adicione uma alimentação de formulário no final
texto_formatado += "\f"
#
# Exiba o texto formatado
print(texto_formatado)
#
# OBS -> RARAMENTE USADO, APENAS PARA IMPRESSORA ANTIGA


