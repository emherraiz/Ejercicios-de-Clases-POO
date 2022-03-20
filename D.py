from asyncio.log import logger


class Logger:

    def log(palabra):
        archivo = str(input("Introduce el nombre del archivo al que se va a escribir: "))
        max_len = 6
        f = open(archivo, "w")
        for i in range(max_len):
            if i == 0:
                f.write("--Start log-- \n")
            else:
                f.write(palabra)
                f.write("\n")

        f.write("--End log: ")
        f.write(str(max_len))
        f.write(" log(s)-- ")
        f.close()

Logger.log("palabra")
