# figure.py
from operator import pos
from tkinter import *
from PIL import  ImageTk


class figure:
    def __init__(self,ID,posX,posY,image):
        self.ID = ID
        self.posX = posX
        self.posY = posY
        self.image = ImageTk.PhotoImage(image)
