import numpy as np
import os
#import spicy as sp
import math as mt

def multiplicacion ():

    os.system("cls")
    matrices_calculo = []
    tipo_traslacion = "@"
    eje_rotacion = "@"
    grados = 0
    sistema =  "@"
    eje_traslacion = "@"
    #vectores
    x=0
    y=0
    z=0
    #respuesta = desplazamiento(x,y,z)
    #matrices_calculo.insert(0,respuesta)
    while True:
        sistema ="@"
        opcion = input("(R)otación o (T)raslacion : ")
        if(opcion.upper() == "R"):
            grados = float(input("Grados de rotación : "))

            #poner condicion para que se defina exacto un eje 
            while True:
                eje_rotacion = input ( "Eje de rotacion (x , y , z) : ")
                if(eje_rotacion == "x"):
                    rotacion = rot_x(grados)
                    #print (rotacion)
                    break
                elif(eje_rotacion == "y"):
                    rotacion = rot_y(grados)
                    break
                elif(eje_rotacion == "z"):
                    rotacion = rot_z(grados)
                    break
                else:
                    print("error intente de nuevo \n\n")
            while (sistema.upper() not in "FM"):
                sistema = input("Sistema (M)ovil o (F)ijo : ")
                if(sistema.upper() == "F"):
                    #premultiplica
                    matrices_calculo.insert(0,rotacion)
                    
                elif(sistema.upper() == "M"):
                    #postmultiplica
                    matrices_calculo.append(rotacion)
                    
                else:
                    print("Error intenta de nuevo \n")
            
        elif(opcion.upper() == "T"):
            sistema ="@"
            x = input ("Unidades trasladadas en X :")
            y = input ("Unidades trasladadas en Y :")
            z = input ("Unidades trasladadas en Z :")
            mat_des = desplazamiento(x,y,z)
            #print(mat_des)
            while (sistema.upper() not in "FM"):
                sistema = input("Sistema (M)ovil o (F)ijo : ")
                if(sistema.upper() == "F"):
                    #premultiplica
                    matrices_calculo.insert(0,mat_des)
                    
                elif(sistema.upper() == "M"):
                    #postmultiplica
                    matrices_calculo.append(mat_des)
                   
                else:
                    print("Error intenta de nuevo \n")
        else:
            print("Error intenta de nuevo \n")
        #----------------------------------------------
        nue_mov ="@"
        while(nue_mov.upper() not in "YN"):
            nue_mov = input ("Nueva transformacion (Y/N): ")
            if(nue_mov.upper() == "Y"):
                continue
            elif(nue_mov.upper()== "N"):
                os.system("cls")
                resultado = multiplicacion_final(matrices_calculo)
                print("_____________Respuesta____________ \n\n")
                print(resultado)
                return True
            else:
                print("Error intenta de nuevo \n")
    
def rot_x(g):
    val = mt.radians(g)
    cos = np.cos(val)
    sin = np.sin(val)
    rot = np.array([[1,0,0,0],
                    [0,cos,-sin,0],
                    [0,sin,cos,0],
                    [0,0,0,1]],dtype=float)
    rot_fix = np.around(rot,1)
    #print(rot_fix)
    return (rot_fix)

def rot_y(g):
    val = mt.radians(g)
    cos = np.cos(val)
    sin = np.sin(val)
    rot = np.array([[cos,0,sin,0],
                    [0,1,0,0],
                    [-sin,0,cos,0],
                    [0,0,0,1]], dtype=float)
    rot_fix = np.around(rot,1)
    #print(rot_fix)
    return (rot_fix)

def rot_z(g):
    val = mt.radians(g)
    cos = np.cos(val)
    sin = np.sin(val)
    rot = np.array([[cos,-sin,0,0],
                    [sin,cos,0,0],
                    [0,0,1,0],
                    [0,0,0,1]],dtype=float)
    rot_fix = np.around(rot,1)
    #print(rot_fix)
    return (rot_fix)

def desplazamiento(x,y,z):
    desp = np.matrix([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]],dtype=float)
    return (desp)

def multiplicacion_final(matriz):
    res = np.identity(4)
    for i in range(len(matriz)):
        print("posicion #"+str(i))
        print("____________________________________")
        print("matrices que operan")
        print(res)
        print("*")
        print(matriz[i])
        res = np.dot(res,matriz[i])
        print("=")
        print(res)
        print("______________________________________")
    return(res)