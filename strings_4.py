# startswith 

x = "Rogério Araújo"
print(x.startswith("Rogério"))
print(x.startswith("Kal-El"))

# isidentifier

a = "ab"
b = "a_b"
c = "_a_b"
d = "aB"
e = "AB"
f = "ab2"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print(e.isidentifier())
print(f.isidentifier())

c2 = "1ab"
d2 = "a-b"
e2 = "a b"
f2 = "$ab"
print(c2.isidentifier())
print(d2.isidentifier())
print(e2.isidentifier())
print(f2.isidentifier())

# exercicios

linguagens = "Python, Java, C, C#, PHP, Python, Python"
print(linguagens.startswith("Python"))
print(len(linguagens))
print(linguagens.count("Python"))

x = "str"
y = "15str"
z = "15"

# isalpha
print(x.isalpha())
# isalnum
print(y.isalnum())
# isnumeric
print(z.isnumeric())

x = "Rogério Araújo"

# index
print(x.index("Araújo"))
#print(x.index("Kal-El")) #vai gerar exceção

# find
print(x.find("Araújo"))
print(x.find("Kal-El"))
print(x.find("Araújo", 0, 6))
print(x.find("Araújo", 7, 14))
print(x.find("Araújo", 7))

# exercicios

frase = "João da Silva é casado e mora numa casa. A casa do casal é bonita"
print(frase.find("casa"))
print(frase.find("casa", 43, 56))
print(type(frase.find("casa", 43, 56)))
print(type(frase.isalnum()))