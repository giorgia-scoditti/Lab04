from stand import Stand
from stand import StandConPreseAggiuntive
from stand import StandPremium
from espositore import Espositore


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.stand_base = {}
        self.stand_con_prese = {}
        self.stand_premium = {}
        self.espositori = {}
        self.stand_assegnato_a_espositore = {}
        self.tutti_gli_stand = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def __str__(self):
        return f"{self.__nome}"


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            file = open(file_path, "r")
            for riga in file:
                dati = riga.strip().split(",")
                if len(dati) == 3:
                    codice_espositore = dati[0]
                    nome_espositore = dati[1]
                    cognome_espositore = dati[2]
                    if codice_espositore not in self.espositori:
                        espositore = Espositore(codice_espositore, nome_espositore, cognome_espositore)
                        self.espositori[codice_espositore] = espositore
                elif len(dati) > 3:
                    codice_stand = dati[0]
                    superficie = float(dati[1])
                    padiglione = int(dati[2])
                    prezzo = float(dati[3])
                    if len(dati) == 4:
                        if codice_stand not in self.stand_base:
                            stand_base = Stand(codice_stand, superficie, padiglione, prezzo)
                            self.stand_base[codice_stand] = stand_base
                    elif len(dati) == 5 and dati[4].isdecimal():
                        num_prese = dati[4]
                        if codice_stand not in self.stand_con_prese:
                            stand_con_prese = StandConPreseAggiuntive(codice_stand, superficie, padiglione, prezzo, num_prese)
                            self.stand_con_prese[codice_stand] = stand_con_prese
                    elif len(dati) == 5 and dati[4].isalpha():
                        posizione = dati[4]
                        if codice_stand not in self.stand_premium:
                            stand_premium = StandPremium(codice_stand, superficie, padiglione, prezzo, posizione)
                            self.stand_premium[codice_stand] = stand_premium
            file.close()
        except FileNotFoundError:
            print(f"File non trovato.")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand in self.stand_base or codice_stand in self.stand_con_prese or codice_stand in self.stand_premium:
            if codice_espositore in self.espositori:
                if codice_stand in self.stand_assegnato_a_espositore.keys():
                    raise Exception(f"Lo stand {codice_stand} non è disponibile.")
                if codice_espositore in self.stand_assegnato_a_espositore.values():
                    raise Exception(f"L'espositore {codice_espositore} è già associato ad un altro stand.")
                if codice_stand not in self.stand_assegnato_a_espositore and codice_espositore not in self.stand_assegnato_a_espositore:
                    self.stand_assegnato_a_espositore[codice_stand] = codice_espositore
                    return self.stand_assegnato_a_espositore[codice_stand]


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.espositori:
            if espositore in self.stand_assegnato_a_espositore.values():
                for stand in self.stand_assegnato_a_espositore.keys():
                    if self.stand_assegnato_a_espositore[stand] == espositore:
                        print(f"{espositore}, {stand}")
            else:
                print(espositore)


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        for stand in self.stand_base.values():
            if stand not in self.tutti_gli_stand:
                self.tutti_gli_stand.append(stand)
        for stand in self.stand_con_prese.values():
            if stand not in self.tutti_gli_stand:
                self.tutti_gli_stand.append(stand)
        for stand in self.stand_premium.values():
            if stand not in self.tutti_gli_stand:
                self.tutti_gli_stand.append(stand)
        lista_ordinata = sorted(self.tutti_gli_stand, key=lambda stand : stand.calcola_prezzo())
        return lista_ordinata
