
C:\Users\debor\Desktop\PROYECTO1\Images\Logo Henry.png

# Proyecto-1-DATAPT10

# Descripción
 Este proyecto tiene como objetivo el desarrollo de un MVP (Minimum Variable Product) que logre poner en marcha un sistema de recomendación de películas. Se utilizó el sistema de similitud del coseno para obtener las recomedaciones, el modelo fue implementado en Python, con librerías como Pandas y Scikit-Learn, entre otras.

 # Proceso
 
 El proceso que se siguó fue el de un profesional en la materia (Ingeniaería de Datos/Machine Learning) en su día a día. 
 - ETL (Extraction - Transform - Load) de la data en crudo.
 - La creación de 6 funciones, para 2 de las cuales decidí realizar datasets específicos, con la data a utilizar unicamente ('get_actor() y get_director()').
 - Desarrollo de API en el framework FastAPI.
 - EDA, análisis de los datos 'limpios' mediante gráficos, y consultas, utilizando un criterio enfocado al posterior desarrollo del modelo de recomendación, con verificación de nulos y duplicados, y la extraccón de características relevantes. 
 - Realización del cálculo de similitud de coseno, la prueba y comprobación del funcionamiento de todas las funciones en Render.
 
# Estructura del Proyecto

Movies: Contiene los 4 datasets utilizados en el proyecto en formato parquet.
EDA: Notebook con el proceso de transformación y análisis + función de recomendación.
ETL: Notebook con la carga y transformación de datos + creación de datasets específicos para dos de las funciones ('get_actor() y get_director()')
README.md: Archivo de documentación del proyecto.
requirements: librerias necesarias para el proyecto.

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

Dataset:
https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5?usp=drive_link

Link a repositorio de GitHub:
https://github.com/DKDeboraKellenberger/Proyecto-1-DATAPT10.git

LInk a la aplicación en Render:
https://proyecto-1-datapt10-ml.onrender.com

# Autor

Débora L. Ferrucci Kellenberger
