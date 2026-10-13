from stand import Stand
from espositore import Espositore


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome

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
        file = open(file_path, "r", encoding=utf-8)
        for riga in file:
            dati = riga.strip().split(",")
            if len(dati) == 3:


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
