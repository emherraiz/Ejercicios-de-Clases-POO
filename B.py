class palindromo:
    def __init__ (self,palabra):
        self.palabra=palabra

    def test(self):
        comprobar = True
        izquierda= 0
        derecha= len(self.palabra)-1

        while izquierda != derecha:
            if self.palabra[izquierda] == self.palabra[derecha]:
                izquierda = izquierda + 1
                derecha = derecha - 1
            else:
                comprobar = False
                break

        if comprobar == True:
            return True
        else:
            return False

p=palindromo("radar".lower())
print(p.test())
