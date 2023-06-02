from furhat_remote_api import FurhatRemoteAPI #importo una libreria que se puede instalar facilemente con el comando en consola: sudo pip install furhat-remote-api

#furhat = FurhatRemoteAPI("192.168.2.65") #creamos el objeto del robot con la ip proporcionada por el robot, tenemos que entrar en ella desde el buscador para gestionar la api
furhat = FurhatRemoteAPI("localhost") #creamos el objeto del robot con la ip del furhat simulado lanzado desde la aplicacion de escritorio por eso localhost
marca = 0 #Marca que uso para saber si es mateo o lucia
furhat.set_voice(name='Lucia') #Inicializo la voz a lucia que es una voz femenina en español
furhat.set_face(character="Isabel",mask="adult") #Inicializo la mascara en Isabel que es un aspecto femenino occidental, el parametro mask puede ser anime o child tambien

#-----------------------------Vectores con posibles cadenas de carácteres que luego uso para saber si lo que ha dicho la persona corresponde a qué accion-----------
saludos =["hola","buenos días", "hola buenos días","hola cómo estás"]
nombre =["hola cómo te llamas","como te llamas","cuál es tu nombre","quién eres"]
funcionalidad =["cómo funcionas","qué haces","hola qué haces","cuéntame sobre este proyecto","cuéntanos sobre este proyecto","qué puedes hacer"]
despedida =["adiós","hasta luego","chao","gracias","hasta luego gracias","adiós gracias","hasta luego gracias","adiós Noa","adios Mateo"]
robotica=["cuéntame sobre la carrera de robótica","cuéntanos sobre la carrera de robótica","hola cuéntame sobre la carrera de robótica"]

while True: 

    furhat.attend(user="CLOSEST") #mira al usuario que designemos en este caso la persona mas cercana
    #users = furhat.get_users() #devuelve una lista con los usuarios(nombre,posx,posy,posz,rotx,roty,rotz) 
    """{'id': 'virtual-user-0', 
    'location': {'x': 0.0, 'y': -0.004999999888241291, 'z': 1.0099999904632568}, 
    'rotation': {'x': 359.71636962890625, 'y': 180.0, 'z': 0.0}}""" 
    #print(furhat.get_gestures())#Este print es para devolver todos los gestos posibles que es capaz de realizar el furhat
    furhat.gesture(name="BrowRaise")#método para realizar un gesto, admite varios parametros en este caso  
    furhat.set_led(red=0, green=255, blue=0) #pone el led debajo del robot en el color elegido en este caso lo pongo verde al inciar la escucha para saber que esta escuchando
    result = furhat.listen(language="es-ES" ) #devuelve dos campos, el campo message con la frase dicha por el usuario y el campo succes(true/false) si ha habido comunicacion 
    #importante poner en el listen el lenguaje en el que estamos hablando para que nos entienda bien, por defecto es Ingles-Estados unidos(en-US)
    #guarda la informacion de la escucha en una cadena de caracteres en result.message
    furhat.set_led(red=0, green=0, blue=255) #pone el Led de debajo del robot en el color elegido RGB en este caso lo pongo en azul al terminar la escucha

    #--------------------Aqui empieza la eurística, que simplemente comprueba si lo dicho por el humano corresponde a alguna frase de los diccionarios------------

    if result.message in saludos: #Si lo que se ha dicho es un saludo de dentro del vector de saludos
            furhat.set_led(red=0, green=100, blue=50)   #Pongo este led para cuando está hablando
            furhat.gesture(name="Wink") #Hace el gesto de guiñar el ojo para saludar
            furhat.say(text="Buenos dias!",blocking = True) #para hablar el campo text es lo que quieres decir y el blocking si quieres que no continue el programa hasta que acabe, en este caso si por eso está en True
    elif result.message in robotica: #si lo que se ha dicho está en el vector robotica

            furhat.gesture(name="Nod") #asiente

            furhat.set_led(red=0, green=100, blue=50)        
            furhat.say(text="Sí claro") 
            furhat.gesture(name="Blink") #pestañea
            furhat.say(text="En el grado de robótica puedes aprender a programarme tanto a mi como a mis otros compañeros robots",blocking = True) 

    elif result.message in nombre : #Si le pregunta su nombre

            furhat.set_led(red=0, green=100, blue=50) 

            if (marca == 0): #Si es noa dira que es noa si es mateo dira que es mateo, la marca la cambio por 0 o 1 cuando cambia de personalidad

                furhat.say(text="Me llamo Noa") 

            else: 

                furhat.say(text= "Me llamo Mateo") 

    elif result.message in despedida: #Si se ha despedido
            furhat.gesture(name="ExpressSad") #Expresa tristeza
            furhat.say(text ="Hasta la próxima, un placer!") 
            furhat.set_visibility(visible=0,duration=1000) #Desvanece durante un segundo?
    elif result.message =="quiero hablar con Mateo": 

            if marca == 0: #si le dice que quiere hablar con mateo y no es mateo lo llama y lo cambia

                furhat.say(text ="Vale, lo llamo",blocking = True) 

                furhat.set_voice(name='Sergio-Neural') #cambia la voz a la masculino

                furhat.set_face(character="James",mask="adult") #cambia el personaje a masculino occidental

                furhat.say(text ="Hola, me llamo Mateo",blocking=True) #se presenta

                marca = 1 #pone la marca a 1 para saber que es mateo

            else: 
                furhat.set_face(character="James",mask="adult") #si es mateo dice que es mateo(el cambio es por si seleccione otra cara manualmente)
                furhat.say(text="Yo soy Mateo",blocking=True) 

    elif(result.message =="quiero hablar con Noa"): 

        if marca == 1: #el mismo comportamiento que antes pero solo si es noa

            furhat.say(text ="Vale, la llamo",blocking= True) 
            furhat.set_voice(name='Lucia') 
            furhat.set_face(character="Isabel",mask="adult") 
            furhat.say(text ="Hola, me llamo Noa",blocking=True) 
            marca = 0   
        else: 

            furhat.say(text="Yo soy Noa",blocking=True) 


    elif result.message in funcionalidad: 
            #si el mensaje pregunta funcionalidad 
            furhat.say(text="El proyecto desarrolla la interacción persona-robot en la cual la conversación esté cargada de reacciones emocionales,leyendo el contexto conversacional",blocking = True)
            furhat.say(text="Pudiendo detectar expresiones, y simular emociones con las expresiones faciales en la cara del robot",blocking = True)
            furhat.gesture(name="BigSmile",blocking= True)
            furhat.gesture(name="Roll",blocking= True)
            furhat.gesture(name="ExpressFear",blocking= True)
            furhat.gesture(name="ExpressDisgust",blocking= True) 
            furhat.gesture(name="Shake",blocking= True)
            furhat.gesture(name="CloseEyes",blocking= True)
            furhat.gesture(name="OpenEyes",blocking= True)
            furhat.gesture(name="Surprise",blocking= True)
            furhat.gesture(name="Nod",blocking= True)
    elif(result.message=="dónde estamos"):
            furhat.say(text="Estamos en Santiago de Compostela, en la Meiker feir Galicia",blocking= True)
    else: 

            furhat.gesture(name="Roll",blocking= True) 
            furhat.say(text="No tengo respuesta para eso",blocking=True) 
    if result.success == False:
        furhat.say(text="Hola, hay alguien ahí?",blocking=True) 
        furhat.set_led(red=255, green=0, blue=0) 

     