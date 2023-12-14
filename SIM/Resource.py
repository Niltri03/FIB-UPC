from slam import *

'''
CLASE Resource 
DOS ESTADOS: "FREE" o "BUSY" (changeState) 
FUNCIONES: 
tractarEsdeveniment(resource, eventoATratar)

'''

class resource(slamiii):

    def __init__(self,scheduler,parametres):
        super(resource, self).__init__(scheduler,parametres)
        #Que faig amb parametres, en aquest cas nop
        self.state="FREE"

    #Recibe un evento, un Resource( a si mismo ) y devuelve ¿?XD dependiendo del estado actual.
    def tractarEsdeveniment(self, event):
        if(self.state == "FREE"):
            self.state == "BUSY"
            #hago codigo
            self.state == "FREE-"
        else:
            pass
        pass


    def changeState(self, newState):#Primer parametro el objeto a cambiar el estado, segundo parametro el nuevo estado
        if(newState == "FREE" or newState == "BUSY"):
            self.state == newState
        else:
            print("Not a valid state")

    def acceptaEntitat(self, n):
        return n

    def fiSimulacio(self):
        #Aquí tampoc faig res
        del self
