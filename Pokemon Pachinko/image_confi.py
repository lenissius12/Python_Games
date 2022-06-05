# image_config.py
from tkinter import PhotoImage
from PIL import Image, ImageTk

# nuevo la libreria
import os
from pathlib import Path
# para systema usando la ruta como una herramienta
filename1 = os.path.join(os.path.dirname(__file__),'C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pikachu.png')
filename2 = os.path.join(os.path.dirname(__file__),'C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Shellder.png')
filename3 = os.path.join(os.path.dirname(__file__),'C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Magnemite.png')
filename4 = os.path.join(os.path.dirname(__file__),'C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pokeball.png')
filename5 = os.path.join(os.path.dirname(__file__),'C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Psyduck.png')
filename6 = os.path.join(os.path.dirname(__file__),'C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Seven.png')
filename7 = os.path.join(os.path.dirname(__file__),'C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Team_Tocket.png')

image1 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pikachu.png')
resize_Image1 = image1.resize((150,150),Image.ANTIALIAS)
image2 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Shellder.png')
resize_Image2 = image2.resize((150,150),Image.ANTIALIAS)
image3 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Magnemite.png')
resize_Image3 = image3.resize((150,150),Image.ANTIALIAS)
image4 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pokeball.png')
resize_Image4 = image4.resize((150,150),Image.ANTIALIAS)
image5 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Psyduck.png')
resize_Image5 = image5.resize((150,150),Image.ANTIALIAS)
image6 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Seven.png')
resize_Image6 = image6.resize((150,150),Image.ANTIALIAS)
image7 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Team_Rocket.png')
resize_Image7 = image7.resize((150,150),Image.ANTIALIAS)
image_decor1 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Cleffairy.png')
resize_decor1 = image_decor1.resize((80,89),Image.ANTIALIAS)

backPic = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pokeball_Background.png')
resize_Background = backPic.resize((1080,720),Image.ANTIALIAS)
