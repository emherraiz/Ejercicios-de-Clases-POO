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

#el primer print da la clase A
#el segundo print devolvera true porque se cumple
#el tercer print devuelve 0 porque le pasas una tupla
#el cuarto devuelve 1 porque llama a la funcion y de la clase a y le pasa la tupla con un elemento
#el quinto devuelve 2 porque llama a la funcion y de A donde en el self le pasa aa que es la clase a y luego una tupla de dos elementos
#el sexto devuelve 3 porque vuelve a hacer lo anterior pasando 3 elementos
