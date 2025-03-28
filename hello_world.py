# Hello World em Python - Estudos Python em 2025

print("Hello, World!")

# A importância da indentação em python e o correto número de tabulação para padrão de código e evitar o erro IndentationError

x = 15
y = 100
if x > y:
    print("x é maior que y")
else:
    print("x é menor que y")

# Expressões, instruções, blocos e tipo da linguagem
x = 15
print("x: " + str(x))

y = (x + 10) / 100
if x > y:
    print("x: "+ str(x) + " | y: " + str(y))

passei = False
if passei:
    print("Churrasco garantido!")
else:
    print("Não foi dessa vez.")
    print("É aprender com os erros e continuar!")

# Blocos contém instruções que por sua vez contém expressões, que criam, manipulam e exibem objetos e variáveis

# Variáveis e constantes - dinamicamente tipada - case-sentitive - ilimitado tamanho - 
x = 15
y = "Rogerão Araújo"
z = 1.84
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
ab = "Python"
a_b = "Python"
_a_b = "Python"
aB = "Python"
AB = "Python"
ab2 = "Python"
print(ab)
print(a_b)
print(_a_b)
print(aB)
print(AB)
print(ab2)

# Tipos de dados e strings, 
# numericos: int, float e complex, 
# bool, 
# str,
# sequência: list, tuple, range
# mapeamento: dict
# conjunto: set, frozenset
# binários: bytes, bytearray, memoryview
# nenhum tipo: NoneType

# list
x = ["apple", "banana", "cherry"]
print(x)
# tuple
x = ("grape", "avocado", "cocoa")
print(x)
#range
x = range(6)
# dict
x = {"nome" : "Rogério", "idade" : 45}
print(x)
# set
x = {"orange", "eggs", "meat"}
print(x)
# frozenset
x = frozenset({"cadeira", "mesa", "armário"})
print(x)
# bytes
x = b"Hello"
print(x)
# bytearray
x = bytearray(5)
print(x)
# memoryview
x = memoryview(bytes(5))
print(x)
# NoneType
x = None
print(x)

# numericos
# int
x = 15
print(x)
print(type(x))
y = 3565600026662245626298784662323232
print(y)
z = -3255
print(z)

# float, pode ser números científicos com um "e" para indicar a potência de 10
x = 1.84
print(x)
z = 35e3
print(z)
y = 12E4
print(y)
z = -87.7e100
print(z)
a = -35.59
print(a)
print(type(a))

# complex
x = 3 + 5j
print(x)
y = 5j
print(y)
z = -5j
print(z)
print(type(z))

# Booleanos
print(10 > 9)
print(10 == 9)
print(10 < 9)
# bool
x = True
y = False
print(x)
print(y)
print(x and y)
print(x or y)
print(not(x))
print(type(x))

# str
# strings de 1 linha apenas
x = "Rogerão Araújo1"
print(x)
x = 'Rogerão Araújo2'
print(x)

# strings de mais de uma linha Docstrings
x = '''Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3
Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3
Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3'''
print(x)
x = """Rogerão Araújo4 Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3
Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3
Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo3 Rogerão Araújo4"""
print(x)
print(type(x))

# Tipos de dados 2 - Casts

# int()
print(int(15))
print(int(1.84))
print(int("3"))

# float()
print(float(15))
print(float(1.84))
print(float("3"))

# complex()
a = complex(15)
print(a)
b = complex(15.7)
print(b)
c = complex("15")
print(c)
d = complex(15,7)
print(d)
e = complex('15+7j')
print(e)
f = complex(15,7) + (10+3j)
print(f)

# bool()
print(bool(15))
print(bool(1.84))
print(bool("str1"))
print(bool("False"))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))

# str()
print(str(15))
print(str(1.84))
print(str("str1"))

# exercícios tipos de dados 2

r = 10
i = 7
c = complex(r, i) + (6 + 3j)
print(c)

x = bool(-3)
y = bool("True"*x)
z = bool("False")
print(x and y and z)

# Strings
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
print(nomeStr.upper())
print(nomeStr.lower())
print(nomeStr.capitalize())

print(nomeStr.replace(" ",""))
print(nomeStr.isnumeric())
print(nomeStr.index("j"))
print(nomeStr.index("Araujo"))

print(nomeStr.strip())
print(nomeStr.replace("rogerao", "Kal-El"))

linguagens = "Python, Java, C, C#, PHP"

print(linguagens.split(","))
print(linguagens.split())

linguagens2 = ["Python", "Java", "C", "C#", "PHP", "Python"]

xStr = "-".join(linguagens2)
print(xStr)
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