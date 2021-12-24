#Hovedprogram

from spillebrett import Spillebrett

# Skriv et hovedprogram, main, der brukeren først skal bli spurt om å oppgi dimensjoner på
# spillebrettet. Deretter skal du opprette brettet og skrive ut den “nulte” generasjonen.

# Illustrasjon 4: Eksempel på utskrift av spillebrettet
# Ved hjelp en menyløkke og input skal brukeren deretter kunne velge å oppgi en tom linje for
# å gå videre til neste steg, eller skrive inn bokstaven “q” for å avslutte programmet. Hver gang
# brukeren oppgir at de ønsker å fortsette skal du kalle på oppdatering-metoden og deretter
# skrive ut brettet på nytt sammen med en linje som beskriver hvilken generasjon som vises
# og hvor mange celler som lever for øyeblikket

#Jeg oppretter en funksjon main som ikke tar imot noen parametere. main blir kalt paa. Brukeren blir bedt om inni funksjonen aa oppgi 
#rader og kolonner, som blir lagret i variabler. Klassen Spillebrett blir kalt på, med de sistnevnte variablene som parametere. Så lenge 
#bruker ikke skriver "q", blir brukeren  spurt om han/hun vil fortsette. For at brukeren skal komme videre til neste generasjon maa 
#han/hun trykk enter. Metodene til klassen Spillebrett med brukerens parametere kaller paa metoden oppdatering og tegnBrett.

def main():
    oppgirader= int(input("Oppgi rader: "))
    oppgikolonner= int(input("Oppgi kolonner: "))
    spillebrettet = Spillebrett(oppgirader, oppgikolonner)
    svar = ""
    while svar != "q":
        svar = input("Onsker du aa fortsette? For aa gaa videre til neste generasjon trykk enter. For aa avslutte trykk q.")
        if svar == "":
            spillebrettet.oppdatering()
            spillebrettet.tegnBrett()
                  
main()