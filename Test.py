class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        Osoba.__init__(self, imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        Osoba.__init__(self, imie, wiek)
        self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium


class PracujacyStudent(Pracownik, Student):
    def __init__(self, imie, wiek, stawka, liczba_godzin, stypendium):
        Pracownik.__init__(self, imie, wiek, stawka, liczba_godzin)
        Student.__init__(self, imie, wiek, stypendium)

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin + self.stypendium
