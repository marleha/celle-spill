#testoppdatering

#Forst importerer jeg Spillebrett. Jeg lager en funksjon hoveddprogram og kaller paa den nederst i programmet. 
#I funksjonen oppretter jeg et spillebrett som jeg lagrer i variabelen spillebrettet. For hvert objekt i spillebrettet 
#sin rutenet bestemmer jeg om cellen skal bli satt til aa vaere doed eller levende. Etterpaa lager jeg en ny 
#liste som viser hvordan brettet skal vaere etter oppdateringen. Jeg kaller paa spillebrettets metode oppdatering
# og spillebrettet jeg lagde blir oppdatert. Ved hjelp av en dobbel for-loekke gaar jeg gjennomm hvert objekt eller celle
#til objektet spillebrettet jeg lagde, og sjekker opp spillebrettet foer oppdatering har blitt spillebrettet etter
#oppdatering. 

from spillebrett import Spillebrett

def hovedprogram():
    spillebrettet = Spillebrett(4, 4)
    spillebrettet._rutenett[0][0].settDoed()
    spillebrettet._rutenett[0][1].settDoed()
    spillebrettet._rutenett[0][2].settDoed()
    spillebrettet._rutenett[0][3].settLevende()
    spillebrettet._rutenett[1][0].settLevende()
    spillebrettet._rutenett[1][1].settLevende()
    spillebrettet._rutenett[1][2].settLevende()
    spillebrettet._rutenett[1][3].settLevende()
    spillebrettet._rutenett[2][0].settLevende()
    spillebrettet._rutenett[2][1].settLevende()
    spillebrettet._rutenett[2][2].settDoed()
    spillebrettet._rutenett[2][3].settLevende()
    spillebrettet._rutenett[3][0].settDoed()
    spillebrettet._rutenett[3][1].settDoed()
    spillebrettet._rutenett[3][2].settDoed()
    spillebrettet._rutenett[3][3].settLevende()
    etterOppdateringRutenett= [[True, False, True, False],[False, True, True, False],[False, True, True, False],[True, True, False, True]]
    spillebrettet.oppdatering()
    for rad in range(spillebrettet._rader):
        for kolonne in range(spillebrettet._kolonner):
            assert spillebrettet._rutenett[rad][kolonne]._doed == etterOppdateringRutenett[rad][kolonne]

    

hovedprogram()
