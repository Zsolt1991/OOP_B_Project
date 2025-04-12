from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: int, nev: str):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.nev = nev

    @abstractmethod
    def info(self) -> str:
        pass

class BelfoldiJarat(Jarat):
    def info(self) -> str:
        return f"Belföldi | {self.jaratszam} ({self.nev}) -> {self.celallomas} | Ár: {self.jegyar} Ft"

class NemzetkoziJarat(Jarat):
    def info(self) -> str:
        return f"Nemzetközi | {self.jaratszam} ({self.nev}) -> {self.celallomas} | Ár: {self.jegyar} Ft"