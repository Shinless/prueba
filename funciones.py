import numpy as np
persona = [str(x) for x in range(1,43)]
ar_asi = np.array(persona).reshape(7,6)
Datos = []
def menu(): 
    while True:
        print("\n1.- Grabar Datos \n2.- Buscar.\n3.- Imprimir Certificado.\n4.- Salir.\n")
        try:
            menu_op = int(input())
            if menu_op >= 1 and menu_op <=4:
                if menu_op == 1:
                    Anotar()
                if menu_op == 2:
                    buscar()
                if menu_op == 3:
                    Imprimir()
                if menu_op == 4:
                    break
            else:
                print("Número de opción no válida.  Vuelva a intentarlo.\n")
        except:
            print("Opción no válida, vuelva a intentarlo.\n")




def Anotar():
  try:
    seguir = True
    while seguir == True:
      n = str(input("Ingresa tu NiF sin el Validador :"))
      nv = len(n)
      if nv == 8:
        val = str(input("Ingresa el Validador: "))
        while seguir == True:
          if val == "RTX":
            nif = n+val
            while seguir == True:
              nombre = str(input("Ingrese nombre : "))
              vn = len(nombre)
              if vn >= 8:
                edad = int(input("Ingrese su Edad : "))
                if edad >= 0:
                  persona = [nif,nombre,edad]
                  return persona
          elif val == "XXY":
            nif = n+val
            while seguir == True:
              nombre = str(input("Ingrese nombre : "))
              vn = len(nombre)
              if vn >= 8:
                edad = int(input("Ingrese su Edad : "))
                if edad >= 0:
                  persona = [nif,nombre,edad]
                  return persona
          elif val == "CCU":
            nif = n+val
            while seguir == True:
              nombre = str(input("Ingrese nombre : "))
              vn = len(nombre)
              if vn >= 8:
                edad = int(input("Ingrese su Edad : "))
                if edad >= 0:
                  persona = [nif,nombre,edad]
                  return persona
          elif val == "03F":
            nif = n+val
            while seguir == True:
              nombre = str(input("Ingrese nombre : "))
              vn = len(nombre)
              if vn >= 8:
                edad = int(input("Ingrese su Edad : "))
                if edad >= 0:
                  persona = [nif,nombre,edad]
                  return persona
          else:
            print("Los digitos valiadores No son existentes")
        else:
          print("EL Nif debe ser de 8 digitos")
          seguir == False
  except:
    print("Error En la anotacion de datos")

def buscar():
  global persona
  try:
    seguir == True
    print("Sistema de busqueda por Nif")
    while seguir == True:
      buscar = str(Input("Ingrese el nif de la persona que desee Buscar : "))
      if buscar == persona[0]:
        print("Nombre : ",Persona[1],"\nEdad :",Persona[2],"\nSi pertenece a la union Europea")
        return
      else:
        print("Datos no Encontrados")
        return
  except:
    print("Datos Ingresado no validos")

def Imprimir():
  global Persona
  print("Binvenido al sistema de impresion")
  opcion = int(input("Seleccione que va a imprimir : \n1 Documento de estado civil \n2) Certificado de nacimiento \n3) Certificado de union Europea"))
  if opcion == 2:
    print("El documento presente aqui \n certifica el nacimiento de ",Persona[1]," Con Nif ",Persona[0])
  elif opcion == 1:
    print("El documento presente aqui \n certifica el estado conguyal de la persona : ",Persona[1]," Con Nif ",Persona[0])
  elif opcion == 3:
    print("El documento presente aqui \n certifica que la persona : ",Persona[1]," Con Nif ",Persona[0],"Esta en la union Europea")
