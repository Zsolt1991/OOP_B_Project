from typing import List, Tuple
from models.jarat import Jarat
from datetime import date

class JegyFoglalas:

    def __init__(self):
        self.foglalasok: List[Tuple[Jarat, str, date]] = []

    def foglalas(self, jarat: Jarat, nev: str, datum: date) -> int:
        if datum < date.today():
            raise ValueError("A megadott dátum már elmúlt.")
        self.foglalasok.append((jarat, nev, datum))
        return jarat.jegyar

    def lemondas(self, jaratszam: str, nev: str) -> bool:
        for foglalas in self.foglalasok:
            if foglalas[0].jaratszam == jaratszam and foglalas[1] == nev:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def listaz_foglalasokat(self) -> List[str]:
        return [f"{f[1]} | {f[0].info()} | Dátum: {f[2]}" for f in self.foglalasok]