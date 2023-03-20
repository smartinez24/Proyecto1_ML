from fastapi import FastAPI, Path, UploadFile, File
from typing import Optional
import shutil 
import pandas as pd
import numpy as np
from starlette.responses import RedirectResponse

#PASOS
#py -m venv fastapi
#fastapi\Scripts\activate.bat
#pip install library
#uvicorn main:app --reload

app = FastAPI(title = 'Consultas de movies y TV shows', 
              description = 'Consultas basadas en el registro de movies y TV shows de las plataformas Amazon, Disney, Hulu y Netflix.')

df_movies = pd.read_csv('Movies.csv', sep = ';')
df_actors = pd.read_csv('Actors.csv', sep = ';')
df_total = pd.read_csv('Total querys.csv', sep = ';')

@app.get('/get_max_duration')
async def get_max_duration( year: int, platform: str , duration_type: str):

    if platform == 'Amazon' or platform == 'amazon': platform_abb = 'as'
    elif platform == 'Disney' or platform == 'disney': platform_abb = 'ds'
    elif platform == 'Hulu' or platform == 'hulu': platform_abb = 'hs'
    elif platform == 'Netflix' or platform == 'netflix': platform_abb = 'ns'
    else: return 'No se reconoce la plataforma. Intente escribir nuevamente la plataforma de la siguiente manera: \n - Amazon Prime Video = Amazon \n - Disney plus = Disney \n - Hulu  = Hulu \n - Netflix = Netflix \n'

    if duration_type == 'Season' or duration_type == 'season': duration_type = 'season'
    elif duration_type == 'Seasons' or duration_type == 'seasons': duration_type = 'season'
    elif duration_type == 'Mins' or duration_type == 'mins': duration_type = 'min'
    elif duration_type == 'Minutos' or duration_type == 'minutos': duration_type = 'min'
    else: return 'No se reconoce el tipo de duración. Intente escribir nuevamente el tipo de duración de la siguiente manera: \n - Season(s) = Season \n - Minutos = Mins'
    
    max_time = df_total[(df_total['release_year'] == year) & (df_total.id.str.startswith(platform_abb)) & (df_total['duration_type'] == duration_type)]['duration_int'].max()
    movie_id = df_total[(df_total['release_year'] == year) & (df_total.id.str.startswith(platform_abb)) & (df_total['duration_type'] == duration_type) & (df_total['duration_int'] == max_time)]['id'].unique()
    movie = df_movies.loc[df_movies['id'] == movie_id[0]]['title'].reset_index()
    movie_title = movie['title'][0]

    return f'La producción con mayor duración en el año {year}, en la plataforma \'{platform}\' es \'{movie_title}\' con una duracion total de {max_time} {duration_type}(s).' 

@app.get('/get_score_count')
async def get_score_count(platform: str, scored: float, year: int):

    if platform == 'Amazon' or platform == 'amazon': platform_abb = 'as'
    elif platform == 'Disney' or platform == 'disney': platform_abb = 'ds'
    elif platform == 'Hulu' or platform == 'hulu': platform_abb = 'hs'
    elif platform == 'Netflix' or platform == 'netflix': platform_abb = 'ns'
    else: return 'No se reconoce la plataforma. Intente escribir nuevamente la plataforma de la siguiente manera: \n - Amazon Prime Video = Amazon \n - Disney plus = Disney \n - Hulu  = Hulu \n - Netflix = Netflix \n'

    quan_movies = len(df_total[(df_total.id.str.startswith(platform_abb)) & (df_total['score_user'] > scored) & (df_total['release_year'] == year)])

    return f'La cantidad de producciones en la plataforma \'{platform}\' en el año {year} con un puntaje mayor a {scored}, es igual a {quan_movies}.'

@app.get('/get_count_platform')
async def get_count_platform(platform):

    if platform == 'Amazon' or platform == 'amazon': platform_abb = 'as'
    elif platform == 'Disney' or platform == 'disney': platform_abb = 'ds'
    elif platform == 'Hulu' or platform == 'hulu': platform_abb = 'hs'
    elif platform == 'Netflix' or platform == 'netflix': platform_abb = 'ns'
    else: return 'No se reconoce la plataforma. Intente escribir nuevamente la plataforma de la siguiente manera: \n - Amazon Prime Video = Amazon \n - Disney plus = Disney \n - Hulu  = Hulu \n - Netflix = Netflix \n'

    total = len(df_movies[df_movies.id.str.startswith(platform_abb)])
    type_min = len(df_movies[(df_movies.id.str.startswith(platform_abb)) & (df_movies['duration_type'] == 'min')])
    type_season = len(df_movies[(df_movies.id.str.startswith(platform_abb)) & (df_movies['duration_type'] == 'season')])
    
    return f'La cantidad de producciones en la plataforma \'{platform}\' es igual a {total}. Un total de movies igual a {type_min} y {type_season} TV shows '

@app.get('/get_actor')
async def get_actor(platform: str, year: int):

    if platform == 'Amazon' or platform == 'amazon': platform_abb = 'as'
    elif platform == 'Disney' or platform == 'disney': platform_abb = 'ds'
    elif platform == 'Netflix' or platform == 'netflix': platform_abb = 'ns'
    elif platform == 'Hulu' or platform == 'hulu': 
        platform_abb = 'hs'
        return 'Lo sentimos. No tenemos registro de los actores de esta plataforma. Puedes probar con las otras plataformas. Gracias.'
    else: return 'No se reconoce la plataforma. Intente escribir nuevamente la plataforma de la siguiente manera: \n - Amazon Prime Video = Amazon \n - Disney plus = Disney \n - Hulu  = Hulu \n - Netflix = Netflix \n'

    actors_year = df_actors[(df_actors.platform.str.startswith(platform_abb)) & (df_actors['year'] == year)]['actor']
    actor = actors_year.value_counts().index[0]
    appears = actors_year.value_counts().max()
    
    return f'El actor que más se repite en la plataforma \'{platform}\', en el año {year}, es {actor}, con un total de {appears} apariciones.'