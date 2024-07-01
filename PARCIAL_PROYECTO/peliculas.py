from validaciones import *
from funciones_matematicas import *
from funciones_archivo import *
from funciones_mostrar import *

# DAR ALTA

lista_peliculas = cargar_desde_csv(r"PARCIAL_PROYECTO\peliculass.csv")

def dar_alta () -> dict:
    """_summary_
        Da de alta una nueva película y la agrega a la lista de películas.
    Return:
        dict: Un diccionario que representa la nueva película agregada.
        str: un print con un mensaje que dice el ID de la nueva pelicula.
    """

    id = validar_id(lista_peliculas)
    titulo = dar_alta_titulo(lista_peliculas,"Ingrese el título de la película: ", lambda titulo: 1 < len(titulo) < 30).capitalize()
    genero = validar_genero()
    año_lanzamiento = validar_numero("Ingrese el año de lanzamiento: ", lambda numero: 1888 <= numero <= 2024)
    duracion = validar_numero("Ingrese la duración de la película (en minutos): ", lambda numero: numero > 1)
    apto_todo_publico = validar_si_no("La película es apta para todo público? (Responder Si/No)")
    plataforma = validar_plataformas("Ingrese la plataforma (INGRESE DE A UNA Y CON LAS MAYUSCULAS CORRESPONDIENTES A CADA PLATAFORMA): ")


    nueva_pelicula = dict()
    nueva_pelicula["id"] = id 
    nueva_pelicula["titulo"] = titulo
    nueva_pelicula["genero"] = genero
    nueva_pelicula["año_lanzamiento"] = año_lanzamiento
    nueva_pelicula["duracion"] = duracion
    nueva_pelicula["atp"] = apto_todo_publico
    nueva_pelicula["plataforma"] = "-".join(plataforma)

    lista_peliculas.append(nueva_pelicula)
    print(f"La pelicula con el ID: {nueva_pelicula['id']} fue dado de alta!")

    return nueva_pelicula

# MODIFICAR

def modificar_pelicula (lista_peliculas: dict) -> str:
    """_summary_
        Es un submenu el cual podrias modificar lo que quieras de una película de la lista de películas, siempre y cuando sea posible y este entre las opciones a modificar.
    Args:
        lista_peliculas (list): La lista de películas.
    Return:
        str: Un mensaje que dice el total de las modificaciones, si no se realizaron cambios o si la pelicula no existe.
    """
    
    retorno = ""
    bandera_existe = False
    verificar_titulo = validar_titulo("Ingrese el título de la película: ", lambda x: 1 < len(x) < 49)
    for i in range(len(lista_peliculas)):
        if verificar_titulo == lista_peliculas[i]["titulo"]:
            bandera_existe = True
            while True:
                    opcion = input("Que dato desea modificar?\n a) Titulo \n b) Genero \n c) Año de lanzamiento \n d) Duracion \n e) ATP \n f) Plataforma \n g) Salir \n").lower()

                    match opcion:
                        case "a":
                            dato = dar_alta_titulo(lista_peliculas,"Ingrese el nuevo título de la película: ", lambda x: 1 < len(x) < 30)
                            lista_peliculas[i]["titulo"] = dato
                            retorno += "se modifico el titulo. \n"
                        case "b":
                            dato = validar_genero()
                            lista_peliculas[i]["genero"] = dato
                            retorno += "se modifico el genero. \n"
                        case "c":
                            dato = validar_numero("Ingrese el nuevo año de lanzamiento de la pelicula: ", lambda x: 1888 <= x <= 2024)
                            lista_peliculas[i]["año_lanzamiento"] = dato
                            retorno += "se modifico el año de lanzamiento. \n"
                        case "d":
                            dato = validar_numero("Ingrese la nueva duracion de la pelicula (Minutos): ", lambda x: x > 1)
                            lista_peliculas[i]["duracion"] = dato
                            retorno += "se modifico la duracion. \n"
                        case "e":
                            dato = validar_si_no("Ingrese el nuevo apt de la pelicula (Responder Si/No): ")
                            lista_peliculas[i]["atp"] = dato
                            retorno += "se modifico el ATP. \n"
                        case "f":
                            
                            dato = validar_plataformas("Ingrese la/las nuevas plataforma/s en las que se encuentra disponible la película (INGRESE DE A UNA Y CON LAS MAYUSCULAS CORRESPONDIENTES A CADA PLATAFORMA): ")
                            dato = "-".join(dato)
                            lista_peliculas[i]["plataforma"] = dato

                            retorno += "se modifico la/las plataformas. \n"
                        case "g":
                            break
                        case _:
                            print("ingrese una opcion valida")

            break

    if retorno == "":
        retorno = "No se realizaron cambios."
    if bandera_existe == False:
        retorno = "Error. No existe esa pelicula con ese titulo."
    return retorno

# ELIMINAR

def eliminar_pelicula(lista_peliculas:list) -> str:
    """_summary_
        La funcion pide al usuario que ingrese un titulo, lo valida reutilizando la funcion de validar_cadena y elimina mostrando la pelicula eliminada. Si la pelicula no existe devuelve un mensaje diferente.
    Args:
        lista_peliculas (list): Es la lista de las peliculas que fueron dadas de alta.
    Return:
        La pelicula eliminada o que la pelicula no existe.
    """

    retorno = ""
    verificar_titulo = validar_titulo("Ingrese el título de la película: ", lambda x: 1 < len(x) < 49)
    for i in range(len(lista_peliculas)):
            if verificar_titulo == lista_peliculas[i]["titulo"]:
                pelicula_eliminada = lista_peliculas.pop(i)
                retorno = f"""La pelicula eliminada fue: 
Titulo: {pelicula_eliminada['titulo']}
Genero: {pelicula_eliminada['genero']}
Año de lanzamiento: {pelicula_eliminada['año_lanzamiento']}
Duracion: {pelicula_eliminada['duracion']}
Apto para todo publico: {"si" if pelicula_eliminada['atp'] else "no"}
Plataforma/s: {pelicula_eliminada['plataforma']}
    """
                break

    if retorno == "":
        retorno = "No existe una pelicula con ese titulo."
    return retorno

# SUBMENU DE MOSTRAR PELICULAS

def submenu_peliculas (lista_peliculas: dict) -> str:
    """ _summary_
        Es un submenu el cual podras mostrar diferentes datos sobre películas, como todas las películas,películas de un género específico, películas de un año específico, películas aptas para todo público, películas no aptas para todo público o salir del menú.
    Args:
        lista_peliculas (dict): Un diccionario que contiene información sobre las películas.
    Return:
        None
    """

    while True:
            
            opcion = input("Que datos desea que se muestren?\n a) Todas las peliculas \n b) Determinado genero \n c) determinado año \n d) Todas las ATP \n e) Todas las no ATP \n f) De determinada plataforma \n g) Mostrar por género \n h) Salir\n").lower()
            match opcion:
                case "a":
                    mostrar_peliculas(lista_peliculas)
                case "b":
                    genero_buscado = validar_genero()
                    mostrar_peliculas_por_atributo(lista_peliculas, "genero", genero_buscado)
                case "c":
                    anio_lanzamiento_buscado = validar_numero("Ingrese el año de lanzamiento que busca: ", lambda x: 1888 <= x <= 2024)
                    mostrar_peliculas_por_atributo(lista_peliculas, "año_lanzamiento", anio_lanzamiento_buscado)
                case "d":
                    mostrar_peliculas_por_atributo(lista_peliculas, "atp", True)
                case "e":
                    mostrar_peliculas_por_atributo(lista_peliculas, "atp", False)
                case "f":
                    plataforma_buscada = "-".join(validar_plataformas("Ingrese la plataforma que busca: "))
                    mostrar_peliculas_por_plataforma(lista_peliculas, "plataforma", plataforma_buscada)
                case "g":
                    mostrar_por_genero(lista_peliculas)
                case "h":
                    break
                case _:
                    print("ingrese una opcion valida")

# ORDENAR PELICULAS

def ordenar_peliculas (lista_peliculas:list) -> str:
    """_summary_
        Ordena una lista de películas según una clave y clasificación. Se debe elegir una clave (por ejemplo, 'titulo', 'genero', 'año_lanzamiento', 'duracion', 'atp' para ordenar las películas. Despues se debe elegir un tipo de clasificacion ("Ascendente (1)" o "Descendente (2)"). Las peliculas se ordenaran segun la clave y la clasificacion elegida.
    Args:
        lista_peliculas (list): La lista de películas que se ordenará.
    Return:
        None
    """

    clave = input("Ingrese la clave a la cual quiera acceder, escriba una de las siguientes \ntitulo\ngenero\naño_lanzamiento\nduracion\natp\n").lower()
    validar_clave(clave, lista_peliculas)
        
    clasificacion = input("eliga la clasificacion que usted quiera: \n1) Ascendente \n2) Descendente \n")
    validar_clasificacion(clasificacion)

    if clasificacion == "1":                
            for j in range (len(lista_peliculas)): 
                intercambio = False
                for i in range (len(lista_peliculas) - 1 - j): 
                    if lista_peliculas[i][clave] > lista_peliculas [i + 1][clave]: 
                        lista_peliculas[i], lista_peliculas[i + 1] = lista_peliculas[i + 1], lista_peliculas[i]
                        intercambio = True
                                
                if intercambio == False:
                    break
    if clasificacion == "2":    
            for j in range (len(lista_peliculas)): 
                intercambio = False
                for i in range (len(lista_peliculas) - 1 - j): 
                    if lista_peliculas[i][clave] < lista_peliculas [i + 1][clave]: 
                        lista_peliculas[i], lista_peliculas[i + 1] = lista_peliculas[i + 1], lista_peliculas[i]
                        intercambio = True
                                
                if intercambio == False:
                    break

# MOSTRAR PELICULA POR TITULO

def pelicula_titulo (lista_peliculas: list) -> None:
    """_summary_
        Te muestra la pelicula que vos elegiste con el titulo que ingresaste.
    Args:
        lista_peliculas (list): la de todas las peliculas dadas de alta.
    Return:
        None
    """

    titulo_buscado = validar_titulo("Ingrese el título de la película: ", lambda x: 1 < len(x) < 49)
    for i in range(len(lista_peliculas)):
        if titulo_buscado == lista_peliculas[i]["titulo"]:
            mostrar_peliculas_por_atributo(lista_peliculas, "titulo", titulo_buscado)


# SUBMENU DE LOS DOS PROMEDIOS

def submenu_promedios (lista_peliculas: dict) -> str:
    """_summary_
        Muestra el promedio del atributo seleccionado por el usuario.
    Args:
        lista_peliculas (dict): Un diccionario que tiene información sobre las películas.
    Return:
        None
    """

    while True:
            opcion = input("Que promedio desea que se muestre?\n a) Promedio de año de lanzamiento \n b) Promedio de duracion de peliculas\n c) Salir \n").lower()

            match opcion:
                case "a":
                    calcular_promedios(lista_peliculas, "año_lanzamiento")
                case "b":
                    calcular_promedios(lista_peliculas, "duracion")
                case "c":
                    break
                case _:
                    print("ingrese una opcion valida")

# SUBMENU DE LOS DOS PORCENTAJES

def submenu_porcentajes (lista_peliculas: dict) -> str:
    """_summary_
        Muestra el procentaje del atributo seleccionado por el usuario.
    Args:
        lista_peliculas (dict): Un diccionario que tiene información sobre las películas.
    Return:
        None
    """

    while True:
            opcion = input("Que porcentaje quiere saber?\n a) Porcentaje por genero \n b) Porcentaje por ATP\n c) Salir \n").lower()

            match opcion:
                case "a":
                    porcentaje_genero(lista_peliculas)
                case "b":
                    porcentaje_atp(lista_peliculas)
                case "c":
                    break
                case _:
                    print("ingrese una opcion valida")