from asyncio.log import logger


class Logger:

    def log(palabra):
        archivo = str(input("Introduce el nombre del archivo al que se va a escribir: "))
        f = open(archivo, "w")
        for i in range(1,6):
            if i == 1:
                f.write(f'--Start log--\nprimera {palabra}\n')
            else:
                f.write(f'{i}º {palabra}\n')

        f.write("--End log: ")
        f.write(str("5"))
        f.write(" log(s)-- ")
        f.close()

Logger.log("llamada")
