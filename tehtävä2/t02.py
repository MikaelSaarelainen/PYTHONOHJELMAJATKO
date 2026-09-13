

def opintopisteet_yhteensa(kurssit):
    summa = 0
    for kurssi in kurssit:
        summa += kurssi["op"]
    return summa


def keskiarvo(kurssit):
    summa = 0
    for kurssi in kurssit:
        summa += kurssi["arvosana"]

    if len(kurssit) == 0:
        return 0

    return summa / len(kurssit)


def painotettu_keskiarvo(kurssit):
    summa = 0
    pisteet = 0

    for kurssi in kurssit:
        summa += kurssi["arvosana"] * kurssi["op"]
        pisteet += kurssi["op"]

    if pisteet == 0:
        return 0

    return summa / pisteet


def tulosta_kurssit(kurssit):
    print("tehdyt kurssit:")

    numero = 1
    for kurssi in kurssit:
        print(str(numero) + ". " + kurssi["nimi"] + "(" +
              str(kurssi["op"]) + "op): " +
              str(kurssi["arvosana"]))
        numero += 1


kurssit = []

while True:
    print("Anna kurssin nimi (lopeta lopettaa)")
    nimi = input("Nimi: ")

    if nimi == "lopeta":
        break

    opintopisteet = int(input("Opintopisteet: "))

    if opintopisteet < 0 or opintopisteet > 20:
        print("Virheellinen syöte.")
        continue

    arvosana = int(input("Arvosana: "))

    if arvosana < 1 or arvosana > 5:
        print("Virheellinen syöte.")
        continue

    kurssi = {
        "nimi": nimi,
        "opintopisteet": opintopisteet,
        "arvosana": arvosana
    }

    kurssit.append(kurssi)


print("Opintopisteet yhteensä", opintopisteet_yhteensa(kurssit))
tulosta_kurssit(kurssit)
print("Arvosanojen keskiarvo:", round(keskiarvo(kurssit), 1))
print("Arvosanojen painotettu keskiarvo:", round(painotettu_keskiarvo(kurssit), 1))