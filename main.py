from fastapi import FastAPI
import pandas as pd
import numpy as np
import ast
import calendar
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud

app = FastAPI()

# uvicorn main:app --reload



## Función 'cantidad_filmaciones_mes( Mes )'

df_movies_fc = pd.read_parquet(r'Movies\df_movies_mod.parquet', engine='auto')

# Se crea un diccionario para relacionar los meses en letras a sus correspondientes números
meses_letras = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
}

# Usando el diccionario creado, se convierten los meses de num a palabras
# Filtra para obtener sólo las pelis que coincida el mes de estreno y se suman
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes):
    mes_num = meses_letras[mes]
    peliculas_mes = df_movies_fc[df_movies_fc['release_date'].dt.month == mes_num]
    cantidad = len(peliculas_mes)
    return f"{cantidad} películas fueron estrenadas en el mes de {mes}."



## Función 'cantidad_filmaciones_dia(Dia)'


# Se crea un diccionario para relacionar los dias en palabras a sus correspondientes números  
dias_letras = {
    'lunes': 1, 'martes': 2, 'miércoles': 3, 'jueves': 4, 'viernes': 5, 'sábado': 6, 'domingo': 7 
}

# Usando el diccionario creado, se convierten los dias de num a palabras
# Filtra para obtener sólo las pelis que coincida el dia de estreno y se suman
@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia):
    dia_num = dias_letras[dia]
    peliculas_dia = df_movies_fc[df_movies_fc['release_date'].dt.dayofweek == dia_num]
    cantidad = len(peliculas_dia)
    return f"{cantidad} películas fueron estrenadas en los días {dia}."



## Función 'score_titulo(titulo_de_la_filmación)'


""" Esta función toma como argumento un título,busca dentro de 'df_movies_fc',
    verifica si la pelicula se encuentraen el 
    listado (si no está devuelve un mje indicando que no se encontró info), 
    y si está, con la primera coincidencia crea un diccionario 'info'
    con la data de la filmación correspondiente.
    """
    
@app.get("/score_titulo/{titulo}")
def score_titulo(titulo):
    peliculas = df_movies_fc[df_movies_fc['title'] == titulo]
    if not peliculas.empty:
        pelicula = peliculas.iloc[0]
        info_pelicula = {
            'titulo': pelicula['title'],
            'año': pelicula['release_year'],
            'score': pelicula['popularity']
        }
        return f"La película {info_pelicula['titulo']} fue estrenada en el año {info_pelicula['año']} con un score/popularidad de {info_pelicula['score']}."
    else:
        return f"No se encontró información para la película con el título '{titulo}'."
    
    
    
 ## Función 'votos_titulo(titulo_de_la_filmación)'   
 
 
""" Esta función toma como argumento un título,busca dentro de 'df_movies_fc',
    verifica si la pelicula se encuentraen el listado y si tiene = o mas de 
    2000 valoraciones. Si cumple con las condiciones, crea un diccionario 
    'info_pelicula' con la data de la filmación correspondiente.
    """
    
@app.get("/votos_titulo/{titulo}")    
def votos_titulo(titulo):
    pelicula = df_movies_fc[df_movies_fc['title'] == titulo]
    if pelicula.empty:
        return f"No se encontró información de la película con el título {titulo}"
    pelicula = pelicula.iloc[0]
    info_pelicula = {
        'titulo': pelicula['title'],
        'año': pelicula['release_year'],
        'cantidad_votos': pelicula['vote_count'],
        'valor_promedio': pelicula['vote_average']
    }
    if info_pelicula['cantidad_votos'] >= 2000:
        return f"La película {info_pelicula['titulo']} fue estrenada en el año {info_pelicula['año']}. La misma cuenta con un total de {info_pelicula['cantidad_votos']} valoraciones, con un promedio de {info_pelicula['valor_promedio']:.2f}."
    else:
        return f"La película {info_pelicula['titulo']} no cumple con la condición de tener al menos 2000 valoraciones. No se devuelve ningún valor."



## Función 'get_actor(nombre_actor)'

df_actor_fc = pd.read_parquet(r'Movies\df_credits_actor.parquet', engine='auto')

"""Esta función filtra el df en busca de las peliculas en las que actúa el actor
(argumento de fc), si no está, devuelve un mje. Para obtener el retorno se debe
unir lo filtrado con el df 'df_movies_fc', ya que ahi es donde obtendremos la
data para las metricas requeridas (promerdio retorno = suma total retornos de ese 
actor / la cant de peliculas en las que actuó)
    """
    
@app.get("/get_actor/{nombre_actor}")  
def get_actor(nombre_actor):
    actor_movies = df_actor_fc[df_actor_fc['actor_name'] == nombre_actor]
    if actor_movies.empty:
        return f"El actor {nombre_actor} no se encuentra en el listado."
    
    # Se une con el DataFrame de películas para obtener el retorno
    actor_movies = actor_movies.merge(df_movies_fc, on='id_movie')
    
    # Se calculan las métricas
    total_return = actor_movies['return'].sum()
    num_movies = actor_movies['id_movie'].nunique()
    avg_return = total_return / num_movies if num_movies > 0 else 0
    
    result = (f"El actor {nombre_actor} participó de {num_movies} películas, "
              f"el mismo consiguó un retorno de {total_return} con un promedio de {avg_return} por película.")
    
    return result

## Función 'get_director(nombre_director)'

df_director_fc = pd.read_parquet(r'Movies\df_credits_director.parquet', engine='auto')


"""Esta función filtra el df en busca de las peliculas en las que dirige el nombre
otorgado (argumento de fc), si no está, devuelve un mje. Para obtener la otra
info: retorno de las peliculas que dirigió: nombre, fecha de 
lanzamiento, retorno, costo y ganancia se debe unir lo filtrado con el df 
'df_movies_fc', ya que ahi es donde obtendremos la data
    """
    
@app.get("/get_director/{nombre_director}")  
def get_director(nombre_director):
    director_movies = df_director_fc[(df_director_fc['director_name'] == nombre_director)] 
    if director_movies.empty:
        return f"El director {nombre_director} no se encuentra en el listado."
    
    # Se une con el DataFrame de películas para obtener la información adicional
    director_movies = director_movies.merge(df_movies_fc, on='id_movie')
    
    director_movies = director_movies.drop_duplicates(subset=['id_movie', 'title'])
    
    result = f"El director {nombre_director} ha dirigido las siguientes películas:\n"
    for _, row in director_movies.iterrows():
        result += (f"{row['title']}, Fecha de lanzamiento: {row['release_date']}, "
                   f"Retorno: {row['return']}, Costo: {row['budget']}, Ganancia: {row['revenue']}\n")
    
    return result

## Función de recomendación

df_movies_modelo = pd.read_parquet(r'Movies\df_movies_mod.parquet')

""" 
Se conviereten textos en una matriz numérica basandose en la importancia 
(según su frecuencia) de cada palabra.

Cada fila de la matriz que devuelve corresponde a un nombre de película, y 
cada columna a una palabra de ese nombre con el valor correspondiente a 
la importancia de la misma. --stop_words='english'

    """
    
vectorizacion = TfidfVectorizer()
matriz = vectorizacion.fit_transform(df_movies_modelo['title'])

# Se crea una matriz con las caracteristicas que considero son las necesarias para el modelo de recomendación
caracteristicas = np.column_stack([matriz.toarray(), df_movies_modelo['popularity'], df_movies_modelo['vote_count']])

df_movies_modelo = df_movies_modelo.reset_index(drop=True)

# Se realiza el cálculo de similitud del coseno
similitud_coseno = cosine_similarity(caracteristicas)

"""Esta función devuelve 5 peliculas recomendadas basada en la similitud del coseno
    
    - Si la pelicula ingresada no está en la base de datos, devuelve el correspondiente mensaje
    - Se busca en el df el indice de la pelicula ingresada.
    - Se crea una lista de tuplas. cada una de ella contiene el indice de una película y su puntaje 
    de similitud con respecto al título ingresado, y las ordena de forma descendente
    - Se va a iterar sobre cada una se esas tuplas en busca de los índices de laspelis
    mas similares (sin repetirlas) hasta llegar a 5. 
    
    """
def recomendacion(titulo, n_recomendaciones=5):
    if titulo not in df_movies_modelo['title'].values:
        return f"¡Lo siento! La película '{titulo}' no se encuentra, por favor intente con otro título."
    indice = df_movies_modelo[df_movies_modelo['title'] == titulo].index[0]
    
    indice = df_movies_modelo[df_movies_modelo['title'] == titulo].index[0]

    similitudes = list(enumerate(similitud_coseno[indice]))
    similitudes = sorted(similitudes, key=lambda x: x[1], reverse=True)
    
    indices_similares = []
    titulos_recomendados = set()
    for i in similitudes:
        if i[0] != indice and df_movies_modelo['title'].iloc[i[0]] not in titulos_recomendados:
            indices_similares.append(i[0])
            titulos_recomendados.add(df_movies_modelo['title'].iloc[i[0]])
        if len(indices_similares) >= n_recomendaciones:
            break
    
    return df_movies_modelo['title'].iloc[indices_similares].tolist()

@app.get("/recomendar/{titulo}")
def recomendar_peliculas(titulo: str, n_recomendaciones: int = 5):
    return recomendacion(titulo, n_recomendaciones)