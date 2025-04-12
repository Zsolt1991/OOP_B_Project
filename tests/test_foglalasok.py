from datetime import date, timedelta
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.initial_data import betoltott_adatok

def test_jarat_letrehozas():
    legitarsasag, _ = betoltott_adatok()
    jaratok = legitarsasag.listaz_jaratokat()
    assert len(jaratok) == 3

def test_foglalas_sikeres():
    legitarsasag, foglalasok = betoltott_adatok()
    jarat = legitarsasag.get_jarat("HUN101")
    datum = date.today() + timedelta(days=1)
    ar = foglalasok.foglalas(jarat, "Teszt Elek", datum)
    assert ar == 15000
    assert any("Teszt Elek" in f for f in foglalasok.listaz_foglalasokat())

def test_lemondas_sikeres():
    legitarsasag, foglalasok = betoltott_adatok()
    jarat = legitarsasag.get_jarat("HUN101")
    datum = date.today() + timedelta(days=2)
    foglalasok.foglalas(jarat, "Minta Géza", datum)
    sikeres = foglalasok.lemondas("HUN101", "Minta Géza")
    assert sikeres is True

def test_lemondas_sikertelen():
    _, foglalasok = betoltott_adatok()
    sikeres = foglalasok.lemondas("HUN101", "Nem Létező Név")
    assert sikeres is False

def test_foglalas_jovobeli_datumra():
    legitarsasag, foglalasok = betoltott_adatok()
    jarat = legitarsasag.get_jarat("HUN101")
    datum = date.today() + timedelta(days=3)
    ar = foglalasok.foglalas(jarat, "Valid Dátum", datum)
    assert ar == 15000
    assert any("Valid Dátum" in f for f in foglalasok.listaz_foglalasokat())

def test_foglalas_multbeli_datumra():
    legitarsasag, foglalasok = betoltott_adatok()
    jarat = legitarsasag.get_jarat("HUN101")
    datum = date.today() - timedelta(days=2)

    try:
        foglalasok.foglalas(jarat, "Mult Dátum", datum)
        assert False, "Foglalás nem dobott hibát múltra!"
    except ValueError as e:
        assert str(e) == "A megadott dátum már elmúlt."