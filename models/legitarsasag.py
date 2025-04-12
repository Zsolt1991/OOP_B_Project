from models.jarat import Jarat
from typing import List, Optional

class Legitarsasag:
    def __init__(self, nev: str):
        self.nev = nev
        self.jaratok: List[Jarat] = []

    def hozzaad_jarat(self, jarat: Jarat) -> None:
        self.jaratok.append(jarat)

    def listaz_jaratokat(self) -> List[str]:
        return [jarat.info() for jarat in self.jaratok]

    def get_jarat(self, jaratszam: str) -> Optional[Jarat]:
        return next((j for j in self.jaratok if j.jaratszam == jaratszam), None)