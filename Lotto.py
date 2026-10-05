import random

# ============================================================
# Methode 1: Eine Lottoziehung (6 aus 45, ohne Wiederholung)
# ============================================================
def lottoziehung():
    verfuegbare_zahlen = list(range(1, 46))   # Liste: [1, 2, 3, ..., 45]
    gezogene_zahlen = []

    for _ in range(6):                         # genau 6 Zahlen ziehen
        index = random.randint(0, len(verfuegbare_zahlen) - 1)  # zufälliger Index
        zahl = verfuegbare_zahlen[index]       # Zahl an diesem Index holen
        gezogene_zahlen.append(zahl)           # Zahl merken
        verfuegbare_zahlen.remove(zahl)        # Zahl entfernen -> kann nicht mehr gezogen werden

    return gezogene_zahlen


# ============================================================
# Methode 2: Statistik über viele Ziehungen
# ============================================================
def lotto_statistik(anzahl_ziehungen):
    # Dictionary vorbereiten: jede Zahl von 1 bis 45 startet bei 0
    statistik = {}
    for zahl in range(1, 46):
        statistik[zahl] = 0

    for _ in range(anzahl_ziehungen):
        ziehung = lottoziehung()               # eine Ziehung durchführen
        for zahl in ziehung:
            statistik[zahl] += 1                # Zähler für diese Zahl erhöhen

    return statistik


# ============================================================
# Programmstart
# ============================================================
print("--- Einzelne Lottoziehung ---")
ergebnis = lottoziehung()
print("Gezogene Zahlen:", ergebnis)

print("\n--- Statistik über 1000 Ziehungen ---")
stat_1000 = lotto_statistik(1000)
for zahl, haeufigkeit in stat_1000.items():
    print(f"Zahl {zahl}: {haeufigkeit}-mal gezogen")

print("\n--- Statistik über 10000 Ziehungen ---")
stat_10000 = lotto_statistik(10000)
for zahl, haeufigkeit in stat_10000.items():
    print(f"Zahl {zahl}: {haeufigkeit}-mal gezogen")