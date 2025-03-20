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

#list
x = ["apple", "banana", "cherry"]
print(x)
#tuple
x = ("grape", "avocado", "cocoa")
print(x)
#range
x = range(6)
#dict
x = {"nome" : "Rogério", "idade" : 45}
print(x)
#set
x = {"orange", "eggs", "meat"}
print(x)
#frozenset
x = frozenset({"cadeira", "mesa", "armário"})
print(x)
#bytes
x = b"Hello"
print(x)
#bytearray
x = bytearray(5)
print(x)
#memoryview
x = memoryview(bytes(5))
print(x)
#NoneType
x = None
print(x)

#numericos
#int
x = 15
print(x)
print(type(x))
y = 3565600026662245626298784662323232
print(y)
z = -3255
print(z)

#float, pode ser números científicos com um "e" para indicar a potência de 10
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

#complex
x = 3 + 5j
print(x)
y = 5j
print(y)
z = -5j
print(z)
print(type(z))

#Booleanos
print(10 > 9)
print(10 == 9)
print(10 < 9)
#bool
x = True
y = False
print(x)
print(y)
print(x and y)
print(x or y)
print(not(x))
print(type(x))

#str
x = "Rogerão Araújo"
print(x)
x = 'Rogerão Araújo'
print(x)
x = '''Rogerão Araújo'''
print(x)
x = """Rogerão Araújo"""
print(x)
print(type(x))