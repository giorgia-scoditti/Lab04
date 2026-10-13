class Espositore:
    def __init__(self, codice_espositore, nome_espositore, cognome_espositore):
        self.__codice_espositore = codice_espositore
        self.__nome_espositore = nome_espositore
        self.__cognome_espositore = cognome_espositore

    def __str__(self):
        return f"{self.__codice_espositore}, {self.__nome_espositore}, {self.__cognome_espositore}"
