# Furhat-Example
Instrucciones para usar el Furhat:
Si queréis usar un código python primero instalar la api a través del comando:
pip install furhat-remote-api
o
sudo pip install furhat-remote-api
Luego dentro de la interfaz web del furhat(si ponemos la ip del furhat en nuestra red, en un buscador, saldrá esta interfaz), hay un botón que pone Remote API, cuando le demos saldrá que se está ejecutando una api, que lo que hace es esperar a que lancemos la api a través de la ventana de comandos
Código ejemplo de Python comentado, para usarlo es necesario estar en la misma red que el furhat, y ejecutar el código con la librería instalada, a través de una ventana de comandos con el comando
python nombredelarchivo.py
En simulación:
Iniciar furhat SDK(aplicación descargable en la web de furhat)
Iniciar Virtual Furhat, y dentro de ahí Open Web interface para poder simular personas en la cámara, probar cosas manualmente, habilitar el uso de apis…
Si queremos usar una api usamos el mismo código anterior pero en vez de poner la ip del robot ponemos como ip “locahost”

En real:
Primero enchufamos el furhat(obviamente) y le damos al botón de encendido
Una vez se encienda la cara con una cara predeterminada, a un costado encotraremos un botón que es a la vez botón y selector, si pulsamos abrirá una interfaz, y pulsar equivale a enter y girar la ruedita sirve para navegar en la interfaz, esta sale proyectada en la propia cara
Lo primero que debemos hacer es conectarla a la red que esté usando nuestro ordenador donde vamos a ejecutar o probar el robot. Normalmente necesitaremos un teclado que se puede conectar al furhat en uno de los puertos USB que tiene. Una vez conectemos a la red, nos saldrá una IP en el robot, esta IP es la que debemos poner en nuestro navegador para acceder a él manualmente, y es la que debemos poner en nuestro archivo Python para que se conecte a él.
La parte de ejecutar el Python es igual en simulación que en el real, solo cambiando la ip de “localhost” a “192.101.XXX”la que tenga el robot

Enlaces de Interés:
Documentacion de la API
https://docs.furhat.io/remote-api/
Para descargar la aplicación de escritorio para simular, necesitamos pedirla a la compañía, te registras fácilmente y proporcionas unos datos
https://furhatrobotics.com/requestsdk/ 
Video en inglés de tutoriales para usar el furhat 
https://www.youtube.com/watch?v=-9YXKNyOiFs&list=PLKiYzqmsr557iXGzzzXKiJ8tZFoSqei0o
https://www.youtube.com/watch?v=zij-8u4CDvo&list=PLKiYzqmsr555P9i-LlwZxpilQDfbgFzhy
