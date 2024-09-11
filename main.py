import pandas as pd
import numpy as np
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
    
app = FastAPI()



# Endpoints de la API
# @profile
@app.get('/cantidad_filmaciones_mes/{mes}')
async def cantidad_filmaciones_mes(mes: str):

    try:
        movies = pd.read_csv("data/movies_api.csv", parse_dates=["release_date"], date_format='%Y-%m-%d')
        meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
        nmes = meses.index(mes.upper())
        
        # Filtrar el DataFrame por el mes indicado

        movies = movies[movies["release_date"].dt.month == (nmes+1)]

        cant = movies.shape[0]
        
        return {f"{cant} películas fueron estrenadas en el mes de {mes.capitalize()}"}

    except Exception as e:
        return {"error": str(e)}            
    

@app.get('/cantidad_filmaciones_dia/{dia}')
async def cantidad_filmaciones_dia(dia: str): 
    try:
        movies = pd.read_csv("data/movies_api.csv", parse_dates=["release_date"], date_format='%Y-%m-%d')
        dias = ['LUNES','MARTES','MIERCOLES','JUEVES','VIERNES','SABADO','DOMINGO']
        ndia = dias.index(dia.upper())
        
        # Filtrar el DataFrame por el dia indicado

        movies = movies[movies["release_date"].dt.weekday == (ndia)]

        cant = movies.shape[0]        
        
        return {f"{cant} películas fueron estrenadas en los días {dia.capitalize()}"}

    except Exception as e:
        return {"error": str(e)}   
    

@app.get('/score_titulo/{titulo_de_la_filmacion}')
async def score_titulo(titulo_de_la_filmacion: str):
    try:
        movies = pd.read_csv("data/movies_api.csv", parse_dates=["release_date"], date_format='%Y-%m-%d')        
                
        # Filtrar el DataFrame por el titulo

        movies = movies[movies["title"].str.upper() == titulo_de_la_filmacion.upper()]

        anio = list(movies['release_date'].dt.year)[0]

        score = list(movies['popularity'])[0]

        title = list(movies['title'])[0]
                
        return {f"La película {title} fue estrenada en el año {anio} con un score/popularidad de {score:.2f}"}

    except Exception as e:
        return {"error": str(e)}  



@app.get('/votos_titulo/{titulo_de_la_filmacion}')
async def votos_titulo(titulo_de_la_filmacion: str):
    try:
        movies = pd.read_csv("data/movies_api.csv", parse_dates=["release_date"], date_format='%Y-%m-%d')        
                
        # Filtrar el DataFrame por el titulo

        movies = movies[movies["title"].str.upper() == titulo_de_la_filmacion.upper()]

        anio = list(movies['release_date'].dt.year)[0]

        votos = list(movies['vote_count'])[0]

        votos_avg = list(movies['vote_average'])[0]

        title = list(movies['title'])[0]              
        
        return {f"La película {title} fue estrenada en el año {anio} .La misma cuenta con un total de {votos:.0f} valoraciones, con un promedio de {votos_avg}"}

    except Exception as e:
        return {"error": str(e)}  


@app.get('/get_actor/{nombre_actor}')
async def get_actor(nombre_actor: str):
    credits = pd.read_csv("data/credits_flat.csv", usecols=['mov_id','name','job'])
    movies = pd.read_csv("data/movies_api.csv", usecols=['id','return'])         
                    
    # Filtrar actor

    actor = pd.DataFrame({'id':credits[(credits["name"].str.upper() == nombre_actor.upper()) & (credits["job"].str.upper() == "ACTOR")]["mov_id"]})
    actor.drop_duplicates(subset="id", inplace=True)

    merge = pd.merge(actor, movies, on='id')

    cant = merge.shape[0]
    retorno = merge['return'].sum()
    ret_avg = np.average(merge['return'])

    return {f"El/La actor/actriz {nombre_actor.upper()} ha participado de {cant} filmaciones, el mismo ha conseguido un retorno de {retorno:.2f} con un promedio de {ret_avg:.2f} por filmación"}

@app.get('/get_director/{nombre_director}')
async def get_director(nombre_director: str):
    ### def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver 
    # el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, 
    # retorno individual, costo y ganancia de la misma.

    credits = pd.read_csv("data/credits_flat.csv", usecols=['mov_id','name','job'])
    movies = pd.read_csv("data/movies_api.csv", usecols=['id','title','release_date','return', 'budget', 'revenue'], parse_dates=["release_date"], date_format='%d-%m-%Y', )         
                    
    # Filtrar Director

    dir = pd.DataFrame({'id':credits[(credits["name"].str.upper() == nombre_director.upper()) & (credits["job"].str.upper() == "DIRECTOR")]["mov_id"]})
    dir.drop_duplicates(subset="id", inplace=True)

    merge = pd.merge(dir, movies, on='id')

    retorno = merge['return'].sum()

    peliculas = merge[['title','release_date','return','budget','revenue']].rename(columns={'title':'Nombre','release_date':'Lanzamiento','return':'Retorno','budget':'Costo','revenue':'Ganacia'})

    respuesta = {"director" : nombre_director, "retorno":  retorno, "peliculas": peliculas.transpose()}
    json_compatible_item_data = jsonable_encoder(respuesta)
    return JSONResponse(content=json_compatible_item_data)
        

@app.get('/recomendacion/{titulo}')
async def recomendacion(titulo: str):
    try:
        df_recom = pd.read_csv("data/recomendacion_db.csv",sep=";")
        movies = pd.read_csv("data/movies_api.csv", usecols=['id','title'])
        movie_id = movies[movies["title"].str.upper() == titulo.upper()]['id']
        
        # Filtrar el DataFrame por el game_id especificado
        df_recom = df_recom[df_recom["movie_id"] == int(movie_id)]["recom"]
        return {"recomendaciones":df_recom}
        
    except Exception as e:
        return {"error": str(e)}     
    
