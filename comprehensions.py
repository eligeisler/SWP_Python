"""Hausübung: je eine list-, set- und dict-Comprehension mit if/else."""

# ============================================================
# Grundidee:
#   [ausdruck for x in iterable]                      -> alle Elemente
#   [ausdruck for x in iterable if bedingung]         -> FILTER (if am Ende):
#                                                        Elemente können wegfallen
#   [a if bedingung else b for x in iterable]         -> if-else AUSDRUCK (vorne):
#                                                        jedes Element bleibt, wird aber umgewandelt
# ============================================================

zahlen = [-3, 8, 5, -1, 12, 7, 0, 8]

# ------------------------------------------------------------
# 1) LIST Comprehension mit if/else
#    Aufgabe: Jede Zahl als "gerade" oder "ungerade" beschriften.
# ------------------------------------------------------------
beschriftet = ["gerade" if z % 2 == 0 else "ungerade" for z in zahlen]
print("1) list :", beschriftet)
# ['ungerade', 'gerade', 'ungerade', 'ungerade', 'gerade', 'ungerade', 'gerade', 'gerade']

# Gleiche Aufgabe mit normaler Schleife (zum Vergleich):
beschriftet2 = []
for z in zahlen:
    if z % 2 == 0:
        beschriftet2.append("gerade")
    else:
        beschriftet2.append("ungerade")
print("   Schleife:", beschriftet2 == beschriftet)           # True

# ------------------------------------------------------------
# 2) SET Comprehension mit if/else
#    Aufgabe: Negative Zahlen durch 0 ersetzen. Ein Set speichert
#    jeden Wert nur EINMAL (Duplikate fallen weg, keine feste Reihenfolge).
# ------------------------------------------------------------
ohne_negative = {z if z >= 0 else 0 for z in zahlen}
print("2) set  :", ohne_negative)
# {0, 5, 7, 8, 12}   (die 8 kommt zweimal vor, im Set nur einmal)

# ------------------------------------------------------------
# 3) DICT Comprehension mit if/else
#    Aufgabe: Jeder Zahl (Schlüssel) ihre Vorzeichen-Kategorie (Wert) zuordnen.
#    Auch hier gilt: Schlüssel sind eindeutig, doppelte Zahlen überschreiben sich.
# ------------------------------------------------------------
kategorie = {z: "positiv" if z > 0 else "null" if z == 0 else "negativ"
             for z in zahlen}
print("3) dict :", kategorie)
# {-3: 'negativ', 8: 'positiv', 5: 'positiv', -1: 'negativ', 12: 'positiv', 7: 'positiv', 0: 'null'}

# ------------------------------------------------------------
# Bonus: if als FILTER (am Ende) kombiniert mit if-else (vorne)
# ------------------------------------------------------------
nur_positive_als_text = ["gerade" if z % 2 == 0 else "ungerade"
                         for z in zahlen if z > 0]
print("Bonus   :", nur_positive_als_text)
# ['gerade', 'ungerade', 'gerade', 'ungerade', 'gerade']