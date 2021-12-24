#Celle 

class Celle:

#Konstrukoer: Forst skriver jeg en klasse celle med en konstruktør som ikke tar imot noen parametre. Jeg setter doed 
#som utgangspunkt, hvor self._doed er True hvis cellen er doed.

    def __init__(self): #(?)
        self._doed= True

#Endre status: Jeg skriver metodene sett Doed og settLevende som ikke tar imot noen parametere. Naar man henter settDoed 
#blir cellen satt til å være doed (True), men naar man henter settLevende blir cellen satt til aa vaere levende (False).

    def settDoed(self):
        self._doed= True 

    def settLevende(self):
        self._doed= False

#Hente status: Jeg lager en metode erLevende som returnerer cellens status False hvis cellen er doed og ellers True hvis 
#cellen er levende. Jeg skriver en metode som returnerer tegnrepresentasjon av cellens status. Hvis cellen er doed returneres
#".", ellers, hvis cellen er levende, returneres "o".

    def erLevende(self):
        if self._doed:
            return False 
        else:
            return True
    
    def hentStatusTegn(self):
        if self._doed == True:
            return "."
        else:
            return "O" 

