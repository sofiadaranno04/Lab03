from strumento import Strumento
from operator import attrgetter
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self._resposabile = responsabile
        self.strumenti = {}
        self.prestiti ={}

    #Getter per il responsabile--> creiamo una proprità responsabile per leggerlo e modificarlo come se fosse un normale attributo
    @property
    def responsabile(self):
        return self._resposabile

    @responsabile.setter
    def responsabile(self, nuovo_responsabile):
        self._resposabile = nuovo_responsabile

        # TODO

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            with open(file_path,"r") as file:
                for riga in file:
                    riga = riga.strip() #eliminiamo gli spazi
                    if not riga:    #saltiamo eventuali righe vuote
                        continue
                    parti = riga.split(",")
                    if len(parti) ==5:
                    #codice,tipo,marca,anno,valore = parti
                        codiceS = parti[0]
                        tipo = parti[1]
                        marca = parti[2]
                        anno_acquisto = int(parti[3])
                        valore = float(parti[4])
                    #creiamo l'oggetto Strumento e lo salviamo nel dizionario del deposito
                        nuovo_strumento = Strumento(codiceS, tipo, marca, anno_acquisto, valore)
                        self.strumenti[codiceS] = nuovo_strumento

        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} non trovato")



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        # Partiamo contando quanti strumenti ci sono già nel dizionario e aggiungiamo 1
        # Esempio: se ci sono 3 strumenti, il prossimo sarà il numero 4
        prossimo_num = len(self.strumenti) + 1

        # Facciamo un controllo di sicurezza nel caso in cui un codice esista già
        # (se per esempio sono stati cancellati o caricati file con buchi nei numeri)
        codiceS = f"S{prossimo_num}"
        while codiceS in self.strumenti:
            prossimo_num += 1
            codiceS = f"S{prossimo_num}"

        # Creiamo l'oggetto Strumento
        nuovo_strumento = Strumento(codiceS, tipo, marca, int(anno_acquisto), float(valore))

        # Lo salviamo nel dizionario del deposito
        self.strumenti[codiceS] = nuovo_strumento

        # Restituiamo il riferimento allo strumento aggiunto
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        # 1. Prendiamo tutti i valori (gli oggetti Strumento) dal dizionario self.strumenti
        lista_strumenti = list(self.strumenti.values())

        # 2. Ordiniamo la lista usando sorted() e attrgetter('marca')
        # attrgetter('marca') dice a Python di guardare l'attributo 'marca' di ogni oggetto Strumento per fare il confronto
        strumenti_ordinati = sorted(lista_strumenti, key=attrgetter('marca'))

        # 3. Restituiamo la lista ordinata
        return strumenti_ordinati

    def nuovo_prestito(self, codice_strumento, nominativo, data_prestito):
        """Crea un nuovo prestito"""
        # TODO
        # 1. Controlliamo se lo strumento esiste nel deposito
        if codice_strumento not in self.strumenti:
            raise ValueError(f"Errore: Lo strumento con codice {codice_strumento} non esiste nel deposito.")

        # 2. Controlliamo se lo strumento è già attualmente in prestito
        if codice_strumento in self.prestiti:
            raise ValueError(f"Errore: Lo strumento {codice_strumento} risulta già in prestito.")

        # 3. Creiamo l'oggetto Prestito (passando i dati necessari)
        prestito = Prestito(codice_strumento, nominativo, data_prestito)

        # 4. Memorizziamo il prestito nel dizionario dei prestiti usando il codice dello strumento come chiave
        self.prestiti[codice_strumento] = prestito

        # 5. Restituiamo l'oggetto prestito appena creato
        return prestito

    def termina_prestito(self, codice_strumento):
        """Termina un prestito in atto"""
        # TODO

        # 1. Controlliamo se lo strumento risulta effettivamente in prestito
        if codice_strumento not in self.prestiti:
            raise ValueError(f"Errore: Lo strumento con codice {codice_strumento} non risulta attualmente in prestito.")

        # 2. Rimuoviamo il prestito dal dizionario usando pop()
        prestito_conclusi = self.prestiti.pop(codice_strumento)

        # 3. Restituiamo l'oggetto prestito appena concluso
        return prestito_conclusi
