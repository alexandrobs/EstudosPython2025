#startswith 

x = "Rogério Araújo"
print(x.startswith("Rogério"))
print(x.startswith("Kal-El"))

#isidentifier

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

# teste para ver se está rastreando corretamente as alterações no github