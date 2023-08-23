

import os
from clases import Producto

class Metodos:

        def igresar_curso ( lista,  curso:Producto):
            ubicaicon=curso.ubicacion
            existe = False

            if not lista:
                lista.append(curso)
            
            else:   
                    for x in lista:
                        nux=x.ubicacion
                        #print(x.ubicacion,curso.ubicacion,curso.nombre,"*****************************/////")
                
                        
                        if nux==ubicaicon and x.nombre==curso.nombre:
                            existe = True
                            x.cantidad+=curso.cantidad
                            break 

                    if existe == False:
                        lista.append(curso)
        def agregar_stock ( lista,  curso:Producto):
            ubicaicon=curso.ubicacion
            existe = False

            if not lista:
                print("no hay productos")
            
            else:   
                    for x in lista:
                        nux=x.ubicacion
                        #print(x.ubicacion,curso.ubicacion,curso.nombre,"*****************************/////")
                
                        
                        if nux==ubicaicon and x.nombre==curso.nombre:
                            existe = True
                            x.cantidad+=curso.cantidad
                            break 

                    if existe == False:
                        print("-----ERROR---- NO existe el producto   ",curso.nombre,"   en esa ubicacion")
        def agregar_venta ( lista,  curso:Producto):
            ubicaicon=curso.ubicacion
            existe = False
            menor=False

            if not lista:
                print("no hay productos")
            
            else:   
                    for x in lista:
                        nux=x.ubicacion
                        #print(x.ubicacion,curso.ubicacion,curso.nombre,"*****************************/////")
                        
                        if nux==ubicaicon and x.nombre==curso.nombre and curso.cantidad > x.cantidad:
                                menor=True
                                break
                        if nux==ubicaicon and x.nombre==curso.nombre and curso.cantidad<=x.cantidad:
                            existe = True
                            x.cantidad-=curso.cantidad
                            break 

                    if existe == False:
                        print("-----ERROR---- NO existe el producto   ",curso.nombre,"   en esa ubicacion")
                    if menor==True:
                        print("-----ERROR---- No hay existencias del producto   ",curso.nombre,"   en esta ubicacion")
       
        def leer_archivo(lista:list,ruta):
                cantidad=0
                pelicula=""
                precio=""
                ubicacion=""
            
                with open(ruta, encoding='utf-8') as f :
                
                    for x in f: 
                        listalocal=[]
                        listalocal=x.split(";")
                        i=1
                        pelicula=listalocal[0]
                        cadena1=pelicula.strip()
                        nombre=cadena1.replace("crear_producto ","")
                        cantidad=int(listalocal[1])
                        precio=listalocal[2]
                        ubicacion=listalocal[3].strip()
                        pro=Producto(nombre,cantidad,precio,ubicacion)
                        Metodos.igresar_curso(lista,pro)
        def leer_archivo_mov(lista:list,ruta):
                cantidad=0
                pelicula=""
                precio=""
                ubicacion=""
                ubicacionventa=""
                nombreventa=""
                cantidadventa=""
            
                with open(ruta, encoding='utf-8') as f :
                
                    for x in f: 
                        listalocal=[]
                        listalocal=x.split(";")
                        i=1
                        pelicula=listalocal[0]
                        nombre=pelicula.strip()
                        if "agregar_stock" in nombre:
                            nombrestok=nombre.replace("agregar_stock ","")
                            cantidad=int(listalocal[1])
                            ubicacion=listalocal[2].strip()
                            pro=Producto(nombrestok,cantidad,"",ubicacion)
                            Metodos.agregar_stock(lista,pro)
                        elif "vender_producto" in nombre:
                            nombreventa=nombre.replace("vender_producto ","")
                            cantidadventa=int(listalocal[1])
                            ubicacionventa=listalocal[2].strip()
                            prov=Producto(nombreventa,cantidadventa,"",ubicacionventa)
                            Metodos.agregar_venta(lista,prov)

        
                    

        def generar_total(lista:list):
            
            producto:Producto
            for producto in lista:
                total=0.0
                total=float(producto.cantidad) * float(producto.precio)
                producto.total=total
        def graficar(lista:list):
            Metodos.generar_total(lista)
            cadenatotal=""
            pie="...             ...              ...             ...             ..."
            producto:Producto
            textopro=""
            cadena=""
            encabezado="Informe de Inventario:\nProducto    Cantidad       Precio Unitario      Valor Total    Ubicación\n----------------------------------------------------------------------------------------\n"
            for producto in lista:
                textopro=producto.nombre+"\t"+"                "+str(producto.cantidad)+"            "+str(producto.precio)+"            "+str(producto.total)+"           "+producto.ubicacion+"\n"
                cadena+=textopro
            cadenatotal=encabezado+cadena+"\n"+pie
            
            with open('resultado.txt', 'w', encoding='utf-8') as f:
                f.write(cadenatotal)

            # Aqui creamos la imagen
            #os.system('dot -Tpng ejemplo_graphviz.dot -o ejemplo_graphviz.png')

                





 
   