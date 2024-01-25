from IPython.display import display
from IPython.display import Markdown

import google.generativeai as palm

key= "Here goes your gemini api key! See The Official Page."
palm.configure(api_key = key)


def promptHandler( case, prompt ):

  if case == 1:

  # try 1: solo una prompt
    try:
      model = palm.GenerativeModel('gemini-pro')
      chat = model.start_chat(history=[])
      response = chat.send_message(prompt)
      textResponse= response.text.split('•')[0]
      return textResponse
    except ValueError as error:
      print("Caso 1 fallido, motivo:\n", str(error), '\n')
      return "Sinceramente, no entiendo."


  # try 2: solo una imagen a describir
  if case == 2:

    try:
      import PIL.Image
      img= PIL.Image.open("imagen.jpg")
      model = palm.GenerativeModel('gemini-pro-vision')

      response = model.generate_content(img)
      textResponse= response.text.split('•')[0]
      
      return textResponse 
    except ValueError as error:
      print("Caso 2 fallido, motivo:\n", str(error), '\n')
      return "No pude procesar la imagen, algo raro paso xd"



  #try 3: Una imagen y una prompt
  if case == 3:
    
    try:
      import PIL.Image
      img= PIL.Image.open("imagen.jpg")
      model = palm.GenerativeModel('gemini-pro-vision')

      response = model.generate_content([prompt, img])
      textResponse= response.text.split('•')[0]

      return textResponse
    except ValueError as error:
      print("Caso 3 fallido, motivo:\n", str(error), '\n')
      return "No entiendo que me paso, pero no pude procesarlo."

