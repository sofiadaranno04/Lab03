
class Prestito:
    def __init__(self,id_prestito,data,codiceS,cognome_studente):
     self.id_prestito = id_prestito
     self.data = data
     self.codiceS = codiceS
     self.cognome_studente = cognome_studente

    def __str__(self):
        return f"Prestito [{self.id_prestito}]: Strumento {self.codiceS} affidato a {self.cognome_studente} in data {self.data}"
