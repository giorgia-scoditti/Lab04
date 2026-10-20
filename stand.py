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

    def calcola_prezzo(self):
        return self.prezzo

    def __str__(self):
        return f"{self.__codice_stand} | Superficie: {self.__superficie} mq, Padiglione: {self.__padiglione}, Prezzo base: {float(self.__prezzo):.2f} euro"


class StandConPreseAggiuntive(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, num_prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__num_prese = int(num_prese)

    def calcola_prezzo(self):
        return self.prezzo * (1 + 0.07 * self.__num_prese)

    def __str__(self):
        return f"{super().__str__()}, Prese aggiuntive: {self.__num_prese}, Prezzo finale: {float(self.calcola_prezzo()):.2f} euro"


class StandPremium(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__posizione = posizione

    def calcola_prezzo_finale(self):
        return self.prezzo * 1.30

    def __str__(self):
        return f"{super().__str__()}, Posizione: {self.__posizione}, Prezzo finale: {float(self.calcola_prezzo_finale()):.2f} euro"