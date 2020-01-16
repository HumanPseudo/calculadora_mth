import os
from test_matrices import multiplicacion

if (__name__ == "__main__"):
    opt = "@"
    while(opt != "S"):
        print("_____________________________")
        print("Calculo de MTH")
        print("1. Iniciar Calculadora \n" )
        print("2. Instrucciones \n" )
        print("Salir \n")
        
        opt = input("Ingrese una Opcion : ")
        if (opt == "1"):
            multiplicacion()
        elif(opt == "2"):
            print("Al iniciar un cálculo usted debera indicar:")
            print("    * Que tipo de transformación es: (R)otación o (T)ranslación")
            print("		   Si es una rotación deberá indicar:")
            print("          - De cuantos grados es el giro")
            print("          - Al rededor de que eje se realiza (X, Y o Z)")
            print("      Si es una translación deberá indicar:")
            print("          - De cuantas unidades es la translación")
            print("          - Sobre que eje se realiza (X, Y o Z)")
            print("    * En que sistema se realiza la transformacion: (M)ovil o (F)ijo")
            print("Recuerde que dependiendo del sistema donde se realice la transformacion se premultiplicará o se postmultiplicará a las demás")
            print("Tenga en cuenta que el programa esta hecho para facilitar el cálculo de la MTH, no tiene algun tipo de validación extra sobre los datos que el programa solicita")
            print("\n\n\n\n\n\n\n\n")

        elif(opt.upper() == "S"):
            print("\n SALIO....")
            os.system("cls")
            opt = "S"
        else:
            print("Incorrecto")