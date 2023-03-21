# Proyecto individual ML - Data 08
By Carlos Martinez
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
### Introducción
Primer proyecto de la parte de Labs del Bootcamp SoyHenry. Proceso de extracción de los archivos tipo csv que se encontraban almacenados en la web y transformación de estos para poder llevar a cabo consultas sobre registros de producciones en plataformas de streaming como Amazon, Disney, Hulu y Netflix. Por último, una carga de los
datos limpios a una API, que permita al usuario o cualquier persona ingresar al servicio web y hacer consultas sobre los registros. También, un modelo de Machine Learning, posterior al ETL y Análisis exploratorio de los datos para saber si dado un usuario del sistema, se le recomienda o no una película.
    
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
  
---
### Parte de ETL y EDA
Para el proceso de ETL, importé los archivos en el Visual Studio Code, para manejar con el lenguaje Python y sus determinadas librerias. Hice una visualización de los datos en general, para poder ver la relación entre los mismos y poder hacer un debido manejo a los nulos, faltantes y atípicos. Por ejemplo, para datos como el cast, el director o el lugar donde se realizó la producción, era imposible hallar una relación con los otros datos del dataset. Sin embargo, habían identificadores o relación entre algunos datos, como los datos de tipo numérico, ya que podíamos solucionar los nulos de estos, gracias a la variación, la moda y el promedio, creando y analizando filtros por plataforma y tipo de producción; Movies o TV shows. Este proceso se pudo concluir 
