from validaciones import *
from funciones_archivo import *

lista_peliculas = cargar_desde_csv(r"PARCIAL_PROYECTO\peliculass.csv")

def calcular_promedios (lista_peliculas:list, clave:str) -> None:
    """_summary_
        Calcula el promedio del atributo seleccionado de las películas en la lista.
    Args:
        lista_peliculas (list): La lista de películas.
        clave (str): La clave que representa al atributo que se calculará el promedio.
    Returns:
        None
    """

    acumulador_pelicula = 0

    for i in range (len(lista_peliculas)):
            
            acumulador_pelicula += lista_peliculas[i][clave]
    promedio = acumulador_pelicula / (len(lista_peliculas))
    print(f"El promedio de {clave} es {promedio:.02f}")

def porcentaje_genero (lista_peliculas:list[dict]) -> None:
    """_summary_
        Calcula y muestra el porcentaje de películas por género.
    Args:
        lista_peliculas (list): La lista de películas.
        clave (str): El género de cada película.
    Returns:
        None
    """

    acumulador_genero = 0

    genero_ingresado = validar_genero()
    for i in range (len(lista_peliculas)):
            
            if genero_ingresado == lista_peliculas[i]["genero"]:
                acumulador_genero += 1
    
    if acumulador_genero == 0:
        print("No se ha encontrado ningun genero del que se busca")
    else:
        porcentaje = (acumulador_genero / len(lista_peliculas)) * 100
        print(f"{genero_ingresado} : {porcentaje:.02f}%")

def porcentaje_atp (lista_peliculas:list[dict]) -> None:
    """_summary_
        Calcula y muestra el porcentaje de películas con ATP positivo y negativo.
    Args:
        lista_peliculas (list): La lista de películas.
    Returns:
        None
    """

    contador_si_atp = 0
    contador_no_atp = 0

    for i in range (len(lista_peliculas)):
            if lista_peliculas[i]["atp"] == True:
                contador_si_atp += 1
            else:
                contador_no_atp += 1

    porcentaje_si_atp = (contador_si_atp / (len(lista_peliculas))) * 100
    porcentaje_no_atp = (contador_no_atp / (len(lista_peliculas))) * 100
    
    print(f"el porcentaje de ATP positivo es: {porcentaje_si_atp:.02f}% y el porcentaje de ATP negativo es: {porcentaje_no_atp:.02f}%")