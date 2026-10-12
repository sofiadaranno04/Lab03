class Strumento:
    def __init__(self,codiceS,tipo,marca,anno_acquisto,valore):
        self.codiceS = codiceS
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = float(valore)

    def __str__(self):
        return f"{self.codiceS},{self.tipo},{self.marca},{self.anno_acquisto},{self.valore}"


