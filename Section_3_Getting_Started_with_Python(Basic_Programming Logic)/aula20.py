# Criar Verificador de CPF
#

# Verificar se o valor de entrada, representa um cpf, com 11 digitos numericos

while True:
    cpf_verificar = input("\nInforme o cpf: ")
    cpf_verificar = cpf_verificar \
        .replace('.', '')  \
        .replace(' ', '') \
        .replace('-', '')
        

    try:
        if len(cpf_verificar) == 11:
            qtd = True
        if ((cpf_verificar.isdigit ) and (qtd == True)):
            break
    except:
        print("\nValor informado não representa um cpf: ")


# Verficar a regiao


regiao = [['RS'], ['DF, GO, MS, MT e TO'], ['AC, AM, AP, PA, RO e RR'],
          ['CE, MA e PI'], ['AL, PB, PE, RN'], ['BA e SE'], ['MG'],
          ['ES e RJ'], ['SP'], ['PR e SC']]

# Primeiro Digito

i = 10
j = 0
soma_dig1 = 0
while i >= 2:

    soma_dig1 += i * int(cpf_verificar[j])
    i -= 1
    j += 1

digito1 = 11 - (soma_dig1 % 11) if soma_dig1 % 11 > 1 else 0




# Segundo digito

i = 10
j = 1

soma_dig2 = 0
while i >= 2:
    soma_dig2 += i * int(cpf_verificar[j])
    i -= 1
    j += 1

digito2 = 11 - (soma_dig2 % 11) if soma_dig2 % 11 > 1 else 0

print("\nPara esse cpf:")
print(f"O primeiro digito é {digito1}: ")
print(f"O Segundo digito é {digito2}:\nLOGO:\n---------------------\n")
if((int(cpf_verificar[9]) == digito1) and  (int(cpf_verificar[10]) == digito2)):
    print(f"O CPF: {cpf_verificar} é valido\nEmitido em {regiao[int(cpf_verificar[8])]}")
else:
    print("CPF INVALIDO")




# ABC.DEF.GH I - J K
# 012.345.67 8 - 9 10


# Considerando o cpf: ABC.DEF.GHI-JK.
# Os primeiros oito dígitos, ABCDEFGH, formam o número-base
# definido pela Receita Federal no momento da inscrição.
#
# O nono dígito, I, define a Região Fiscal responsável pela inscrição.
#
# O penúltimo, J, é o dígito verificador dos nove primeiros.
#
# O último, K, é o dígito verificador dos noves anteriores a ele.
#
