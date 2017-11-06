import sqlite3
import time

# Baza, v katero vstavljamo.
baza = "banka1.db"

class BancniTerminal:
    def __init__(self):
        self.oseba = None
        self.racun = None
        self.cur = None # Ga ustvarimo, ko zaženemo bazo
        self.menu = "glavni" # Beleži, v katerem meniju smo.
        self.zazeni()

    def zazeni(self):

        with sqlite3.connect(baza) as con:
            self.cur = con.cursor()

            while True: # Obračalnik menijev
                if self.menu == "glavni":
                    self.glavniMenu()
                elif self.menu == "oseba":
                    self.izberiOsebo()
                elif self.menu == "dodajOsebo":
                    self.dodajOsebo()
                elif self.menu == "izpisRacunov":
                    self.izpisRacunov()
                    
    def glavniMenu(self):
        print("_"*10)
        print("O - Pregled Osebe")
        print("X - Izhod")
        izbira = input("> ").strip()
        if izbira.lower() == "o":
            self.menu = "oseba"
        elif izbira.lower() == "x":
            exit()

    def izberiOsebo(self):
        ime = input("Ime osebe: ")
        self.cur.execute("SELECT EMSO, Priimek, Ime FROM Oseba WHERE Ime LIKE ?", ("%" + ime + "%",))
        # print(cur.fetchall())
        stevec = 0
        print("Izberi številko pred osebo ali drugo akcijo.")
        osebe = self.cur.fetchall()
        for emso, ime, priimek in osebe:
            print(stevec, priimek, ime, emso)
            stevec += 1
        print("D - Dodaj osebo")
        print("N - Nazaj")
        izbira = input("> ")
        if izbira.lower() == "d":
            self.menu = "dodajOsebo"
            return # Ni nujno, a je lepo
        elif izbira.lower() == "n":
            self.menu = "glavni"
            return
        elif izbira.isdigit():
            n = int(izbira) - 1
            if n >= 0 and n < len(osebe):
                self.oseba = osebe[n]
                self.izpisRacunov()
            

    def dodajOsebo(self):
        print("Zdaj bi rad dodal osebo")
        oseba = input("Vpiši osebo: ")
        (emso, ime, priimek, ulica, hisna_st, posta) = oseba.split()
        # Tu jo dodamo

    def izpisRacunov(self):
        print("Izpis racunov za", self.oseba)
        self.menu = "glavni"

        

BancniTerminal()


