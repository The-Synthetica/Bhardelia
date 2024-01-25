
# Corta un mensaje largo en una cantidad definida de caracteres a mandar.
# Devuelve una lista
def msgParser( msg, maxCaracter):
    
    arr= msg.split()
    parsedMsg= ""
    res=[]

    def wordParser( word ):
        for i in range(0, len(word), maxCaracter):
            res.append( word[i:i+maxCaracter])


    for word in arr:

        if len(word) > maxCaracter:
            #si la palabra es mas grande que nuestro propio limite
            wordParser( word )

        else:
            if (len(parsedMsg) + len(word)) > maxCaracter:
                res.append(parsedMsg)
                parsedMsg = word + " "
            
            else:
                parsedMsg+= word + " "
    else:
        res.append(parsedMsg)
        return res
    
# Busca en el mensaje de configuracion el codigo del canal del texto que se pretende encontrar
# Devuelve un string
def searchCode( msg ):
    wrappedMsg= msg
    firstIndex= wrappedMsg.find("<#") + 2
    wrappedMsg= wrappedMsg[firstIndex : ]
    lastIndex= wrappedMsg.find(">")
    wrappedMsg= wrappedMsg[0 : lastIndex]

    return wrappedMsg