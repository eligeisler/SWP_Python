import random

# ============================================================
# Methode 1: Lottoziehung (6 aus 45) mit Tausch-Logik
# ============================================================
def lottoziehung(anzahl_zahlen=6):
    kugeln = list(range(1, 46))                # [1, 2, 3, ..., 45]
    letzte_position = len(kugeln) - 1          # Index 44 = Ende des "Ziehbereichs"

    for _ in range(anzahl_zahlen):
        zufalls_position = random.randint(0, letzte_position)   # nur im Ziehbereich würfeln

        # Gezogene Kugel ans Ende des Ziehbereichs tauschen
        kugeln[zufalls_position], kugeln[letzte_position] = kugeln[letzte_position], kugeln[zufalls_position]

        letzte_position -= 1                   # Ziehbereich wird um 1 kleiner

    return kugeln[letzte_position + 1:]        # alles hinter dem Ziehbereich = gezogene Zahlen


# ============================================================
# Methode 2: Statistik über viele Ziehungen
# ============================================================
def lotto_statistik(anzahl_ziehungen):
    statistik = {}
    for zahl in range(1, 46):
        statistik[zahl] = 0                    # jede Zahl startet bei 0

    for _ in range(anzahl_ziehungen):
        ziehung = lottoziehung()
        for zahl in ziehung:
            statistik[zahl] += 1               # Zähler erhöhen

    return statistik


# ============================================================
# Programmstart
# ============================================================
print("--- Einzelne Lottoziehung ---")
print("Gezogene Zahlen:", lottoziehung())

print("\n--- Statistik über 1000 Ziehungen ---")
stat_1000 = lotto_statistik(1000)
for zahl, haeufigkeit in stat_1000.items():
    print(f"Zahl {zahl}: {haeufigkeit}-mal gezogen")

print("\n--- Statistik über 10000 Ziehungen ---")
stat_10000 = lotto_statistik(10000)
for zahl, haeufigkeit in stat_10000.items():
    print(f"Zahl {zahl}: {haeufigkeit}-mal gezogen")