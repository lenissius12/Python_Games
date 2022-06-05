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

prize_image1 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pikachu.png')
prize_resize_Image1 = prize_image1.resize((35,35),Image.ANTIALIAS)
prize_image2 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Shellder.png')
prize_resize_Image2 = prize_image2.resize((35,35),Image.ANTIALIAS)
prize_image3 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Magnemite.png')
prize_resize_Image3 = prize_image3.resize((35,35),Image.ANTIALIAS)
prize_image4 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pokeball.png')
prize_resize_Image4 = prize_image4.resize((35,35),Image.ANTIALIAS)
prize_image5 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Psyduck.png')
prize_resize_Image5 = prize_image5.resize((35,35),Image.ANTIALIAS)
prize_image6 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Seven.png')
prize_resize_Image6 = prize_image6.resize((35,35),Image.ANTIALIAS)
prize_image7 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Team_Rocket.png')
prize_resize_Image7 = prize_image7.resize((35,35),Image.ANTIALIAS)
prize_backPic2 = Image.open('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pokeball_Background2.png')
prize_resize_Background2 = prize_backPic2.resize((400,720),Image.ANTIALIAS)