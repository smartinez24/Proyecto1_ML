# Proyecto individual ML
By Carlos Martinez DTS - 08
<div id = "header" align = "center">
  <img = src = "https://i.pinimg.com/564x/9a/3f/3f/9a3f3f56b757dcac242958c82e2d7270.jpg" width = "500" />
    <h1 align = 'Center'> !Bienvenido a mi primer proyecto como Data engineer! </>
    <h2 align = 'Center'> ETL(Extract, Transform and Load), EDA(Exploratory Data Analysis) y ML(Machine Learning).
    </2>
</div>

<div id ='badges' align = 'center'>
  <a href = 'https://www.linkedin.com/in/carlos-martinez08'>
    <img src = 'https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white' alt = 'LinkedIn Badge' />

  <a href = 'https://www.instagram.com/csantiagom88'>
    <img src = 'https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white' alt = 'Instragram Badge' />
  
  <a href = 'https://github.com/smartinez24/Proyecto1_ML.git'>
    <img src = 'https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white' alt = 'Github Badge' />
  
  <a href = 'https://studio.youtube.com/channel/UCuXJk_xMmGLQj8kXyYSjTnQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D'>
    <img src = 'https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white' alt = 'Youtube Badge' />
  </a>
</div>

<div id ='badges' align = 'center'>
  <a href = 'https://www.asus.com/co/laptops/for-home/vivobook/asus-vivobook-s14-m433ia/'>
    <img src = 'https://img.shields.io/badge/Windows-ASUS_VivoBook_S14/S15-0078D6?style=for-the-badge&logo=windows&logoColor=white' alt = 'LinkedIn Badge' />
  </a>
</div> 

---
### Introducción.
Primer proyecto de la parte de Labs del Bootcamp SoyHenry. Proceso de extracción de los archivos tipo csv que se encontraban almacenados en la web y transformación de estos para poder llevar a cabo consultas sobre registros de producciones en plataformas de streaming como Amazon, Disney, Hulu y Netflix. Por último, una carga de los
datos limpios a una API, que permita al usuario o cualquier persona ingresar al servicio web y hacer consultas sobre los registros. También, un modelo de Machine Learning, posterior al ETL y Análisis exploratorio de los datos para saber si dado un usuario del sistema, se le recomienda o no una producción.
    
---
<h3> Herramientas usadas: </h3>
<div>
   <img src = 'https://github.com/devicons/devicon/blob/master/icons/slack/slack-original.svg' title = 'Slack' alt = 'Slack' width = '40' height = '40' />&nbsp;
   <img src = 'https://github.com/devicons/devicon/blob/master/icons/google/google-original.svg' title = 'Google' alt = 'Google' width = '40' height = '40'/>&nbsp;
   <img src = 'https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original-wordmark.svg' title = 'VSC' alt = 'VSC' width = '40' height = '40' />&nbsp;
   <img src = 'https://github.com/devicons/devicon/blob/master/icons/windows8/windows8-original.svg' title = 'Windows' alt = 'Windows' width = '40' height = '40' />&nbsp;
   <img src = 'https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg' title = 'Python' alt = 'Python' width = '40' height = '40' />&nbsp;
   <img src = 'https://github.com/devicons/devicon/blob/master/icons/fastapi/fastapi-original.svg' title = 'fastAPI' alt = 'fastAPI' width = '40' height = '40' />&nbsp;
   <img src = 'https://res.cloudinary.com/practicaldev/image/fetch/s--iWNIikKc--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u6kmbieir6su8dt70z3l.png' title = 'Render' alt = 'Render' width = '40' height = '40' />&nbsp;
    <img src = 'https://github.com/devicons/devicon/blob/master/icons/github/github-original-wordmark.svg' title = 'Github' alt = 'Github' width = '40' height = '40' />&nbsp;
  
---
### ETL y EDA.
Para el proceso de ETL y EDA, importé los archivos en el Visual Studio Code, para manejar con el lenguaje Python y sus determinadas librerias. Hice una visualización de los datos en general, para poder ver la relación entre los mismos y poder hacer un debido manejo a los datos nulos, faltantes y atípicos. Por ejemplo, para datos como el cast, el director o el lugar donde se realizó la producción, era imposible hallar una relación con los otros datos del dataset. Sin embargo, habían identificadores o relación entre algunos otros datos, como los datos de tipo numérico, ya que podíamos solucionar los nulos de estos, gracias a la variación, la moda y el promedio, creando y analizando filtros por plataforma y tipo de producción; Movies o TV shows. Este proceso se pudo llevar a cabo y complementar gracias a las siguientes consignas de evaluación:
  - Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123).
  - Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”.
  - De haber fechas, deberán tener el formato AAAA-mm-dd.
  - Los campos de texto deberán estar en minúsculas, sin excepciones.
  - El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas).
  
---
### [API](https://fastapi-hbsx.onrender.com/docs).
Para la creación de la api, se creó un entorno virtual de Python, que me permitió trabajar las consultas con el modulo de fastAPI. Este modulo permite crear una plataforma y/o servicio web, por medio del servidor Render, que trabaja bajo sistema HTTP simples. En este [enlace](https://fastapi-hbsx.onrender.com/docs), podemos realizar las consultas siguientes: 
  - Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type)).
  - Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year)).
  - Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform)).
  - Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year)).

---
### Sistema de recomendación.
Una vez realizado el proceso de ETL y EDA, pasé al sistema de recomendación. Con los datos limpios y un análisis adecuado de la información que se obtuvo de los datasets, se creo un modelo supervisado, que de acuerdo con la calificación a producciones anteriores que visualizó el usuario en una fecha determinada, permitiera evaluar si al recomendar una nueva producción del registro de producciones, que el usuario no haya visto, determine si se le recomienda o no. 
  
---
### [Video](https://studio.youtube.com/channel/UCuXJk_xMmGLQj8kXyYSjTnQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D).
En el siguiente [enlace](https://studio.youtube.com/channel/UCuXJk_xMmGLQj8kXyYSjTnQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D) estará disponible un video haciendo la presentación del proyecto y los procesos realizados para llegar al producto final y poder satisfacer las consultas del proyecto.
  
<div id = "header" align = "center">
  <h1 align = 'Center'> !Gracias! </>
</div>
