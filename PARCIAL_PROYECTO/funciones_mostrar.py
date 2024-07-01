from funciones_archivo import *
import json

def mostrar_peliculas (lista_peliculas: dict) -> None:
    """
    Muestra las películas contenidas en una lista de diccionarios en un formato matriz.

    Args:
    - lista_peliculas (list): Lista de diccionarios donde cada diccionario representa una película.

    Returns:
    - None
    """

    caracteres_interna = "-" * 153
    caracteres_externa = "*" * 153

    matriz = [
            ["Titulo", "Genero", "Año de lanzamiento", "Duración", "ATP", "Plataforma"]
        ]
    for i in range (len(lista_peliculas)):
            fila = [
lista_peliculas[i]["titulo"],lista_peliculas[i]["genero"],str(lista_peliculas[i]["año_lanzamiento"]),str(lista_peliculas[i]["duracion"]),"Si" if lista_peliculas[i]["atp"] else "No",lista_peliculas[i]["plataforma"]]
            matriz.append(fila)

    print(caracteres_externa)
    for i in range (len(matriz)):
            print(f"| {matriz[i][0]:<50} | {matriz[i][1]:<25} | {matriz[i][2]:<18} | {matriz[i][3]:<8} | {matriz[i][4]:<3} | {matriz[i][5]:<30} |")
            if i == 0:
                print(caracteres_interna)
        
    print(caracteres_externa)

def mostrar_peliculas_por_atributo(lista_peliculas: list, atributo: str, valor_busqueda: str) -> None:
    """Muestra películas que coinciden con un atributo y valor específicos.
    Args:
        lista_peliculas (list): Lista de películas.
        atributo (str): El atributo por el cual se buscará (por ejemplo, "genero" o "año_lanzamiento").
        valor_busqueda (str): El valor específico que se busca en el atributo.
    Returns:
        None
    """
    encontrada = False  
    peliculas_encontradas = []
    for i in range(len(lista_peliculas)):
        pelicula = lista_peliculas[i]

        if pelicula.get(atributo) == valor_busqueda:
            peliculas_encontradas.append(pelicula)
            encontrada = True
            
    
    if encontrada == True:
        mostrar_peliculas(peliculas_encontradas)
    else:
        print("No se encontraron películas con el atributo y valor especificados.")

def mostrar_por_genero (lista_peliculas) -> None:
    
    peliculas_por_genero = {}

    for i in range(len(lista_peliculas)):
        pelicula = lista_peliculas[i]
        
        genero = pelicula.get("genero")
        titulo = pelicula.get("titulo")
        
        if genero in peliculas_por_genero:
            peliculas_por_genero[genero].append(titulo)
        else:
            peliculas_por_genero[genero] = [titulo]

    for genero in peliculas_por_genero:
        print(f"Existen {len(peliculas_por_genero[genero])} peliculas del siguiente genero: {genero}")
        peliculas = " - ".join(peliculas_por_genero[genero])
        print(peliculas)

    path = r"PARCIAL_PROYECTO\peliculas_generos.json"
    with open(path, "w", encoding="utf-8") as archivo:
        json.dump(peliculas_por_genero,archivo,indent=4,ensure_ascii=False)

def mostrar_peliculas_por_plataforma(lista_peliculas: list, atributo: str, valor_busqueda: str) -> None:
    """Muestra películas que coinciden con un atributo y valor específicos.
    Args:
        lista_peliculas (list): Lista de películas.
        atributo (str): El atributo por el cual se buscará (por ejemplo, "genero" o "año_lanzamiento").
        valor_busqueda (str): El valor específico que se busca en el atributo.
    Returns:
        None
    """

    encontrada = False  
    peliculas_encontradas = []
    for i in range(len(lista_peliculas)):
        pelicula = lista_peliculas[i]

        if valor_busqueda in pelicula.get(atributo):
            peliculas_encontradas.append(pelicula)
            encontrada = True
    
    if encontrada == True:
        mostrar_peliculas(peliculas_encontradas)
    else:
        print("No se encontraron películas con la plataforma especificada.")
