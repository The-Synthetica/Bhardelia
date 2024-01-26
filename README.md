# 💀 Bhardelia
Un-Official Google Bard bot. Using the Gemini Api from Google.

(for entertainment use)

![](https://i.imgur.com/RAJC66P.png)
# 📚 Modules

***app.py*** : This module uses the Gemini Api to request a textual response, the process is separated in 3 possible cases of request, based on the idea that the simple text responses can have an historial that the other cases apparently cant have.

- Case 1: Simple text request, only a prompt is given.
- Case 2: Simple image request, only a image is given.
- Case 3: A combination of case 1 & 2

###### 

- `promptHandler( case, prompt )`: The only functiont of this module, u give it a type of case and a prompt, and will respond based on the case type.


> Note: Really, i tried everything, but the damn thing is unable to give a response if i use the chat option, so the responses cant be saved on the historial. What it means that is uncapable of remember the image requests (case 2 and 3)

###### 

> Potentially, all the cases can be handled as a variation of case 3.

***msgAux.py*** : Message processing. On resume, this module charges two functions.

- `msgParser( msg, maxCaracter )`: Divides a long text response into subtexts that arent more larger than the max character number. On discord the lenght of a message cant be more than 2000 characters, so it divides the long messages into sub-messages with no more than 1900 characters

- `searchCode( msg )`: Searchs the text-channel ID for the bot settings, on the "setChannel" message.

> Note that in the main file, anyway i have a message handler, but its the same thing.

***main.py***  : Discord client management and combines all the modules. Initializes the client, handles the messages and sends the first message for settings on the first text-channel that can be found. 

>The code is designed to be intuitive, so i dont be describing the events, but if u want to see more, u can read the notes on the code! (Pero vas a tener que saber español xd)

***⚠️ Important Variables:***

- `promptTo` : Its a pre-prompt addition, this forces the bot to respond in spanish and makes him act more "bot for discord" than Bard for default.

> Note: This makes the chat history a little bit confuse for the Gemini Api, so its no the best way to make the bot act "natural". A possible solution maybe its "fine tunning" but the api doesnt have any information about this. (Maybe i will try it with dolphin mixtral, stills being difficult) 

- `servers` : Saves the server ID and the established text channel on a python dictionary. I used the pickle library for use this option. And the server code is not private, its safe!


# 🔧 Future upgrades! 

This project isnt prepared for high demand requests. 

Its easy for any person make the bot down by multiple request or find some exceptions. 

The idea behind this is add multiple NLP-AI's to my discord channel. And make some experiments with that, like make them talk (probably a bad a idea, but intresting).

We can implement a fine tunning for the bot and find a hosting to! 

At the moment, the bot lost the only free hosting lol. (Pagar un server en dolares para este proyecto no esta en mi abanico de posibilidades. #Argentina )

Important!: The history chat of the bot doesnt work in high demand request due its a simple client for all the servers, so, if i want to have a record of all the servers, each server must have their own client, or the client should admit have different records. (I try this last one, but the client dont admint the chat history object)

# 🔗 Links

### Related content:

[![gemini-api](https://img.shields.io/badge/-Gemini%20Api%20Docs-informational?logo=Google&style=for-the-badge&logoColor=4285f4&color=fafafa&labelColor=fafafa)](https://ai.google.dev/tutorials/python_quickstart "Gemini-Api")

[![Discord.py Api](https://img.shields.io/badge/-Discord.py-informational?logo=Discord&style=for-the-badge&logoColor=bdc733&color=555555&labelColor=052d57)](https://discordpy.readthedocs.io/en/stable/)

[![Invite Bhardelia](https://img.shields.io/badge/-Invite%20Bhardelia-informational?logo=Discord&style=for-the-badge&logoColor=ffffff&color=fafafa&labelColor=5865f2&)](https://discord.com/oauth2/authorize?client_id=1198735562706792518&scope=applications.commands%20bot&permissions=537159744)

### About Me:

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://the-synthetica.github.io/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/franciscorizzi/)

[![linktree](https://img.shields.io/badge/linktree-black?style=for-the-badge&logo=linktree&logoColor=4DCC17)](https://linktr.ee/FranciscoRizzi)


##### Besitos! ❤️
