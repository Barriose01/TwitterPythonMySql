# TwitterPythonMySql

ATENCION: Debido a que es un programa pensado en funcionar en un servidor local, se debe crear la base de datos
con el query sql que se dejo junto a los archivos. Se deben ejecutar las sentencias una por una

El programa se ejecuta mediante el archivo "menuPrincipalTwitter.py".
Al hacerlo, nos apareceran las siguientes opciones:

![image](https://user-images.githubusercontent.com/107152796/179851618-a2e36a8e-0b6e-496c-b81f-2d80e004f52c.png)

Pasaremos por las dos primeras opciones.

Al escoger la opcion de registrar un usuario, el programa nos pedira que elijamos un nombre de usuario y una clave,
la cual la va a volver a preguntar para asegurarse de que el usuario la recuerde:

![image](https://user-images.githubusercontent.com/107152796/179852504-0c752cd1-e683-4714-ad01-41f648291793.png)

Si se trata de registrar con un nombre de usuario que ya existe, el programa nos indicara de la existencia de este
usuario y no nos dejara registrarnos:

![image](https://user-images.githubusercontent.com/107152796/179852653-4820ede2-9a81-490f-a73d-d5e4babfcd0e.png)

Al iniciar sesion, nos pedira el nombre y la clave. Si estos estan registrados, el programa nos mostrara un nuevo menu:

![image](https://user-images.githubusercontent.com/107152796/182677579-4220a933-132d-41b5-a0a6-26ca15954e05.png)

Tenemos distintas opciones que podemos utilizar. Creamos un post de la siguiente manera:

![image](https://user-images.githubusercontent.com/107152796/182679044-2c0f374a-c0c3-4d64-b6d7-748b22106c2f.png)

Si queremos revisar las publicaciones que hemos hecho, entramos en la opcion para ver nuestras publicaciones:

![image](https://user-images.githubusercontent.com/107152796/182679170-83927fff-c9b6-4b4a-a162-29e2fb5fe6b5.png)

Al escribir publicaciones, tenemos la opcion de escribir hashtags (#) como en Twitter. Esto nos permitira realizar una busqueda
sobre las publicaciones utilizando este hashtag como filtro.

Vamos a realizar algunas publicaciones utilizando hashtags para luego realizar una busqueda especial utilizando estas etiquetas:
![image](https://user-images.githubusercontent.com/107152796/182679323-bd729531-b0c0-4855-a4fa-e0bf21fca71f.png)
![image](https://user-images.githubusercontent.com/107152796/182679356-99d3539a-6fd7-4d55-982b-4b7b566ce157.png)

Vamos a realizar una busqueda utilizando alguno de los hashtags que creamos. Elegimos la opcion que dice "Buscar posts por Hashtags" e introducimos
el hashtag que querramos buscar:

![image](https://user-images.githubusercontent.com/107152796/182679632-6477830c-75a7-4b03-804b-d0e7d0928a98.png)

Nos aparecen las publicaciones que contienen la palabra que ingresamos como hashtag. Crearemos otro hashtag diferente para comprobar que la busqueda sirve:

![image](https://user-images.githubusercontent.com/107152796/182679790-0bd5dd97-38be-487f-91e4-3bda09c28b5b.png)
![image](https://user-images.githubusercontent.com/107152796/182679845-ae4c1485-a080-486f-8808-3becb6313364.png)

Podemos ver cuales son los hashtags mas populares ingresando a la opcion "Ver Hashtags mas populares". Se nos mostrara una lista de los 10 hashtags mas
utilizados por los usuarios, de mas utilizados a menos utilizados:

![image](https://user-images.githubusercontent.com/107152796/182680113-227dfd64-9f83-42ce-9db4-bb3b0d54ac40.png)

Como apenas tenemos un solo usuario y solo hemos ingresado 3 hashtags distintos, solamente nos apareceran 3 hashtags como los mas populares. Si prestamos atencion,
podremos ver que el hashtag #hashtag esta en primera posicion, esto debido a que es el hashtag que mas se ha utilizado. Si realizamos otras publicaciones utilizando
otros hashtags, pueden cambiar de posicion:

![image](https://user-images.githubusercontent.com/107152796/182680422-ca86cfa9-2b3a-42ae-9cc0-ff4ce6c263fd.png)
![image](https://user-images.githubusercontent.com/107152796/182680462-9cac10b0-d771-444b-8232-2c6ed42f39eb.png)

Ya que tenemos varias publicaciones, podremos verlas ingresando a la opcion "Ver tus posts":

![image](https://user-images.githubusercontent.com/107152796/182680616-b807c5e8-e62d-4a88-be5d-717823061275.png)

Si prestamos atencion, nos daremos cuenta de que aparecen desde el ultimo post hasta el primero. Si queremos ver los posts desde mas antiguos a mas recientes,
elegimos la opcion que dice "Ver tus posts (de mas antiguos a mas recientes)":

![image](https://user-images.githubusercontent.com/107152796/182680867-e97f1e0d-9cc9-4a8f-9671-31a46dcadffe.png)

En la opcion (8), podremos borrar un determinado post. Al entrar aqui, solamente tendremos que ingresar el id del post que querramos eliminar. Este id se mostrara
a la izquierda de la publicacion:

![image](https://user-images.githubusercontent.com/107152796/182681145-d6551835-67a5-426a-9cac-a752f7224522.png)

En este caso, eliminamos la publicacion que decia: "prueba #hashtag". Para verificar de que se elimino esta publicacion, veremos nuevamente nuestros posts:

![image](https://user-images.githubusercontent.com/107152796/182681349-76ef31fc-434e-436b-aeac-d266452a032b.png)

Como se puede ver, ya no aparece esta publicacion.

Para las siguientes funcionalidades, cerraremos sesion y crearemos un nuevo usuario:

![image](https://user-images.githubusercontent.com/107152796/182681678-a67080d5-2ca8-423c-9a8b-6f2330ef7d93.png)

Si ingresamos en la opcion "Ver posts", se nos mostraran todas las publicaciones que se han hecho utilizando este programa, independientemente del usuario:

![image](https://user-images.githubusercontent.com/107152796/182681797-d3b87dd5-22e1-4a0c-ae50-9f678392665f.png)

Como nos podemos dar cuenta, iniciamos sesion con usuario2, pero podemos ver las publicaciones hechas por usuario1

Para demostrar que es posible ver todos los posts de los usuarios que hayan realizado esta accion, crearemos un nuevo post y veremos nuevamente las publicaciones
que se han hecho:

![image](https://user-images.githubusercontent.com/107152796/182682195-cc320148-3a31-470a-82b8-46d803074ccd.png)
![image](https://user-images.githubusercontent.com/107152796/182682238-f986fda4-c563-43f0-80bc-200b8a7408b8.png)

Podemos ver que se encuentran tanto los posts de usuario como de usuario2.

Para buscar las publicaciones de un determinado usuario, solo basta con elegir la opcion que dice "Buscar posts por usuario". Funciona de la misma manera que
cuando buscabamos posts por el Hashtag, solo que introduciremos el nombre del usuario que querramos ver. En este caso, veremos las publicaciones de usuario2:

![image](https://user-images.githubusercontent.com/107152796/182682582-2daeb299-fea2-40c8-955d-25cbe5d8751c.png)

Para eliminar todos los posts, entraremos a la opcion que dice "Borrar todos tus posts". Se nos mostrara una pantalla de seleccion en donde nos pregunta si
estamos seguros de querer realizar esa operacion. Si aceptamos, se nos borraran todas las publicaciones:

![image](https://user-images.githubusercontent.com/107152796/182683036-14eb356f-7cab-4f2d-8b9b-6aec1958601d.png)

Si queremos ver nuestros posts, nos mostrara esto:

![image](https://user-images.githubusercontent.com/107152796/182683130-32b9511f-6ab7-431c-8aa6-b3e495c6f141.png)

Esto debido a que eliminamos todas las publicaciones de usuario2. Si vemos los hashtags populares, tambien se eliminaran aquellos ingresados por usuario2, ya que
se eliminaron sus publicaciones:

![image](https://user-images.githubusercontent.com/107152796/182683315-8db138bf-bfba-4312-a908-3f8116f50861.png)

Cuando hicimos una publicacion con usuario2, utilizamos el hashtag #post, por lo que en un inicio apareceria en la lista de los hashtags mas populares, ya que, al solo
tener dos usuarios y ser la primera vez que se usa esta etiqueta, tendria que aparecer en esta lista, pero como borramos todas las publicaciones, tambien se borran 
aquellas que incluian hashtags, por lo que ya no aparece en esta lista.






















