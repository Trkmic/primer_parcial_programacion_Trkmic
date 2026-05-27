# Sistema de Gestión de Películas (Movie Management System)

Este es un sistema interactivo de consola desarrollado en Python para gestionar un catálogo de películas. El proyecto fue diseñado con una arquitectura modular y limpia, ideal para la persistencia de datos local mediante archivos CSV y validaciones robustas.

## 🚀 Características principales

- **Gestión CRUD Completa (Alta, Modificación, Eliminación)** de películas con IDs autoincrementales.
- **Validaciones Rigurosas:** Entrada de datos saneada (insensibilidad a mayúsculas en géneros, control de años de lanzamiento, duraciones correctas y nombres de plataformas válidos).
- **Consultas y Filtrado:** Búsqueda por título, listado y ordenamiento de películas.
- **Métricas y Estadísticas:**
  - Cálculo de promedio de duración de las películas.
  - Porcentaje de películas por género específico.
  - Porcentaje de películas Aptas para Todo Público (ATP).
  - Exportación de reportes de géneros en formato JSON.
- **Persistencia de Datos:** Lectura y escritura en archivo CSV (`peliculass.csv`).

## 📁 Estructura del Proyecto

El código está modularizado para separar las responsabilidades de manera clara:

*   **`main.py`**: Punto de entrada de la aplicación. Controla el bucle principal y el menú de navegación de la consola.
*   **`peliculas.py`**: Contiene la lógica central de negocio (registro, edición y eliminación de películas) y menús secundarios.
*   **`validaciones.py`**: Valida y sanea los inputs del usuario (fechas, enteros, strings, plataformas, géneros, etc.).
*   **`funciones_archivo.py`**: Administra la persistencia de datos (carga y guardado de películas en formato CSV).
*   **`funciones_matematicas.py`**: Contiene submódulos para cálculos promedio y porcentuales.
*   **`funciones_mostrar.py`**: Formatea de manera matricial e imprime la información en la consola de manera legible.
*   **`peliculass.csv`**: Archivo de almacenamiento de las películas.

## 🛠️ Requisitos e Instalación

1. Asegúrate de tener instalado **Python 3.10+** (desarrollado y probado en Python 3.13).
2. Clona este repositorio:
   ```bash
   git clone https://github.com/Trkmic/movie-management-system.git
   ```
3. Navega al directorio del proyecto:
   ```bash
   cd movie-management-system
   ```
4. Ejecuta la aplicación:
   ```bash
   python main.py
   ```
