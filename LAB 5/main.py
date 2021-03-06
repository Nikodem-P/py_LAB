class Kształty():
#definicja konstruktora
    def __init__(self, x, y):
    #deklarujemy atrybuty
    #self wskazuje że chodzi o zmienne własnie definiowanej klasy
        self.x = x
        self.y = y
        self.opis = "To jest klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik


#klasa która dziedziczy po klasie Kształty
class Kwadrat(Kształty):
    def __init__(self,x):
        self.x = x
        self.y = x
        # i jeszcze klasa, która dziedziczy po klasie Kwadrat
        # bedzie definiwoać figurę złożoną z 3 kwadratów w kształcie litery L
        #  _
        # | |_
        # |_ _|


class KwadratLiteraL(Kwadrat):
    def obwod(self):
        return 8 * self.x

    def pole(self):
        return 3 * self.x * self.y

#inicjujemy klasę Kwadrat
kwadrat = Kwadrat(5)
#sprawdzenie metod z klasy bazowej
print(kwadrat.obwod())
print(kwadrat.pole())
kwadrat.dodaj_opis("Nasza figura to kwadrat")
print(kwadrat.opis)
kwadrat.skalowanie(0.3)
print(kwadrat.obwod())
print("")
#inicjujemy klasę KwadratLiteraL
litera_l = KwadratLiteraL(5)
print(litera_l.obwod())
print(litera_l.pole())
litera_l.dodaj_opis("Litera L")
print(litera_l.opis)
litera_l.skalowanie(0.5)
print(litera_l.obwod())


class Kwadrat(Kształty):
    def __init__(self,x):
        self.x = x
        self.y = x
        kwadrat = Kwadrat(5)
        print(kwadrat)


class Kwadrat(Kształty):
    def __init__(self,x):
    self.x = x
    self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)
        kwadrat = Kwadrat(5)
        print(kwadrat)


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
    # wywołanie konstruktora klasy bazowej
    Osoba.__init__(self, imie, nazwisko)
    # lub drugi sposób
    # super().__init__(imie, nazwisko)
    self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):
    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

jozek = Pracownik('Józef', 'Bajka', 2000)
adrian = Menadzer('Adrian', 'Mikulski', 12000)
print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imieself.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik:
    def __init__(self, pensja):
        self.pensja = pensja


class Menadzer(Osoba, Pracownik):
        def __init__(self, imie, nazwisko, pensja):
            Osoba.__init__(self, imie,nazwisko)
            Pracownik.__init__(self, pensja)

        def przedstaw_sie(self):
            return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


adrian = Menadzer("Adrian", "Mikulski", 12000)
print(adrian.przedstaw_sie())
