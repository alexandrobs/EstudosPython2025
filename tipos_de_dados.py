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