from funciones_archivo import * 

# VALIDA EL MAXIMO DEL ID Y EN LA OTRA FUNCION SE LE AGREGA 1 O QUEDA EN 1 SI NO HAY ID ANTERIOR

def validar_id_maximo(lista_peliculas: list) -> int:
    """_summary_
        Calcula el máximo valor del ID en una lista de diccionarios que representan películas.
    Args:
        lista_empleados (list):  Una lista de diccionarios donde cada diccionario contiene información sobre una película.
    Returns:
        int | None: El valor máximo del ID en la lista proporcionada, o None si la lista está vacía.
    """
    
    bandera = False
    maximo = 0
    for i in range(len(lista_peliculas)):
        maximo = int(maximo)
        dato = int(lista_peliculas[i]["id"])
        if bandera == False or dato > maximo:
            maximo = dato
            bandera = True

    return maximo

def validar_id(lista_peliculas:list) -> int:
    """_summary_
        Si el ID es 0 entonces la pelicula tiene ID 1, si el ID es cualquier otro numero el ID es el siguiente a ese numero.
    Returns:
        int: Returna el ID unica para la pelicula.
    """

    id = validar_id_maximo(lista_peliculas)
    id = int(id)
    if id == 0:
        id = 1
    else:
        id += 1

    return id

# VALIDA TITULO DE LAS PELICULAS QUE SE DAN DE ALTA. LA DIFERENCIA CON EL OTRO VALIDAR TITULO ES QUE UNO TIENE QUE SI SE REPITEN EL TITULO TE LO RECHACE Y EL OTRO NO.


def dar_alta_titulo(lista_peliculas:list,mensaje:str, criterio:bool) -> str:
    """_summary_
    Permite ingresar y validar un título de película para dar de alta en la lista de películas.

    Args:
        lista_peliculas (list): La lista de películas.
        mensaje (str): El mensaje para solicitar el título de la película.
        criterio (bool]): La función lambda de validación del título.

    Returns:
        str: El título de la película validado y listo para dar de alta.
    """
    while True:
        
        cadena = input(mensaje).capitalize()

        if criterio(cadena) == False:
            print("Ingrese una opción válida por favor!")
            continue
        
        repetido = False
        for i in range(len(lista_peliculas)):
            if lista_peliculas[i]["titulo"].capitalize() == cadena.capitalize():
                repetido = True
                break
        
        if repetido == True:
            print("La película que quiere ingresar ya ha sido validada. Ingrese un título nuevo.")
        else:
            return cadena

# VALIDA EL TITULO DE LAS PELICULAS DEL CVS

def validar_titulo(mensaje, criterio) -> str:
    """_summary_
    Valida un título de película.

    Args:
        mensaje (str): El mensaje para solicitar el título de la película.
        criterio (bool]): La función de validación del título.

    Returns:
        str: El título de la película validado.
    """
    
    cadena = input(mensaje).capitalize()
    while not criterio(cadena):
        print("Ingrese una opción válida por favor!")
        cadena = input("Ingrese la opción nuevamente: ").capitalize()

    return cadena

# VALIDA AÑO DE LANZAMIENTO Y DURACION

def validar_numero(mensaje, criterio) -> int:
    """_summary_
        Lo que hace la funcion es pedir un numero, verifica que se cumpla con el criterio y devuelve un entero validado.
    Args:
        mensaje (str): Es el mensaje el cual se le pasa por parametro dependiendo lo que se este validando.
        criterio (lambda): Es el criterio que se debe respetar para que se pueda seguir a la siguiente validacion (los lambda).

    Returns:
        int: Returna el entero validado.
    """

    numero = input(mensaje)
    while not numero.isdigit() or not criterio(int(numero)):
        print("Ingrese un valor válido por favor!")
        numero = input("Ingrese el valor nuevamente: ")
    return int(numero)

# VALIDA GENERO

def validar_genero() -> str:
    """_summary_
        Valida que el genero sea una de las opciones dadas en el mensaje y pasa la primera letra a mayuscula.
    Returns:
        str: Returna el genero validado
    """
    
    genero = input("Ingrese el género de la película, uno de los siguientes: \nAcción, Aventura, Animación, Biográfico, Comedia, Comedia romántica, Comedia dramática, Crimen, Documental, Drama, Fantasía, Histórico, Infantil, Musical, Misterio, Policíaco, Romance, Ciencia ficción, Suspenso, Terror, Western, Bélico, Deportivo, Noir, \nExperimental, Familiar, Superhéroes, Espionaje, Artes marciales, Fantástico, Catástrofe, Melodrama, Erótico, Cine independiente, Zombies, Vampiros, Cyberpunk, Steampunk, Distopía, Utopía, Road Movie, Docuficción, Mockumentary, Gótico, Slasher, Adolescente, \nCulto, Maravilloso. \n").capitalize()
    while genero != "Acción" and genero != "Aventura" and genero != "Animación" and genero != "Biográfico" and genero != "Comedia" and genero != "Comedia romántica" and genero != "Comedia dramática" and genero !=  "Crimen" and genero != "Documental" and genero != "Drama" and genero != "Fantasía" and genero != "Histórico" and genero != "Infantil" and genero != "Musical" and genero != "Misterio" and genero != "Policíaco" and genero != "Romance" and genero != "Ciencia ficción" and genero != "Suspenso" and genero != "Terror" and genero != "Western" and genero != "Bélico" and genero != "Deportivo" and genero != "Noir" and genero != "Experimental" and genero != "Familiar" and genero != "Superhéroes" and genero != "Espionaje" and genero != "Artes marciales" and genero != "Fantástico" and genero != "Catástrofe" and genero != "Melodrama" and genero != "Erótico" and genero != "Cine independiente" and genero != "Zombies" and genero != "Vampiros" and genero != "Cyberpunk" and genero != "Steampunk" and genero != "Distopía" and genero != "Utopía" and genero != "Road Movie" and genero != "Docuficción" and genero != "Mockumentary" and genero != "Gótico" and genero != "Slasher" and genero != "Adolescente" and genero != "Culto" and genero != "Maravilloso":
        print("Ingrese una opción válida por favor!")
        genero = input("Ingrese la opción nuevamente: ").capitalize()
    return genero

# VALIDA NINGUNA PELICULA

def validar_si_no(mensaje) -> bool:
    """_summary_
        La funcion pide al usuario que ingrese "Si" o "No", pasa la primera letra a mayuscula (si es minuscula) y devuelve un booleano (si es "Si" devuelve True, si es "No" devuelve False)  
    Args:
        mensaje (str): Es el mensaje el cual se le pasa por parametro dependiendo lo que se este validando.

    Returns:
        bool: Returna un booleano, que seria "Si" o "No"   
    """
    
    atp = input(mensaje).capitalize()
    while atp != "Si" and atp != "No":
        print("Debe ingresar Si o no, otro valor es invalido.")
        atp = input(mensaje).capitalize()
    return atp == "Si"

# PARA SABER SI ES UN NUMERO O NO. COMPLEMENTARIA A VALIDAR_PLATAFORMAS

def numeracion_no(cadena):
    """_summary_
    Verifica si una cadena contiene caracteres numéricos.
    
    Args:
        cadena (str): La cadena a verificar.
    
    Returns:
        bool: True si la cadena contiene caracteres numéricos, False de lo contrario.
    """
    for i in range(len(cadena)):
        if cadena[i].isdigit():
            return True
    return False

# VALIDACION DE LAS PLATAFORMAS

def validar_plataformas(mensaje:str) -> list[str]:
    """_summary_
    La función solicita al usuario el ingreso de las plataformas que estan disponibles para la pelicula. las ingresa una por una.
    
    Args:
        mensaje (str): El mensaje que se le muestra al usuario.
    
    Returns:
        list[str]: Retornauna lista de plataformas separadas por - .
    """
    lista_plataformas = []

    while True:

        plataforma = input(mensaje)
        no_numeracion = numeracion_no(plataforma)
        while (no_numeracion == True or len(plataforma) > 20 or plataforma == ""):
            print("Debe ingresar una plataforma valida que no tenga numeros!")
            plataforma = input(mensaje)
            no_numeracion = numeracion_no(plataforma)
        
        lista_plataformas.append(plataforma)
        
        ingresar_otra_plataforma = input("Esa fue su ultima plataforma o quiere agregar otra? (Responda con Si o No)?: ").capitalize()
        while (ingresar_otra_plataforma != "Si" and ingresar_otra_plataforma != "No"):
            ingresar_otra_plataforma = input("Ingrese una opcion valida: ").capitalize()
    
        if (ingresar_otra_plataforma == "No"):
            break
    
    return lista_plataformas

# LA VALIDACION DE LAS PELICULAS (TITULO, GENERO, AÑO_LANZAMIENTO, DURACION O ATP)

def validar_clave (clave:str, lista_peliculas: list[dict]) -> None:
    """_summary_
        Valida si la clave es válida para poder acceder a un atributo de las películas en la lista.

    Args:
        clave (str): La clave que se va a validar.
        lista_peliculas (list): La lista de películas.

    Returns:
        None
    """
    
    while lista_peliculas[0].get(clave) == None:
        print("La clave elegida no existe")
        clave = input("Ingrese correctamente la clave, es una de las siguientes \ntitulo\ngenero\naño_lanzamiento\nduracion\natp \n").lower()

# VALIDA LA CLASIFICACION DE LAS PELICULAS (ASCENDENTE O DESCENDENTE)

def validar_clasificacion(clasificacion: list) -> None:
    """_summary_
        Valida si la clasificación es válida para ordenar las películas.

    Args:
        clasificacion (str): La clasificación a validar.

    Returns:
        None
    """

    while clasificacion != "1" and clasificacion != "2":
        print("La clasificacion elegida no existe")
        clasificacion = input("Ingrese correctamente la clasificacion \n")