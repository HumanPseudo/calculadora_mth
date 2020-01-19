import numpy as np
import os
#import spicy as sp
import math as mt

class manipulador():
    cadena_cinematica = []

    def __init__(self):
        self.cadena()

    def cadena(self):
        eslabones = int(input("ingrese la cantidad de eslabones : "))
        bandera = eslabones-1
        for i in range(eslabones):
            if (i == 0):
                print("\n\n\n______eslabon______no #" + str(i))
                self.cadena_cinematica.append(eslabon(0))
                print("________articulacion___________")
                self.cadena_cinematica.append(articulacion())
            elif(i == bandera):
                print("\n\n\n______eslabon______no #" + str(i))
                self.cadena_cinematica.append(eslabon(1))
            #elif(i !=)
            else:
                print("\n\n\n______eslabon______no #" + str(i))
                self.cadena_cinematica.append(eslabon(2))
                print("________articulacion___________ ")
                self.cadena_cinematica.append(articulacion())

    def imprimir_cadena(self):
        for i in range(len(self.cadena_cinematica)):
            print("_________________________")
            print("posicion numero " + str(i))
            print("_________________________")
            self.cadena_cinematica[i].imprimir()
            print("_________________________\n\n\n")

    
class eslabon():
    def __init__(self,codigo):
        while True:
            if(codigo == 0):
                self.tipo_eslabon = "base"
                self.largo_eslabon = self.largo_esl()
                break
            elif(codigo == 1):
                self.tipo_eslabon = "extremo"
                self.largo_eslabon = self.largo_esl()
                break
            else:
                self.tipo_eslabon = "simple"        
                self.largo_eslabon = self.largo_esl()
                break
        
    def largo_esl(self):
        largo = float(input("Largo de la articulacion : "))
        return(largo)
    
    def imprimir(self):
        print("tipo eslabon : " + self.tipo_eslabon)
        print("largo eslabon : " + str(self.largo_eslabon)+ " cm")
        

class articulacion():
    def __init__(self):
        while True:
            tipo = input("(L)ineal / (R)otacional : ")
            if(tipo.upper() == "R"):
                self.tipo_articulacion = "Rotacional"
                self.grados_rotacion = self.rotacion()
                break
            elif(tipo.upper() == "L"):
                self.tipo_articulacion = "Prismatica/lineal"
                break
            else:
                print("Error intenta de nuevo \n")
    def rotacion(self):
        grados = float(input("Grados de rotacion : "))
        grados = mt.radians(grados)
        
        return(grados)
    
    def imprimir(self):
        if(self.tipo_articulacion == "Rotacional"):
            print("tipo articulacion :"+ self.tipo_articulacion)
            print("grados de rotacion :" + str(mt.degrees(self.grados_rotacion)) + " grados")
        else:
            print("tipo articulacion : " + self.tipo_articulacion)



class algoritmo(manipulador):
        eslabones = []
        articulaciones = []

        def __init__ (self,cadena_cinematica):
            self.nodo = self.cadena_cinematica
            for i in range(len(self.nodo)):
                a = self.nodo[i]
                if(type(a).__name__ == "eslabon"):
                    self.eslabones.append(a)
                else:
                    self.articulaciones.append(a)
            
            self.paso1()
        
        def __str__(self):
            cant = str(len(self.eslabones))+"--"+str(len(self.articulaciones))
            return cant
        
        def paso1(self):
            pass

if __name__ == "__main__":
    os.system("cls")
    mi_manipulador = manipulador()
    mi_manipulador.imprimir_cadena()
     
    e = algoritmo(mi_manipulador.cadena_cinematica)
    print(e)
    #mi_articulacion = articulacion()
    #print (mi_articulacion.tipo_articulacion)
    #print(str(mi_articulacion.grados_rotacion))