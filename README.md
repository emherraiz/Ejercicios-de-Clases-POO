# Ejercicios-de-Clases-POO

Entrega por Parejas: UML Y CÓDIGO

a. Palíndromo - método de clase

Enunciado: crear una clase Palindromo que contenga un método de clase esPalindromo(), que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda. Se tienen en cuenta los caracteres no alfanuméricos.

Comportamiento esperado:

print(Palindromo.esPalindromo('radar')) 
>>> True 
print(Palindromo.esPalindromo('sonar')) 
>>> False 
print(Palindromo.esPalindromo('Arde ya la yedra')) 
>>> False 
print(Palindromo.esPalindromo('Ardeyalayedra')) 
>>> True 
print(Palindromo.esPalindromo('!@#$% %$#@!')) 
>>> True 
print(Palindromo.esPalindromo('L O L')) 
>>> True 

b. Palíndromo - método de instancia

Enunciado: en esta misma clase Palindromo, añada un atributo que se inicializará en el constructor. Añada también un método test() que pruebe si el atributo de la instancia es un palíndromo. Además, al destruir la instancia, muestre el atributo en mayúsculas.

Comportamiento esperado:

p = Palindromo("radar") 
print(p.test()) 
>>> True 
p = Palindromo("sonar") 
>>> RADAR 
print(p.test()) 
>>> False 
SONAR 
Pregunta adicional: ¿por qué se muestra RADAR después de la instanciación Palindromo("sonar")?

c. Puzzle
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

d. Logger

Enunciado: escriba una clase Logger, cuyo objetivo sea escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje). La primera línea del archivo debe ser "--Start log--", seguida de los mensajes recibidos por el método log en la parte superior de un mensaje por línea, y la última línea del archivo, escrita cuando se destruye la instancia de Logger, debe ser "--End log: x log (s) -" donde x es el número de llamadas al método log. Esta clase Logger se utilizará en un método llamada() de una clase Test.

Comportamiento esperado:

test = Test() 
for i in range(1, 6): 
   if i == 1: 
       test.llamada("Primera llamada") 
   else: 
       test.llamada("{}ª llamada".format(string)) 
$> cat log.txt 
--Start log-- 
Primera llamada 
2a llamada 
3a llamada 
4a llamada 
5a llamada 
--End log: 5 log(s)-- 
