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
                    superficie = dati[1]
                    padiglione = dati[2]
                    prezzo = dati[3]
                    if len(dati) == 4:
                        if codice_stand not in self.stand_base:
                            stand_base = Stand(codice_stand, superficie, padiglione, prezzo)
                            self.stand_base[codice_stand] = stand_base
                        if len(dati) == 5 and dati[4].isalnum():
                            nume_prese = dati[4]
                            if codice_stand not in self.stand_con_prese:
                                stand_con_prese = StandConPreseAggiuntive(codice_stand, superficie, padiglione, prezzo, nume_prese)
                                self.stand_con_prese[codice_stand] = stand_con_prese
                                # CONTINUA

        except FileNotFoundError:
            print("File non trovato.")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
