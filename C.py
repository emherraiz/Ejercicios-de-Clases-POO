# Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:

class A:
    def z(self):
        return self

    def y(self, t):
        return len(t)

a = A
y = a.z
print(y(a))
aa = a()
print(aa is a())
z = aa.y
print(z(()))
print(a().y((a,)))
print(A.y(aa, (a,z)))
print(aa.y((z,1,'z')))
