# strings
linguagem = "Python"
print(linguagem[2])
print(linguagem[-1])

# fatiamento de string
print(linguagem[0:3])
print(linguagem[:])
print(linguagem[:6])
print(linguagem[0:])
print(linguagem[::])

# fatiamento de string usando indices e passes negativos
print(linguagem[::-1])
print(linguagem[::2])
print(linguagem[-1:-4:-1])
print(linguagem[-1:-4:-2])
print(linguagem[-5:-1])
print(linguagem[-5:-1:2])

# nomes de variaveis permitidas e nao permitidas, essas ultimas comentadas
_name = "."
name123 = ""
name123name = ""
name_nome = ""
name_nome_name_nome_name123name = "" 
# name@ = ""
#name name = ""
# @name = ""
# name-name = ""
# 1name = ""

print(_name)

# métodos de string
nomeStr = " rogerao Araujo "
print("nomeStr: " + nomeStr)
# maiúscula
print(nomeStr.upper())
# minúscula
print(nomeStr.lower())
# primeiro caractere maiúsculo
print(nomeStr.capitalize())

print(nomeStr.replace(" ",""))
print(nomeStr.isnumeric())
print(nomeStr.index("j"))
print(nomeStr.index("Araujo"))

# remove espaço em branco do início ou do fim
print(nomeStr.strip())

# substitui uma string por outra
print(nomeStr.replace("rogerao", "Kal-El"))

linguagens = "Python, Java, C, C#, PHP"

# retorna uma lista
print(linguagens.split(","))
print(linguagens.split())

linguagens2 = ["Python", "Java", "C", "C#", "PHP", "Python"]

# pega todos os itens em uma coleção
xStr = "-".join(linguagens2)
print(xStr)

# retorna a quantidade de vezes que uma substring aparece em uma string
print(xStr.count("Python"))

yStr = ",".join(linguagens)
print(yStr)

strings = ["Olá, ", "mundo!"]
print(''.join(strings))
concatena = ''.join(strings)
print(concatena)

testaStr = "América do Sul"
print(testaStr.split(';'))
s1 = (testaStr.split(';')).pop().upper()
print(testaStr)
print(s1)

# Exercicio strip e split
a = " Hello World! "
print(a)
print(a.strip())
print(a.split())
b = a.split()
print(b[0])
print(b[1])

# Exercicio replace e count
seq = 'AUUCCUUCTGG'
seq = seq.replace('A','G')
# seq = 'GUUCCUUCTGG'
seq = seq.replace('U','T')
# seq = 'GTTCCTTCTGG'
G = seq.count('G')
# G = 3
C = seq.count('C') 
# C = 3
T = seq.count('T')
# T = 5
# print G, C, T # isso da erro, o correto seria
print(G, C, T)

# continuar em string IV 10:58 min