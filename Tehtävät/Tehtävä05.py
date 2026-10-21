#Tehtävä 5

class KurssiSuoritus():
    def __init__(self, nimi: str, pisteet: int, arvosana: int):
        self.nimi = nimi
        self.pisteet = pisteet
        self.arvosana = arvosana

    def __repr__(self):
        return f"KurssiSuoritus({self.nimi}, {self.pisteet}, {self.arvosana})"

    def __eq__(self, other):
        return (
            isinstance(other, KurssiSuoritus)
            and self.nimi == other.nimi
            and self.pisteet == other.pisteet)

class SuoritusOte():
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.suoritukset = []

    def __repr__(self):
        return f"SuoritusOte({self.nimi}, {self.suoritukset})"

    def lisaaSuoritus(self, uusiSuoritus):
        for suoritus in self.suoritukset:
            if suoritus == uusiSuoritus:
                if uusiSuoritus.arvosana > suoritus.arvosana:
                    suoritus.arvosana = uusiSuoritus.arvosana
                return
        self.suoritukset.append(uusiSuoritus)

    def opintopisteet(self):
        return sum(suoritus.pisteet for suoritus in self.suoritukset)

    def keskiarvo(self):
        if len(self.suoritukset) == 0:
            return 0
        return sum(suoritus.arvosana for suoritus in self.suoritukset) / len(self.suoritukset)

    def painotettuKeskiarvo(self):
        if self.opintopisteet() == 0:
            return 0
        summa = sum(suoritus.arvosana * suoritus.pisteet for suoritus in self.suoritukset)
        return summa / self.opintopisteet()

    print(ote)
    print("Opintopisteet:", ote.opintopisteet())
    print("Keskiarvo:", ote.keskiarvo())
    print("Painotettu keskiarvo:", ote.painotettuKeskiarvo())

