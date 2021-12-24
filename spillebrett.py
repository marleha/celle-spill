#Spillebrett


from random import randint
from celle import Celle

#Forst lager jeg en klasse Spillebrett. Instansvariablene er rader og kolonner. Jeg oppretter en tom liste ruternett, samt 
#en variabel generasjonsnummer som blir satt til a vaere null. Deretter en for-loekke som lager en radCeller liste antall 
#"rader" ganger. Hvis f eks det er tre rader, lager for-loekken tre lister. En ny for-loekke gjoer noe antall "kolonner"
#ganger. For hver kolonne blir klassen Celle kalt paa, en doende celle blir plassert i hver liste radCeller. Deretter blir 
#alle listene radCeller plassert inn i rutenett. Metoden generer blir kalt paa som setter tilfeldig antall cellene til aa bli
#levende.  

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjonsnummer = 0
        
        for rad in range(rader): 
            radCeller = []
            
            for kolonne in range(kolonner): 
                radCeller.append(Celle())
            self._rutenett.append(radCeller)
        self.generer()

#Jeg lager metoden tegnBrett. For hver gang et nytt spillebrett blir lagt blir 100 nye tomme linjer laget, slik at man ikke
#ser det forgje spillebrettet. For hvert element i antall rader, og for hver elemtent i antall kolonner, blir metoden 
#hentStatusTegn kalt på og blir plassert i hvert element i antall kolonne og i hvert element i antall rader inn i rutenett listen. 
#Cellene faar enten doed eller levende som status. For aa unngaa linjeskift etter hver utskrift
# avslutter jeg utskriften med en tom streng (end=""). For hver gang brettet blir tegnet printes generasjonsnummer og antall levende
#celler med tekst.

    def tegnBrett(self):
        print("\n"*100)
        for i in range(self._rader):
            for j in range(self._kolonner):
                print(self._rutenett[i][j].hentStatusTegn(), end="")
            print()
        print("Generasjon:", self._generasjonsnummer, "Antall levende celler:", self.finnAntallLevende())

#Forst lager jeg metoden oppdatering. I metoden lager jeg to lister levendeCeller og doendeCeller som begge er tomme. 
#Vi trenger å kopiere alle objektene i listen, ikke bare listen i seg selv. 
#Derfor lager jeg en variabel som settes aa vaere en dyp kopi av rutenett listen. For hvert element i rutenett, hvis elementer er levende
#lages en variabel naboer. finnNabo funksjonen kalles på og den settes å være variabelen nabo. En teller settes aa vaere 0. For hvert
#element i variabelen naboer, hvis elementet er levende, plusses telleren med 1. Videre, hvis teller er mindre enn 2, settes den neste
#generasjonscellen til aa vaere doed (metoden settDoed kalles paa). Hvis cellen har 2 eller 3 naboer, fortsetter cellen aa leve. Hvis teller 
#er hoyere enn 3, blir cellen i neste generasjon satt til aa vaere doed. 

#Hvis cellen er doed: blir metoden finnNabo kalt på som settes til aa vaere variabelen naboer. teller settes aa vaere 0.
#for hvert element/nabo i naboer. For hver gang nabocellen er levende, okes teller med 1. Hvis teller er 3, settes vellen aa vaere
#levende og lagres i neste generasjon listen. ruternett settes til aa til slutt vaere nesteGenerasjon listen. For hver gang spillebrettet
#oppdateres okes generasjonsnummer med 1. 

    def oppdatering(self):
        levendeCeller = []
        doedeCeller = []
        import copy
        nesteGenerasjon = copy.deepcopy(self._rutenett)
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._rutenett[i][j].erLevende():
                    naboer = self.finnNabo(i, j)
                    teller=0
                    for nabocelle in naboer:
                        if nabocelle.erLevende():
                            teller += 1
                    if teller < 2:
                        nesteGenerasjon[i][j].settDoed()
                    if teller == 2 or teller == 3:
                        pass
                    if teller > 3:
                        nesteGenerasjon[i][j].settDoed()
                else:
                    naboer = self.finnNabo(i,j)
                    teller = 0
                    for nabocelle in naboer:
                        if nabocelle.erLevende():
                            teller += 1
                    if teller == 3:
                        nesteGenerasjon[i][j].settLevende()
        self._rutenett = nesteGenerasjon
        self._generasjonsnummer += 1

#Forst lager jeg en metode finnAntallLevende. en variabel antallLevende settes aa vaere 0. for hvert element i den to dimensjonale
#listen, hvis cellen er levende, antallLevende oker med 1. antallLevende printes med tekst og deretter returneres resultatet.

    def finnAntallLevende(self):
        antallLevende=0
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                if self._rutenett[rad][kolonne].erLevende():
                    antallLevende += 1
        return antallLevende
          

    def generer(self) :
        for i in range (self._rader):
            for j in range (self._kolonner):
                rand = randint(0,3)
                if rand == 3 :
                      self._rutenett[i][j].settLevende()

    def finnNabo (self, rad, kolonne):
        naboliste = []
        for i in range (-1, 2):
            for j in range (-1, 2):
                naboRad = rad+i
                naboKolonne = kolonne+j
                if (naboRad == rad and naboKolonne == kolonne) != True:
                    if (naboRad < 0 or naboKolonne < 0 or naboRad > self._rader-1
    or naboKolonne > self._kolonner-1) != True:
                        naboliste.append(self._rutenett[naboRad][naboKolonne])
        return naboliste