from clases.A import palindromo
from clases.B import palindromo2
from clases.D import Test,logger,llamadas_a_una_funcion

if __name__ == '__main__':
    print(palindromo.esPalindromo("cerda en salsa"))

    p=palindromo2("atar a la rata")
    print(p.test())
    p=palindromo2("capullo")
    print(p.test())

    print(llamadas_a_una_funcion(5))