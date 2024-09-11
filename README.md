# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

El objetivo de este proyecto es emular un escenario real para poner en práctica los conocimientos adquiridos durante el bootcamp. Para ello se pretende idealizar una situación dentro de una start-up que provee servicios de agregación de plataformas de streaming. Se debe crear un  modelo de ML que soluciona un problema de negocio: un sistema de recomendación. Se cuenta con información sobre los peliculas, actores y colaboradores.

## Proceso de Desarrollo

### Proceso ETL

En el documento `ETL.ipynb` se encuentran los pasos realizados, para este proyecto se propuso realizar las siguientes etapas:
- cargar cada archivo, decodearlo
- eliminar keys duplicadas
- flatenizar jsons anidados
- eliminar filas vacias
- guardar como csv

Se utilizaron librerias como:
- ast
- json
- pandas
- numpy

### Proceso EDA

En el documento `EDA.ipynb` se encuentran los pasos realizados. Para esta etapa la propuesta fue: a partir de las preguntas del negocio, de los requerimientos solicitados, explorar los datos a fin de organizar, depurar, filtrar. Siempre atentos a que se debe deployar las funciones en una webservice.
El detalle de las funciones a dearrollar se pueden encontrar [aquí](https://github.com/soyHenry/fe-ct-pimlops2?tab=readme-ov-file#propuesta-de-trabajo-requerimientos-de-aprobaci%C3%B3n "aquí")

Se utilizaron librerias como:
- pandas
- numpy
- matplotlib
- seaborn
- wordcloud
- sklearn
	- TfidfVectorizer
	- cosine_similarity

### Deployment

Para disponibilizar las funciones desarrolladas mediante api consumibles desde internet, se utilizó **FastApi** y **uvicorn** en un servicio conocido como **render**:

### Api

Se pueden consultar los distintos endpoints en la siguiente url:
https://pi-mlops-guille-veron.onrender.com/docs

## Contacto

Para obtener más información o realizar preguntas sobre el proyecto, puedes ponerte en contacto con el autor:

- Nombre: Guillermo Veron
- Correo Electrónico: [negoveronr@gmail.com)
