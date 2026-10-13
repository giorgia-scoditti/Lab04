class Stand:
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        self.__codice_stand = codice_stand
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo

    def __str__(self):
        return f"{self.__codice_stand}, Superficie: {self.__superficie}, Padiglione: {self.__padiglione}, Prezzo: {float(self.__prezzo):.2f}"

class StandConPreseAggiuntive(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, num_prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__num_prese = num_prese

    def calcola_prezzo(self):
        return self.prezzo * (1 + 0.07 * self.__num_prese)

    def __str__(self):
        return f"{super().__str__()}, Prese aggiuntive: {self.__num_prese}, Prezzo finale: {float(self.calcola_prezzo()):.2f}"

class StandPremium(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        # CONTINUA