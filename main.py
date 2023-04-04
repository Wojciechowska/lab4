import random
#zad1
dane = []
for i in range(10):
    dane.append(random.randint(0,30) * 2)
plik = open('liczby.txt', 'w+')
plik.writelines(str(dane))
plik.close()

#zad2
with open('liczby.txt', 'r') as plik1:
     zawartosc = plik1.read()
     print(zawartosc)

#zad3
with open('zdanie.txt', 'w') as plik2:
    plik2.writelines('Testowy tekst \n')
    plik2.writelines('który zostanie zapisany \n')
    plik2.writelines('w tym pliku \n')
    plik2.writelines('o nazwie zdanie.txt \n')
with open('zdanie.txt', 'r') as plik2:
    zawartosc2 = plik2.read()
    print(zawartosc2)

#zad4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print(f"Nazwa produktu: {self.nazwa_produktu}")
        print(f"Ilość: {self.ilosc} {self.jednostka_miary}")
        print(f"Cena za jednostkę: {self.cena_jed} zł")

    def ile_produktu(self):
        return f"{self.ilosc} {self.jednostka_miary}"

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

#zad5
class CiagArytmetyczny:
    def __init__(self):
        self.elementy = []

    def wyswietl_dane(self):
        print("Elementy ciągu:", self.elementy)
    def pobierz_elementy(self):
        n = int(input("Liczba elementów ciągu: "))
        self.elementy = [float(input(f"Podaj {i}-ty element ciągu: ")) for i in range(1, n + 1)]
    def pobierz_parametry(self):
        a1 = float(input("Pierwszy element ciągu: "))
        r = float(input("Różnica ciągu: "))
        n = int(input("Liczba elementów do wygenerowania: "))
        self.elementy = [a1 + i * r for i in range(n)]
    def policz_sume(self):
        suma = sum(self.elementy)
        print("Suma elementów ciągu: ", suma)
    def policz_elementy(self, a, r, n):
        self.elementy = [a + i * r for i in range(n)]
        print("Elementy ciągu: ", self.elementy)

ciag = CiagArytmetyczny()
ciag.pobierz_elementy()
ciag.wyswietl_dane()
ciag.pobierz_parametry()
ciag.wyswietl_dane()
ciag.policz_sume()
ciag.policz_elementy(1, 3, 5)

#zad6
class Robaczek:
    def __int__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        print("Aktualne współrzędne: x =", self.x, ", y =", self.y)

        roba = Robaczek(0, 0, 2)
        roba.idz_w_gore(4)
        roba.idz_w_lewo(3)
        roba.idz_w_dol(2)
        roba.idz_w_prawo(1)
        roba.pokaz_gdzie_jestes()