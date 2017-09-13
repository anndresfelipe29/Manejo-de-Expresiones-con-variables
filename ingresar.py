from cola import *
class ingresar():

    def __init__(self,Lista):
        self.Lista=Lista
        self.a=Cola()

    def ingreso(self, Lista):

        if len(Lista)>0:
            self.a.meter(Lista[0])
            self.ingreso(Lista[1:])
        return self.a



