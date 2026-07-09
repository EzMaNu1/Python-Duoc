medicamentos = {
    "M001": ["Paracetamol 500", "GenLab", "analgesico", "L", False, "DistribSur"],
    "M002": ["Amoxicilina 750", "BioFarma", "antibiotico", "R", False, "NorteMed"],
    "M003": ["Insulina NPH", "VidaCorp", "hormonal", "C", True, "FrioPharma"],
}

inventario = {
    "M001": [1290, 40],
    "M002": [5990, 0],
    "M003": [18990, 6],
}

def Menu_de_opciones():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Búsqueda de medicamentos por rango de precio")
    print("3. Actualizar precio de un medicamento")
    print("4. Agregar medicamento")
    print("5. Eliminar medicamento")
    print("6. Salir")
    print("=====================================")

def lista_opciones():
    opcion=0
    try:
        opcion=int(input("Ingrese Una opcion: "))
        if opcion>=1 and opcion<=6:
            return opcion
    except ValueError:
        print("Ingrese Un numero entero positivo")
        return None

def validar_nombre(nombre_medicamento):
    if nombre_medicamento.strip()=="":
        return False
    else:
        return True
    
def validar_laboratorio(laboratorio):
    if laboratorio.strip()=="":
        return False
    else:
        return True

def validar_categoria(categoria):
    if categoria.strip()=="":
        return False
    else:
        return True

def validar_receta(receta):
    if receta== "L" or receta=="R" or receta=="C":
        return True
    else:
        return False
    
def validar_refrigerado(refrigerado):
    if refrigerado.lower()=="s" or refrigerado.lower()=="n":
        return True    
    else:
        return None

def validar_proveedor(proveedor):
    if proveedor.strip()=="":
        return False
    else:
        return True

def validar_precio(precio):
    if precio>0:
        return True
    else:
        return False
    
def validar_stock(stock):
    if stock>=0:
        return True
    else:
        return False

def stock_por_categoria(lista_medicamentos, lista_inventario, categoria_buscada):
    stock_total=0

    for clave in lista_medicamentos:
        if lista_medicamentos[clave][2]==categoria_buscada.lower():
            stock_total+=lista_inventario[clave][1]
    print(f"Total Acumulado: {stock_total}")

def busqueda_precio(lista_medicamentos, lista_inventario, L_precio_min, L_precio_max):
    resultados=[]
    for codigo, valores in lista_inventario.items():
        precio=valores[0]
        stock=valores[1]
        if L_precio_min <= precio <=L_precio_max and stock!=0:
            nombre=lista_medicamentos[codigo][0]
            L_resultado=f"{nombre}--{codigo}"
            resultados.append(L_resultado)
    resultados.sort()
    if len(resultados)>0:
        print("=== Resultados de la busqueda ===")
        for items in resultados:
            print(items)
    else:
        print("No hay coincidencias")

def buscar_codigo(lista_inventario, l_codigo):
    if l_codigo in lista_inventario:
        return True
    else:
        return False

def actualizar_precio(lista_inventario, l_codigo, nuevo_precio):
    if buscar_codigo(lista_inventario, l_codigo):
        lista_inventario[l_codigo][0]=nuevo_precio
        return True
    else:
        return False
    
def agregar_medicamento(lista_medicamento, lista_inventario, codigo, nombre_medicamento, laboratorio, categoria, receta, refrigerado, proveedor, precio, stock):
    if not buscar_codigo(lista_inventario, codigo):
        lista_medicamento[codigo]=[nombre_medicamento, laboratorio, categoria, receta, refrigerado, proveedor]

        lista_inventario[codigo]=[precio, stock]
        return True
    else:
        return False

def eliminar_medicamneto(lista_medicamento, lista_inventario, codigo):
    if buscar_codigo(lista_inventario, codigo):
        del lista_medicamento[codigo]
        del lista_inventario[codigo]
        return True
    else:
        return False

    
    


while True:
    Menu_de_opciones()
    opc=lista_opciones()
    match opc:
        case 1:
            categoria=input("Ingrese la categoria que desea Buscar: ")
            stock_por_categoria(medicamentos, inventario, categoria)
        case 2:
            while True:
                try:
                    precio_min=int(input("Ingrese el precio Minimo: "))
                    precio_max=int(input("Ingrese el precio Maximo: "))

                    if validar_precio(precio_min) and validar_precio(precio_max):
                        if precio_min <= precio_max:
                            break
                        else:
                            print("El precio minimo no puede superar al precio maximo")

                    else:
                        print("Los precios deben ser mayor a 0")
                except ValueError:
                    print("Ingrese el precio en numeros enteros")

            busqueda_precio(medicamentos, inventario, precio_min, precio_max)
        case 3:
            med_actualizar=input("Ingrese el medicamento a actualizar(M001,M002 o M003): ").upper()
            while True:
                try:
                    nuevoprecio=int(input("Ingrese el nuevo precio: "))
                    if validar_precio(nuevoprecio):
                        break
                    else:
                        print("El precio debe ser mayor a 0")
                except ValueError:
                    print("Ingrese el precio en numeros enteros")

            if actualizar_precio(inventario, med_actualizar , nuevoprecio):
                print("Precio actualizado")
            else:
                print("error codigo de medicamento incorrecto")
                
        case 4:
            codigo=input("Ingrese nuevo codigo ej:(M004): ").upper()
            while True:
                nombre_medicamento=input("Ingrese el Nombre del medicamento: ")
                nombre_valido=validar_nombre(nombre_medicamento)
                if nombre_valido==False:
                    print("El nombre del medicamento no debe tener espacios!")
                else:
                    print("Nombre medicamento Guardado!")
                    break
            while True:
                laboratorio=input("Ingrese el Nombre del laboratorio: ")
                laboratorio_valido=validar_laboratorio(laboratorio)
                if laboratorio_valido==False:
                    print("El nombre del laboratorio no debe tener espacios!")
                else:
                    print("Nombre laboratorio Guardado!")
                    break
            while True:
                categoria=input("Ingrese La categoria: ")
                categoria_valida=validar_categoria(categoria)
                if categoria_valida==False:
                    print("El nombre de la categoria no debe tener espacios")
                else:
                    print("Categoria Guardada!")
                    break
            while True:
                receta=input("Ingrese La receta (L, R o C): ")
                receta_valida=validar_receta(receta)
                if receta_valida==False:
                    print("La receta es invalida")
                else:
                    print("La receta fue guardada")
                    break
            while True:
                refrigerado=input("Necesita refrigerado (S o N): ")
                refrigerado_valido=validar_refrigerado(refrigerado)
                if refrigerado_valido==False:
                    print("El dato Ingresado no es valido!")
                else:
                    if refrigerado.lower()=="s":
                        refrigerado=True
                    else:
                        refrigerado=False
                    print("Refrigerado Guardado")
                    break
            while True:
                proveedor=input("Ingrese El proovedor: ")
                proveedor_valdio=validar_proveedor(proveedor)
                if proveedor_valdio==False:
                    print("El nombre del proveedor no debe tener espacos")
                else:
                    print("EL proveedor se guardo")
                    break
            while True:
                try:
                    precio=int(input("Ingrese el precio del medicamento:"))
                    precio_valido=validar_precio(precio)
                    if precio_valido==False:
                        print("El precio debe ser mayor a 0")
                    else:
                        print("Precio guardado")
                        break
                except ValueError:
                    print("Ingrese el precio en numeros enteros")
            while True:
                try:
                    stock=int(input("Ingrese el stock: "))
                    stock_valido=validar_stock(stock)
                    if stock_valido==False:
                        print("el stock debe ser mayor o igual a 0")
                    else:
                        print("stock guardado")
                        break
                except ValueError:
                    print("El stock debe estar en numeros enteros positivos")
            
            if agregar_medicamento(medicamentos, inventario, codigo, nombre_medicamento, laboratorio, categoria, receta, refrigerado, proveedor, precio, stock):
                print(f"El medicamento {codigo} fue agregado con exito")
            else:
                print(f"Error: El codigo {codigo} ya existe!")
        case 5:
            codigo_eliminar=input("Ingrese el codigo del medicamento a eliminar: ").upper()
            if eliminar_medicamneto(medicamentos, inventario, codigo_eliminar):
                print(f"El medicamento {codigo_eliminar} se elimino correctamente")
            else:
                print("Error: el codigo no existe")


        case 6:
            print("Gracias por usar el sistema de medicamentos!")
            break
