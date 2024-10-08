
 ![alt text](<Images/Logo Henry.png>)

# Proyecto-1-DATAPT10

# Descripción
 Este proyecto tiene como objetivo el desarrollo de un MVP (Minimum Viable Product) que logre poner en marcha un sistema de recomendación de películas. Se utilizó el sistema de similitud del coseno para obtener las 5 recomendaciones, por medio de Python, con librerías como Pandas y Scikit-Learn, entre otras.

 # Proceso
 
 El proceso que se siguó fue el de un profesional en la materia (Ingeniaería de Datos/Machine Learning): 

 - ETL (Extraction - Transform - Load) de la data en crudo. Los dos datasets .csv iniciales fueron transformados por separado, obteniendo de esta forma dos nuevos archivos, convertidos al formato parquet para cuidar la optimización computacional. (movies_dataset.csv => df_movies_mod.parquet y credits => df_credit_mod.parquet)
 - La creación de las 6 funciones para la API: Para 2 de estas decidí realizar datasets específicos, con los datos relevantes unicamente:  
 df_credits_mod.parquet:  df_credits_actor => fc. 'get_actor()' // df_credits_director => fc. 'get_director()'
 - Desarrollo de API en el framework FastAPI.
 - EDA: Análisis de los datos 'limpios' mediante gráficas, y consultas, utilizando un criterio enfocado al posterior desarrollo del modelo de recomendación, con verificación de nulos y duplicados, y la extraccón de características relevantes. Aquí tambien creé un dataset específico (df_movies_modelo.parquet)
 - Modelado: Primeramente vectoricé mediante la técnicas TF-IDF para que, ademas de la vectorizacion en sí (para que el algoritomo posteriormente pueda procesar la data) me asegure una reducción de la misma para evitar fallas en el rendimiento del modelo, y la utilización del cálculo de similitud de coseno se fundó en la simplicidad del mismo a la hora de la implementación.
 - La prueba y comprobación de todas las funciones en Render fue exitosa.

 ![alt text](Images/Deploy.png)
 <sub>Deploy exitoso en Render</sub> 
 
# Estructura del Proyecto

- Movies: Contiene los 4 datasets creados/utilizados en el proyecto en formato parquet.
- EDA: Notebook con el proceso de transformación y análisis + función de recomendación.
- ETL: Notebook con la carga y transformación de datos + creación de datasets específicos.
- main.py: contiene las funciones para la API (debidamente comentadas)
- README.md: Archivo de documentación del proyecto.
- requirements: librerias necesarias para el proyecto.

![alt text](Images/FastAPI.png)
<sub>Funciones en framework FastAPI</sub> 

 # Requisitos:

- Python
- pandas
- numpy
- matplotlib
- scikit-learn
- fastapi
- fastparquet
- matplotlib
- pyarrow
- seaborn
- uvicorn
- wordcloud

# Fuente de datos

Datasets originales, sin transformar:
https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5?usp=drive_link

LInk a la aplicación en Render:
https://proyecto-1-datapt10-ml.onrender.com

Video explicativo:
https://youtu.be/qDkZ15sm2c8

# Autor

Débora L. Ferrucci Kellenberger

<sub>Fe de Erratas: En el video me refiero al MVP como Minimum Variable Product, cuando en verdad quise decir 'Viable'.</sub> 
