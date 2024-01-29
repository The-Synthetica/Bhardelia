import discord
import requests
import pickle

import app
import msgAux as aux

# Cargamos el diccionario que tiene los canales configurados de los servidores
with open('servers.pkl', 'rb') as fp:
    servers = pickle.load(fp)
    print(servers)

# Nuestro parser de mensajes.
async def messageHandler( content, message ):
    arr= aux.msgParser(content, 1900)

    for elem in arr:
        await message.channel.send(elem)

# Prompt Engineering para hacer que responda menos trivialmente
# Le agrega esta frase atras de la peticion, y fuerza a que hable en español!
promptTo= "Eres Bhardelia, un bot asitente de discord, respondes la siguiente consulta: "

# Configuracion de cliente
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



# Cliente inicializado correctamente:
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



# El cliente es invitado a un nuevo servidor
@client.event
async def on_guild_join(guild):

# Enviamos un mensaje personalizado explicando como configurar el bot
    textChannels = guild.text_channels

    msg='''***Hola! Soy @Bhardelia, Gracias por invitarme. :kissing_heart:***
    *Soy un Bot no oficial que utiliza la API de Google Gemini para interactuar con los mensajes específicos de un canal. *
    ﻿  

    ***:nut_and_bolt:﻿﻿  Configuración: :screwdriver:﻿﻿***
    *Necesito que especifiques en que canal voy a funcionar, enviando un mensaje con el siguiente formato: *
    ﻿
    `" @Bhardelia﻿ setChannelTo #<TextChannel> "`
    ﻿
    ***Recordá mencionarme a mi y al canal!*** 
    ***Así puedo comprenderlo. Además, asegúrate de que puedo acceder al mismo. :smile:﻿﻿ ***

    ﻿:computer: *Puedo escanear imágenes, responder a tus solicitudes y ayudarte en lo que necesites!*  :toolbox:
    ﻿

    ***Nota: De sentirme incomodidad por algún comentario, procederé directamente a ignorarlo. :face_with_raised_eyebrow:﻿﻿  ***
    '''

    # Buscamos un canal que sea valido para enviar el mensaje
    for channel in textChannels:
        try: 
            await client.fetch_channel(channel.id)
            await channel.send(msg)
            print("encontre uno")
            break
        except:
            print("No encontramos un canal valido para mandar el mensaje de configuracion, pero no importa, ellos se lo pierden.")
            pass

    # Problema: Notemos que cuando el bot recibe un mensaje, primero se fija si el servidor en algun momento fue registrado.
    # Pero si buscamos una key inexistente en el diccionario, nos va a tirar un error de index.
        
    # Solucion: Simple, cada vez que un servidor nuevo es agregado, lo ponemos en el diccionario con un valor default (cero) 
        
    servers[str(guild.id)]= 0

    # Guardamos nuestro nuevo diccionario (con la nueva configuracion default)
    with open('servers.pkl', 'wb') as fp:
        pickle.dump(servers, fp)
        print('dictionary saved successfully to file')



# Cliente recibe un mensaje
@client.event
async def on_message(message):
    
    # Ignoramos nuestros propios mensajes.
    if message.author == client.user:
        return
    
    # Mensaje de configuracion de canal:
    if message.content.startswith('<@1198735562706792518> setChannelTo'):
        # Hay un cambio de configuracion.
            # Buscamos el canal que deberia estar adjunto y vemos si es valido. 
        channelID= int(aux.searchCode(message.content))
      
        # De ser un canal valido, toca actualizar la informacion.
            # Obtenemos el ID del servidor.
        try:
            await client.fetch_channel(channelID)
            serverID= str(message.guild.id)
            servers[serverID]= channelID

            # Guardamos nuestro nuevo diccionario (con la nueva configuracion)
            with open('servers.pkl', 'wb') as fp:
                pickle.dump(servers, fp)
                print('dictionary saved successfully to file')
            
            await message.channel.send("Canal configurado exitosamente!")

        # Si no encuentra el canal
        except: 
            await message.channel.send("No pude encontrar el canal que me estas pidiendo. Asegurate de que yo este incluida en ese canal")

        return
    

    
    # Recibimos un mensaje que:
    #                           - No es de configuracion
    #                           - Y en el canal configurado del servidor
    elif(message.channel.id == servers[str(message.guild.id)]):
        print(message.channel.id)
        print(message.content)

        # El mensaje tiene alguna foto adjunta??
        adjuntos= message.attachments
        if( len(adjuntos) > 0):
            # Varios adjuntos
            if(len(adjuntos) > 1):
                await message.channel.send('Solo puedo procesar un solo adjunto a la vez!')

            # Solo un adjunto
            else:
                archivo= adjuntos[0]

                # Si el archivo es una foto, la descargamos.
                if ( archivo.filename.endswith(".jpg")
                    or archivo.filename.endswith(".jpeg")
                    or archivo.filename.endswith(".png")
                    or archivo.filename.endswith(".webp")
                    or archivo.filename.endswith(".gif")):

                    img_data = requests.get(archivo.url).content
                    with open("imagen.jpg", "wb") as handler:
                        handler.write(img_data)
                else:
                    await message.channel.send('No tolero ese tipo de archivos.')
                

                #Esta foto tiene una prompt??
                if(message.content != ""):
                    print("Tipo de intento 3")
                    prompt= message.content
                    respuesta= app.promptHandler(3, promptTo + prompt)
                    await messageHandler( respuesta, message )

                
                else:
                    print("Tipo de intento 2")
                    prompt= message.content
                    respuesta= app.promptHandler(3, promptTo + "Describre la imagen por favor!")
                    await messageHandler( respuesta, message )

                    
        
        # No hay adjuntos
        else:
            print("Tipo de intento 1")
            prompt= message.content
            respuesta= app.promptHandler(1, promptTo + prompt)
            await messageHandler( respuesta, message )
        # await message.channel.send('Hello!')


# Ejecutamos el cliente.
import os

#Usen variables de entorno ♥
token= str( os.getenv("discordToken") )
client.run( token )

# Notita, les recomendaria usar variables de entorno si tienen la posibilidad o en su defecto claramente
# NO DEJEN VISIBLE SU TOKEN
# Esto esta asi porque lo corri 24/7 en la pc. Besitos ♥