from tkinter import filedialog

from metodos import Metodos
import os

lista=[]
metodo=Metodos
def cargar():
       try:
               file = filedialog.askopenfilename(title="abrir", filetypes=(("inv files", "*.inv"),("all files", "*.*")))
               metodo.leer_archivo(lista,file)
               print("---------------El archivo fue leido y los datos guardados----------------")
       except:
               print("---------------Error","El contenido del archivo no es valido o  no has selecionado un archivo-------------------------") 
def cargarmov():
       try:
               file = filedialog.askopenfilename(title="abrir", filetypes=(("mov files", "*.mov"),("all files", "*.*")))
               metodo.leer_archivo_mov(lista,file)
               print("---------------El archivo fue leido y los datos guardados----------------")
       except:
               print("---------------Error","El contenido del archivo no es valido o  no has selecionado un archivo-------------------------")
separador="---------------------------------------------------------"
app="================================================================"
opcion=0
mostrar=0
filtro=0
os.system("cls")
presione=input ("---------------------------------------------------------\n\t\tBIENVENIDO\n\nLenguajes formales y de programacion\nSeccion:B+\nNombre: Luis Humberto Lemus Perez        Carnet:201445840 \n---------------------------------------------------------\nPresione 1 para continuar   ........\n")

if presione=="1":
        
        os.system("cls")
        while opcion<4:
                try:
            
                        print(separador)
                        print('''
                        Selecciona una opcion:
                        1) Cargar inventario inicial
                        2) Cargar instrucciones de movimiento
                        3) crear informe de inventario.
                        4) Salir
                        ''')
                        print(separador)
                        opcion=int(input("\nPulsa 1 a 4 para continuar\n"))
                        
                        if opcion==1:
                                print("Cargando....")
                                
                                cargar()
                        elif opcion==2:
                                
                                print("Cargando....")
                                
                                cargarmov()
                                        
                        elif opcion==3:
                                os.system("cls")
                                #metodo.generar_total(lista)
                                #for producto in lista:
                                        #print(producto.nombre, producto.total)
                                try:
                                        metodo.graficar(lista)
                                        print("Archivo escrito con exito")
                                except:
                                        print("Eroror al escribir el archivo")
                                
                                
                        elif opcion==4:
                                print("Saliendo.....")

                                
                       
                except:
                        print("Ingreso un dato incorrecto")


else:
        print("Programa no  iniciado")


        