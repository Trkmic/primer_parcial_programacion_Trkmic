from peliculas import *
from funciones_archivo import * 


while True:

        print ("""
**** WELCOME TO NANI'S CINEMA ****
Elija una de las siguiente opciones: 
1. DAR ALTA
2. MODIFICAR
3. ELIMINAR
4. MOSTRAR PELICULAS
5. ORDENAR PELICULAS
6. BUSCAR PELICULA POR TITULO
7. CALCULAR PROMEDIO
8. CALCULAR PORCENTAJE
9. SALIR
        """)

        opcion = input("")

        match (opcion):
                
                case "1":     
                        dar_alta()
                case "2":
                        print(modificar_pelicula(lista_peliculas))
                case "3":
                        print(eliminar_pelicula(lista_peliculas))
                case "4":
                        submenu_peliculas(lista_peliculas)
                case "5":
                        ordenar_peliculas(lista_peliculas)
                        mostrar_peliculas(lista_peliculas)
                case "6":
                        pelicula_titulo(lista_peliculas)
                case "7":
                        submenu_promedios(lista_peliculas)
                case "8":
                        submenu_porcentajes(lista_peliculas)
                case "9":
                        guardar_a_csv(lista_peliculas, r"PARCIAL_PROYECTO\peliculass.csv")
                        sobre_escribir_csv(lista_peliculas, r"PARCIAL_PROYECTO\peliculass.csv")
                        break
                case _:
                        print("Ingrese una opcion valida! ")