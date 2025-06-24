# Análisis del FC Barcelona temporada 2008-2009

## 📌 1. Objetivo del proyecto

Este proyecto tiene como objetivo construir un pipeline de datos tipo ETL (Extracción, Transformación y Carga) de forma local, utilizando un dataset público relacionado con fútbol. A través de este ejercicio se busca aprender e implementar conceptos clave de ingeniería de datos como conexión a bases de datos, manejo de logs y excepciones, control de calidad, pruebas de unidad y exportación de resultados. El análisis se centra en preparar la información de los partidos del FC Barcelona durante la temporada 2008-2009 como caso práctico.

## 📁 2. Dataset utilizado

El dataset utilizado fue **"Football Data from Transfermarkt"**, que fue obtenido desde la plataforma Kaggle. Este DataSet contiene información historica de ligas europeas con datos como: equipos, partidos, ligas y atributos tecnicos.


## 🔍 3. Alcance y casos de uso

El alcance de este proyecto es contruir un pipeline ETL (Extracción, Transformación y Carga) utilizando python de forma local, a partir de una base de datos SQLite obtenida de Kaggle sobre futbol europeo, el objetivo del proyecto es aprender y aplicar buenas practicas en la ingenieria de datos, incluyendo:

-Conexión a una base de datos relacional
-Extracción de datos relevantes mediante consultas SQL.
-Transformación de datos para filtrar partidos del FC Barcelona temporada 2008-2009.
-Cargar los datos transformados en .CSV
-Registro de logs, manejo de excepciones, validaciones de calidad y pruebas unitarias.

El proyecto **no busca construir dashboards o hacer análisis estadístico profundo**, sino **enfocarse exclusivamente en el diseño y ejecución del proceso ETL de manera reproducible y organizada**.

## 🔍 4. Análisis exploratorio de datos (EDA)

Durante el análisis exploratorio se realizaron los siguientes pasos:

- Se identificaron las tablas disponibles en la base de datos.
- Se contaron los registros por tabla.
- Se inspeccionaron las columnas y sus tipos de datos.
- Se validaron las fechas mínimas y máximas para entender el rango temporal.
- Se identificaron valores nulos en columnas clave.
- Se depuraron columnas irrelevantes y se seleccionaron solo las necesarias para el análisis del FC Barcelona.

Se decidió no tratar los valores nulos ya que representaban un porcentaje muy bajo del total (<2%).

## 🧱 5. Modelo de datos y arquitectura

A. Modelo de datos conceptual (Modelo estrella)

Para estructurar el analisis, se propuso un modelo estrella, donde la tabla de hechos es Match, y la tabla de dimensiones son:

- Team: Información del equipo.
- Team_attributes: Caracteristicas tácticas del equipo.
- League: Liga en que se jugó el partido.
- Player_attributes: Atributos de los jugadores.
- Player: Información base de los jugadores.

Este modelo facilita el análisis de desempeño del FC Barcelona en la temporada 2008-2009, relacionando partidos con jugadores, equipos y ligas.

B. Arquitectura del pipeline ETL

El pipeline se desarrolló de forma local, a continuación se describe el proceso del ETL:

    1. Extracción: Se hace una consulta SQL desde python a la base SQL Lite usando sqlite3 y se transforma en un dataframe.

    2. Transformación: Se filtran los partidos del FC Barcelona de la temporada 2008 - 2009, también se eliminan los valores nullos.

    3. Carga: Los datos finales se guardan en formato .CSV en la carpeta data/."

Este pipeline esta automatizado con un script etl.py y controlado con loggin. Además, se realizaron pruebas unitarias para verificar que la extracción y transformación funcionen correctamente. 

## 🧼 6. Pipeline ETL

Proceso ETL (Extract, Transform, Load)

Este proyecto implementa un proceso de ETL básico, basado en Python para analizar los partidos del FC Barcelona en la temporada 2008 - 2009.

    🔹 Extracción (Extract)

        Se realiza una conexión local a la base de datos database.sqlite usando sqlite3.

        Se ejecuta una consulta SQL que une las tablas Match y Team para traer información como:

        match_api_id, date, home_team_goal, away_team_goal

        Nombre del equipo local (home_team_name) y visitante (away_team_name)

        La consulta se ejecuta desde una función en Python (extract_match_data) con manejo de excepciones y logs.

    🔹 Transformación (Transform)
        Se convierte la columna date al formato datetime.

        Se filtran los partidos en los que participó el FC Barcelona, ya sea como local o visitante.

        Se seleccionan solo los partidos disputados entre julio de 2008 y junio de 2009.

        Se eliminan registros nulos.

        Se incorporan controles de calidad (validación de resultados vacíos, logging de resultados).

    🔹 Carga (Load)

        El DataFrame resultante se guarda como un archivo .csv en la carpeta /data/, con el nombre:

## ✅ 7. Control de calidad y pruebas

Control de Calidad y Pruebas

Control de Calidad en la Transformación
    
    Durante el proceso de transformación, se implementaron validaciones básicas para garantizar que los datos cumplieran con ciertos requisitos mínimos. Por ejemplo:

        Conversión del campo date a formato datetime.

        Filtro para incluir solo partidos donde el FC Barcelona participó como local o visitante.

        Validación para asegurar que el DataFrame resultante no esté vacío.

        Eliminación de valores nulos (dropna), ya que representaban un porcentaje pequeño del total.

Se agregó un sistema de logging, que guarda en la carpeta logs/ los eventos importantes del proceso: conexiones exitosas, cantidad de registros extraídos, errores, advertencias, etc.

Pruebas Unitarias

    Se implementaron dos pruebas unitarias en el archivo test_etl.py:

        1. test_extract_returns_dataframe: verifica que la función de extracción retorne un DataFrame.

        2. test_transform_filters_data: asegura que la transformación filtre correctamente partidos del FC Barcelona y que el DataFrame no esté vacío.

## 📖 8. Diccionario de datos

Columna | Tipo de dato | Descripción

match_api_id | Integer | Identificador unico de partido
date | Datetime | Fecha en la que se jugó el partido
home_team_goal | Integer | Goles anotados por el equipo local
away_team_goal | Integer | Goles anotados por el equipo visitante
home_team_name | String	| Nombre del equipo local
away_team_name | String	| Nombre del equipo visitante

## 🔁 9. Frecuencia de actualización propuesta

Frecuencia sugerida:

Mensual y trimestral

Justificación:

    - El análisis realizado corresponde a una temporada histórica de fútbol (2008-2009), lo que implica que los datos no cambian en el tiempo.
    -Por lo tanto, no es necesario actualizarlos constantemente, ya que no hay nuevas entradas ni cambios.
    -Sin embargo, si el proyecto se ampliara a incluir temporadas más recientes o futuras, podría considerarse una frecuencia de:
        -Mensual: si se recibe información frecuente (por ejemplo, datos de partidos al cierre de cada mes).
        Semanal: si se quisiera mantener un seguimiento actualizado de una liga en tiempo real.

Conclusión:

Para el caso actual (análisis de una temporada histórica), no se requiere una actualización periódica. Si se extendiera el proyecto a nuevas temporadas, se podría establecer una frecuencia de actualización mensual.

## 📂 12. Estructura del proyecto


├── database.sqlite                  # Base de datos original descargada desde Kaggle
├── etl.py                           # Script principal del pipeline ETL (Extract, Transform, Load)
├── test_etl.py                      # Archivo de pruebas unitarias para validar el ETL
├── data/                            # Carpeta de salida donde se guarda el CSV final transformado
│   └── barcelona_2008_2009.csv
├── logs/                            # Carpeta con los logs de ejecución
│   └── proyecto.log
├── README.md                        # Documentación principal del proyecto
├── Documentación prueba técnica.docx  # Archivo Word con notas y avances del proyecto
├── Modelo_Estrella.drawio          # Diagrama conceptual del modelo de datos
└── Proyecto_futbol.ipynb           # Exploración inicial del dataset y EDA (análisis exploratorio)

## 13. Criterio de reproducibilidad:

Para ejecutar el proyecto y reproducir los resultados, se deben seguir los siguientes pasos:

1. Clonar el repositorio:

git clone ***

2. Instalar los requerimientos (si aplicas entorno virtual):

pip install pandas

3. Verificar que el archivo database.sqlite esté en la raíz del proyecto.

4. Ejecutar el pipeline ETL:

python etl.py

5. Ejecutar las pruebas unitarias:

python test_etl.py

6. El archivo resultante estará en:

data/barcelona_2008_2009.csv

## 14. Escenarios alternos:

📈 Escalabilidad (datos se incrementan 100x)

En caso de que el volumen de datos aumente significativamente:

    1. Se recomienda migrar de SQLite a un motor más robusto como PostgreSQL o Amazon Redshift.
    2. Usar procesamiento distribuido con herramientas como Apache Spark para manejar grandes volúmenes.
    3. Almacenar los archivos en un sistema escalable como Amazon S3.

⏰ Ejecución diaria en ventana de tiempo específica

Si las tuberías deben ejecutarse automáticamente todos los días:

    1. Utilizar Apache Airflow, AWS Step Functions o cron jobs para orquestar las tareas ETL.
    2. Validar los logs y métricas de ejecución automáticamente.
    3. En ambientes cloud, habilitar trigger por eventos o CloudWatch Events (AWS).

👥 Acceso concurrente por más de 100 usuarios

    1. Usar un motor de base de datos transaccional como PostgreSQL, BigQuery o Snowflake, que soportan alta concurrencia.
    2. Implementar caching con Redis o Memcached para evitar sobrecargar la base.
    3. Separar entornos: uno para ingesta/ETL y otro para consultas de usuarios.

⚡️ Analitica en tiempo real

Si se requiere analitica en tiempo real

    1. Cambiar el modelo batch por uno streaming, usando herramientas como:
        a. Kafka para ingesta
        b. Apache Flink o Spark Streaming para procesamiento
        c. DynamoDB, ClickHouse o Elasticsearch para consultas rápidas.
    2. Visualizar en tiempo real con herramientas como Grafana o Power BI Streaming Datasets.
