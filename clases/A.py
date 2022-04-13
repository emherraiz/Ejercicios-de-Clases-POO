import unicodedata
import sys
class palindromo:

    def esPalindromo(x):
        x=x.lower()
        x=x.replace(" ","")
        caracteres=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
        x_normalizado=unicodedata.normalize("NFD",x)
        x=x_normalizado.translate(caracteres)
        longitud=len(x)
        if longitud%2==0:
            izquierda=x[:longitud//2]
            derecha=x[longitud//2:]
            return izquierda==derecha[::-1]
        else:
            izquierda=x[:longitud//2]
            derecha=x[longitud//2+1:]
            return izquierda==derecha[::-1]

print(palindromo.esPalindromo("cerda"))
