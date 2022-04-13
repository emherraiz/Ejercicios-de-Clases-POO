class Test:
    def metodo(self, linea, resultado_final):
        return resultado_final + linea

class logger:

    def primera_linea(self):
        return '--Start log--'

    def linea_intermedia(self, numero_de_llamada):
        return f'\n{numero_de_llamada}a llamada'

    def ultima_linea(self, tamaño):
        return f'\n--End log: {tamaño} log(s)--'


def llamadas_a_una_funcion(tamaño):
    llamada = Test()
    proceso = logger()
    resultado_final = proceso.primera_linea()
    for i in range(tamaño):
        resultado_final = llamada.metodo(proceso.linea_intermedia(i+1), resultado_final)

    resultado_final = llamada.metodo(proceso.ultima_linea(tamaño), resultado_final)

    return resultado_final


print(llamadas_a_una_funcion(5))
