#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      anderson
#
# Created:     15/08/2017
# Copyright:   (c) anderson 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Cola:
    def __init__(self):
        self.__datos = []

    def meter(self,valor):
        self.__datos.append(valor)

    def sacar(self):
        p_ult = len(self.__datos) - 1
        if (p_ult > 0):
            #self.__datos.pop(0)
            del self.__datos[p_ult]

    def primero(self):
        return self.__datos[len(self.__datos) - 1]

    def numElem(self):
        return len(self.__datos)


    def buscar(self,categoria,dat):
        self.listapar=[]
        if self.numElem()== None:
            return False
        elif categoria== 'nombre':
            for i in range(self.numElem()):
                 if self.__datos[i].nombre == dat:
                     self.listapar.append(self.__datos[i])

        elif categoria== 'codigo':
            for i in range(self.numElem()):
                 if self.__datos[i].codigo == dat:
                     self.listapar.append(self.__datos[i])
        elif categoria== 'placa':
            for i in range(self.numElem()):
                 if self.__datos[i].placa == dat:
                     self.listapar.append(self.__datos[i])

        return self.listapar