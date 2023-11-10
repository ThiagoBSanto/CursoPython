"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Thiago'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))


Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str

variavel = 'Olá mundo'
print(variavel[::-1])
"""

# EXERCICIO

nome = input("Informe seu nome: ")
idade = input("Informe a idade")

if ((nome == "") or (idade == "")):
     print("Desculpe, você deixou campos vazios.")
    
else:

   #imprimir nome
    print(f"Seu nome é {nome}")

    #imprimir nome invertido
    print(f"Seu nome invertido é {nome[-1::-1]}")

    #verifica se há espaços no nome
    if(" " in nome):
        print("Seu nome possui espaço")
    else:
        print("Seu nome não possui espaço")

    #quantidade de letras do nome
    qtd = 0
    for caracter in nome:
        if caracter == " ":
            qtd +=1
    print(f"Seu nome possui {len(nome) - qtd} letras")

    print(f"A primeira letra do seu nome é {nome[0]}")

    print(f"A última letra do seu nome é {nome[len(nome)-1]}")