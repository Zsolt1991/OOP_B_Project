from data.initial_data import betoltott_adatok
from datetime import datetime, date

def menu():
    print("\n--- Repülőjegy Foglalási Rendszer ---")
    print("1. Járatok listázása")
    print("2. Jegy foglalása")
    print("3. Foglalás lemondása")
    print("4. Foglalások listázása")
    print("5. Kilépés")

def main():
    legitarsasag, foglalasok = betoltott_adatok()
    print(f"\nÜdvözöljük a {legitarsasag.nev} foglalási rendszerében!")

    while True:
        menu()
        valasztas = input("Válassz egy műveletet (1-5): ")

        if valasztas == "1":
            print("\n--- Elérhető járatok ---")
            for info in legitarsasag.listaz_jaratokat():
                print(info)

        elif valasztas == "2":
            nev = input("Add meg a neved: ")
            jaratszam = input("Add meg a járatszámot: ")
            datum_str = input("Add meg az utazás dátumát (ÉÉÉÉ.HH.NN): ")
            try:
                datum = datetime.strptime(datum_str, "%Y.%m.%d").date()
                if datum < date.today():
                    print("Hiba: a megadott dátum már elmúlt.")
                else:
                    jarat = legitarsasag.get_jarat(jaratszam)
                    if jarat:
                        ar = foglalasok.foglalas(jarat, nev, datum)
                        print(f"Sikeres foglalás! Jegyár: {ar} Ft")
                    else:
                        print("Hiba: ilyen járatszám nem létezik.")
            except ValueError:
                print("Hiba: Érvénytelen dátumformátum. Használj ÉÉÉÉ.HH.NN formátumot.")

        elif valasztas == "3":
            nev = input("Add meg a neved: ")
            jaratszam = input("Add meg a járatszámot: ")
            sikeres = foglalasok.lemondas(jaratszam, nev)
            if sikeres:
                print("A foglalás sikeresen le lett mondva.")
            else:
                print("Nem található ilyen foglalás.")

        elif valasztas == "4":
            print("\n--- Aktuális foglalások ---")
            for f in foglalasok.listaz_foglalasokat():
                print(f)

        elif valasztas == "5":
            print("Viszontlátásra!")
            break

        else:
            print("Hibás választás, próbáld újra!")

if __name__ == "__main__":
    main()