
import unicodedata
import sys
class palindromo:
    def __init__(self,palabra):
        self.palabra = palabra
    def test(self):
        self.palabra=self.palabra.lower()
        self.palabra=self.palabra.replace(" ","")
        caracteres=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
        self.palabra_normalizado=unicodedata.normalize("NFD",self.palabra)
        self.palabra=self.palabra_normalizado.translate(caracteres)
        longitud=len(self.palabra)
        if longitud%2==0:
            izquierda=self.palabra[:longitud//2]
            derecha=self.palabra[longitud//2:]
            return f'{izquierda==derecha[::-1]}\n{self.palabra.upper()}'
        else:
            izquierda=self.palabra[:longitud//2]
            derecha=self.palabra[longitud//2+1:]
            return f'{izquierda==derecha[::-1]}\n{self.palabra.upper()}'



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

p=palindromo("atar a la rata")
print(p.test())
p=palindromo("capullo")
print(p.test())