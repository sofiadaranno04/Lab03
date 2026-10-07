class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.resposabile = responsabile
        self.strumenti = {}
        self.prestiti ={}

        # TODO

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        with open(file_path,"r") as file:
            for riga in file:
                riga = riga.strip()
                if riga:
                    parti = riga.split(",")
                    id_strumento = parti[0]
                    tipo = parti[1]
                    marca = parti[2]
                    anno_acquisto = int(parti[3])
                    valore = float(parti[4])



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        max_id = 0
        for id_str in self.strumenti:
            num = int(id_str(1:))#estraggo parte numerica dopo la S
            if num > max_id
                max_id = num
        nuovo_id = f"S{max_id + 1}"


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti, key=lambda strumento: strumento.marca)

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
