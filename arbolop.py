from Nodo import *
from cola import *
from ecuaciones import *
from ingresar import *
class Arbol:
  def __init__(self, Lista):
		self.Lista=Lista


  def llenar(self, Lista,Arbol):
		if Lista.numElem()>0:
			if Arbol==None:
				Arbol=Nodo(None)
				self.llenar(Lista, Arbol)
			else:
				if self.Tipo(Lista.primero()) ==1: #valor entero
					Arbol.valor=Lista.primero()
					Lista.sacar()
				elif self.Tipo(Lista.primero()) ==0:
					Arbol.valor=Lista.primero()
					Lista.sacar()
					Arbol.Derecho=Nodo(None)
					self.llenar(Lista, Arbol.Derecho)
					Arbol.Izquierdo=Nodo(None)
					self.llenar(Lista, Arbol.Izquierdo)
		return Arbol



  def Tipo(self,valor):# 0 operaciones 1 numero entero 2 paila
		if valor=='+':
			numero=0
		elif valor=='-':
			numero=0
		elif valor=='/':
			numero=0
		elif valor=='*':
			numero=0
		else:
			numero=2
			try:
				num= int(valor)
				numero=1
			except Exception as e:
				print "Este valor no es numerico "
		return numero


  def evaluar(self,arbol):
		if arbol.valor=='+':
			return self.evaluar(arbol.Izquierdo)+ self.evaluar(arbol.Derecho)
		elif arbol.valor=='-':
			return self.evaluar(arbol.Izquierdo)- self.evaluar(arbol.Derecho)
		elif arbol.valor=='/':
			return self.evaluar(arbol.Izquierdo)/ self.evaluar(arbol.Derecho)
		elif arbol.valor=='*':
			return self.evaluar(arbol.Izquierdo)* self.evaluar(arbol.Derecho)
		else: return arbol.valor


  def agregadorop(self,arreglo):
        pr=(ingresar(arreglo).ingreso(arreglo))
        px=ecuaciones(pr)
        p=Arbol(px.ecuacion(pr))
        return [p.evaluar(p.llenar(pr,None)),px.vara()]



Ar=Arbol(None);
arreglo1=[3,2,"+",5,8,"-","+","A"]
arreglo2=[5,6,"+","B"]
A=Ar.agregadorop(arreglo1)
B=Ar.agregadorop(arreglo2)
arreglo3=[A[0],B[0],"-","C"]
C=Ar.agregadorop(arreglo3)
print A,B,C
