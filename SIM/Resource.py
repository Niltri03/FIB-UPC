from slam import *

class resource(slamiii):

    def __init__(self,scheduler,parametres):
        super(resource, self).__init__(scheduler,parametres)
        #Que faig amb parametres, en aquest cas nop
        self.state="FREE"

    def changeState(self, newState):
        self.state == newState

    def acceptaEntitat(self, n):
        return n

