#
#
# ***********   FORMATAÇÃO STRINGS    ***********
#
## 1 - Formatando a saída:
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
# Quantificar as casas decimais
# usamos :.nf
# onde o n é a quantidade de casa decimais desejadas

altura = 1.789
print(f" altura: {altura:.2f}")
print()