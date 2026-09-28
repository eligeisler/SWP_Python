# ============================================================
# 1) if / elif / else  (Fallunterscheidung)
# ============================================================
print("--- 1) if / elif / else ---")

alter = 20

if alter < 14:
    print("Kind")
elif alter < 18:
    print("Jugendlicher")
else:
    print("Erwachsener")


# ============================================================
# 2) match / case  (Ersatz für switch, ab Python 3.10)
# ============================================================
print("\n--- 2) match / case ---")

tag = "Samstag"

match tag:
    case "Samstag" | "Sonntag":      # | bedeutet "oder"
        print(tag, "ist Wochenende")
    case "Montag" | "Dienstag" | "Mittwoch" | "Donnerstag" | "Freitag":
        print(tag, "ist ein Werktag")
    case _:                          # _ = alles andere (wie else)
        print("Kein gültiger Wochentag")


# ============================================================
# 3) for-Schleife  (feste Anzahl / Liste durchlaufen)
# ============================================================
print("\n--- 3) for-Schleife ---")

fruechte = ["Apfel", "Banane", "Kirsche"]

for frucht in fruechte:
    print("Ich mag", frucht)

for zahl in range(1, 4):             # 1, 2, 3
    print("Zahl:", zahl)


# ============================================================
# 4) while-Schleife  (läuft, solange die Bedingung stimmt)
# ============================================================
print("\n--- 4) while-Schleife ---")

zaehler = 1

while zaehler <= 3:
    print("Durchgang", zaehler)
    zaehler = zaehler + 1            # sonst Endlosschleife!


# ============================================================
# 5) break  (Schleife sofort beenden)
# ============================================================
print("\n--- 5) break ---")

for n in range(1, 10):
    if n == 4:
        print("4 erreicht, Schleife wird abgebrochen")
        break
    print("n =", n)


# ============================================================
# 6) pass  (Platzhalter, tut nichts)
# ============================================================
print("\n--- 6) pass ---")

for i in range(1, 4):
    if i == 2:
        pass                         # hier später evtl. Code, jetzt nichts
    else:
        print("i =", i)


# ============================================================
# 7) try / except  (Fehler abfangen)
# ============================================================
print("\n--- 7) try / except ---")

try:
    ergebnis = 10 / 0                # erzeugt einen ZeroDivisionError
    print(ergebnis)
except ZeroDivisionError:
    print("Fehler: Durch 0 darf man nicht teilen!")
finally:
    print("Das steht immer am Ende (finally)")