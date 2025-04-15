# strings - parte 2

# instrução que retorna SU
s = 'IFSUL'
print(s[-3:-1])

# instrução que exibe "MU"
s2 = "ALO MUNDO"
print(s2[-5:-3])

# len
nome = " Rogerão Araújo "
print (len(nome))

# operador in e not in
frutas = "abacaxi, laranja, maça"
print("maça" in frutas)
print("melancia" in frutas)
print("maça" not in frutas)
print("melancia" not in frutas)

# concatenação de strings com cast e sem cast, multiplicando a string
x2 = "Rogerão"
y2 = " Araújo"
z2 = x2 + y2
print(z2)

x3 = "11"
y3 = 4
print(x3 + str(y3))
print(int(x3) + y3)

print(x2 * y3)

a3 = 3
b3 = "ANP"
print(a3 * b3)

b4 = " BNB "
print(a3 * b4)