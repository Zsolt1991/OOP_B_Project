from models.jarat import BelfoldiJarat, NemzetkoziJarat
from models.legitarsasag import Legitarsasag
from models.jegy_foglalas import JegyFoglalas
from datetime import date, timedelta

def betoltott_adatok():
    legitarsasag = Legitarsasag("Python Airlines")

    # 3 járat
    j1 = BelfoldiJarat("HUN101", "Debrecen", 15000, "Debreceni gyors")
    j2 = NemzetkoziJarat("INT202", "London", 80000, "Budapest–London expressz")
    j3 = NemzetkoziJarat("INT303", "Párizs", 95000, "Budapest–Párizs éjszakai")

    legitarsasag.hozzaad_jarat(j1)
    legitarsasag.hozzaad_jarat(j2)
    legitarsasag.hozzaad_jarat(j3)

    foglalasok = JegyFoglalas()
    datum = date.today() + timedelta(days=7)

    foglalasok.foglalas(j1, "Kiss Anna", datum)
    foglalasok.foglalas(j1, "Nagy Péter", datum)
    foglalasok.foglalas(j2, "Szabó Dóra", datum)
    foglalasok.foglalas(j3, "Tóth Gábor", datum)
    foglalasok.foglalas(j3, "Kovács Lili", datum)
    foglalasok.foglalas(j2, "Bognár Márk", datum)

    return legitarsasag, foglalasok