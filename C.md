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

#### Solucion

1 - Asignamos a 'y' la funcion 'z' dentro de la clase A. Esta funcion devuelve la propia clase a la que pertenece con un self, por lo que el print nos devolverá la propia clase y su modulo __main__ en el que se ha declarado la clase.

2 - Podría parecer que tiene que ser verdadero, sin embardo, estamos asignando al objeto 'aa' una instancia, es decir la llamada a un método (__init__).
Al asignar una nueva instancia de 'A', la dirección de memoria ya no es la misma.

3 - 
