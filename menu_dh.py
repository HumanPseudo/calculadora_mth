import os
from test_matrices import multiplicacion

if(__name__ == "__main__"):
    opt = "@"
    while (opt != "S"):
        os.system("cls")
        print("____________________________")
        print("creacion tabla parametros DH")
        print("____________________________")
        print("1.Iniciar Calculo \n")
        print("2.Instrucciones \n")
        print("(S)alir \n")

        opt = input("Ingrese una Opcion : ")
        if(opt == "1"):
            continue
        elif(opt == "2"):
            print ("1: Ingrese la cantidad de articulaciones que posee el robot (desde la base) \n )")
            print ("2:  \n )")
        elif(opt.upper() == "S"):
            print("\n SALIO....")
            os.system("cls")
            opt = "S"
        else:
            print("Incorrecto intente de nuevo \n")
        