### Enunciado:
Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:

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

### Solucion

1 - Asignamos a 'y' la funcion 'z' dentro de la clase A. Esta funcion devuelve la propia clase a la que pertenece con un self, por lo que el print nos devolverá la propia clase y su modulo __main__ en el que se ha declarado la clase.

2 - Podría parecer que tiene que ser verdadero, sin embardo, estamos asignando al objeto 'aa' una instancia, es decir la llamada a un método (__init__).
Al asignar una nueva instancia de 'A', la dirección de memoria ya no es la misma.

3 - Asignamos a 'z' una funcion de la instancia 'aa' la cual nos devolverá el tamaño del elemento que le pasemos. En este caso es cero ya que le pasamos una tupla vacía.

4 - 'y' tiene que ser usado mediante una instancia, por la cual estamos devolviendo la longitud del elemento que le pasemos, en este caso le hemos pasado una tupla (se observa gracias a la coma), con un solo objeto por lo que el tamaño es 1.

5 - Llamamos a la funcion A.y donde observamos que el self, es la instancia que hace que el método funcione. Como argumento 't' le estamos pasando una tupla de dos elementos ('a' y 'z' los toma como dos objetos cualesquiera sin aplicarle ningún uso en este caso)

6 - Al se 'aa' una instancia e indicar que utilizamos el metodo 'y' comenzamos a trabajar directamente con este, al cual le pasamos una tupla de tres elementos y nos muestra el tamaño de esta tupla

