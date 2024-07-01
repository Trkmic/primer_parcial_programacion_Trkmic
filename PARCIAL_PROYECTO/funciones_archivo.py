from validaciones import *

# MOSTRAR PELICULAS

def cargar_desde_csv(path:str) -> list:
    """_summary_
    Carga datos de las peliculas desde un archivo CSV.
    
    Args:
    - path (str): La ruta del archivo CSV.
    
    Returns:
    - list: Una lista de diccionarios, donde cada diccionario representa una película.
    """
    lista_peliculas = []

    with open(path, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    for i in range(1, len(lineas)):
        claves = lineas[i].strip().split(",")
        plataforma = claves[6].split("-")
        if len(claves) == 7:

            atp_value = claves[5].capitalize() 
            atp_bool = atp_value == "Si"
            pelicula = {
                "id": int(claves[0]),
                "titulo": claves[1].capitalize(),
                "genero": claves[2], 
                "año_lanzamiento": int(claves[3]),
                "duracion": int(claves[4]),
                "atp": atp_bool,
                "plataforma": "-".join(plataforma)
            }

            bandera_existe = False
            for j in range(len(lista_peliculas)):
                if lista_peliculas[j]["titulo"] == pelicula["titulo"]:
                    bandera_existe = True
                    break

            if bandera_existe == False:
                lista_peliculas.append(pelicula)

    sobre_escribir_csv(lista_peliculas, r"PARCIAL_PROYECTO\peliculass.csv")
    return lista_peliculas

def guardar_a_csv(lista_peliculas: list, path:str) -> None:
    """_summary_
    Guarda la lista de películas en un archivo CSV.
    
    Args:
    - lista_peliculas (list): La lista de películas representadas como diccionarios.
    - path (str): Ruta del archivo CSV donde se guardarán los datos.
    
    Returns:
    - None
    """
    with open(path, "a", encoding="utf-8") as archivo:
        for i in range(len(lista_peliculas)):
            pelicula = lista_peliculas[i]
            
            id = pelicula["id"]
            titulo = pelicula["titulo"]
            genero = pelicula["genero"]
            año_lanzamiento = pelicula["año_lanzamiento"]
            duracion = pelicula["duracion"]
            atp = "Si" if pelicula["atp"] else "No"
            plataforma = pelicula["plataforma"]


            archivo.write(f"{id},{titulo},{genero},{año_lanzamiento},{duracion},{atp},{plataforma}\n")

def sobre_escribir_csv(lista_peliculas: list, path:str) -> None:
    """_summary_
    Sobrescribe un archivo CSV con la lista de películas segun las especificaciones que le pase el usuario.
    
    Args:
    - lista_peliculas (list): Lista de películas representadas como diccionarios.
    - path (str): Ruta del archivo CSV que se sobrescribirá.
    
    Returns:
    - None
    """
    with open(path, "w", encoding="utf-8") as archivo:
        archivo.write("ID,Título,Género,Año de lanzamiento,Duración,ATP,Plataformas\n")
        for i in range(len(lista_peliculas)):
            pelicula = lista_peliculas[i]

            id = pelicula["id"]
            titulo = pelicula["titulo"]
            genero = pelicula["genero"]
            año_lanzamiento = pelicula["año_lanzamiento"]
            duracion = pelicula["duracion"]
            atp = "Si" if pelicula["atp"] else "No"
            plataforma = pelicula["plataforma"]

            archivo.write(f"{id},{titulo},{genero},{año_lanzamiento},{duracion},{atp},{plataforma}\n")