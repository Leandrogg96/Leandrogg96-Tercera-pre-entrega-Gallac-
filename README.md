# Leandrogg96-Tercera-pre-entrega-Gallac-
Tercera pre-entrega - Curso Python - comision 48265

Pasos para ejecutar el proyecto (tercera pre-entrega):

1.- Clonar el proyecto en el directorio deseado;

2.- Dentro de la carpeta del proyecto, instalamos un entorno virutal, llamamos al administrador de paquetes y con el comando: "pip install vitualenv"

3.- Activamos el entorno virtual;

4.- En caso de no tener el framework "Django" instalado, lo hacemos utilizando el administrador de paquetes "pip": "pip install django";

5.- Realizamos la migraciones que son requeridas con el comando: "python manage.py migrate";

6.- Ejecutamos el servidor con el comando: "python manage.py runserver".


  Mi idea de este tercer proyecto es hacer un base de datos para un torneo de fútbol, donde se puedan registrar los equipos que vayan a participar,
el entrenador de cada equipo, los jugadores y hasta los arbitros que vayan a participar. Con esta aplicación logro recaudar toda la información, detallada de datos de mi interés,
de todas las personas que intervengan en dicho torneo.

  Inciando la página se abre una "pantalla principal" con un menú de cabecera donde tenemos acceso a los registros de los distintos entes que participen 
y deban registrase. 

  Desde la barra de navegación, completanto la URL de incio con: "/admin" ingresamos al panel de administrador, donde se pueden registrar las autoridades del torneo, y así
también se pueden cargar de manera manual los afectados al torneo. 
  
  Tenemos tambien la opción de búsqueda de algún jugador, completanto la URL de incio con: "/busqueda-jugador", ingresando el apellido del mismo, donde en caso de que,
este registrado, se lo muestre por pantalla, caso contrario, muestra un mensaje de "no registrado".
