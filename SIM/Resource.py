from slam import *

'''
CLASE Resource 
DOS ESTADOS: "FREE" o "BUSY" (changeState) 
FUNCIONES: 
tractarEsdeveniment(resource, eventoATratar)
me comunico con alter prempt free
Diagrama de grafo: Flechas son funciones/signals, nodos son estados


'''

class resource(slamiii):

    def __init__(self,scheduler,parametres):
        super(resource, self).__init__(scheduler,parametres)
        #Que faig amb parametres, en aquest cas nop
        self.parametres = parametres
        atributos = parametres.split(',')
        self.state="FREE"

    def __repr__(self):
        return "resource"

    #Recibe un evento, un Resource( a si mismo ) y devuelve ¿?XD dependiendo del estado actual.
    def tractarEsdeveniment(self, event):
        if(self.state == "FREE"):
            self.state == "BUSY"
            #hago codigo
            self.state == "FREE"
        else:
            pass
        pass


    def changeState(self, newState):#Primer parametro el objeto a cambiar el estado, segundo parametro el nuevo estado
        if(newState == "FREE" or newState == "BUSY"):
            self.state == newState

    def entraAlter(self):

    def acceptaEntitat(self, n):
        return n

    def iniciSimulacio(self):
        pass

    def summary(self):
        pass
        #nº entidades procesadas 
    
    def fiSimulacio(self):
        #Aquí tampoc faig res
        del self
