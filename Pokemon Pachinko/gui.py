from tkinter import Button, PhotoImage, Tk, Label
from PIL import  ImageTk
from figure import figure
from image_confi import *
import pygame


window = Tk()
pygame.mixer.init()
pygame.mixer.music.load('music/Pokemon_OST.mp3')
pygame.mixer.music.play()
#WINDOW CONFIGURATION
#--------------------------------------------------
#--------------------------------------------------
window.geometry("1080x720")
window.title("Pokemon Slot Coin")
icon = PhotoImage(file='images/Pokeball_title.png')
window.iconphoto(False,icon)

#BACKGROUND CONFIGURATION
#-------------------------------------------------
background_ = ImageTk.PhotoImage(resize_Background)
Image1 = ImageTk.PhotoImage(resize_Image1)
Image2 = ImageTk.PhotoImage(resize_Image2)
Image3 = ImageTk.PhotoImage(resize_Image3)
Image4 = ImageTk.PhotoImage(resize_Image4)
Image5 = ImageTk.PhotoImage(resize_Image5)
Image6 = ImageTk.PhotoImage(resize_Image6)
Image7 = ImageTk.PhotoImage(resize_Image7)
decor1 = ImageTk.PhotoImage(resize_decor1)

#LABEL CONFIGURATION
#------------------------------------------
#------------------------------------------
fig1 = figure(1,220,280,resize_Image1)
fig2 = figure(2,460,280,resize_Image2)
fig3 = figure(3,700,280,resize_Image3)

background_label = Label(window,image=background_)
background_label.place(x=0,y=0)
decor1_label = Label(window,image=decor1)
decor1_label.place(x=100,y=600)
decor2_label = Label(window,image=decor1)
decor2_label.place(x=900,y=600)
credits_label = Label(window,
                      text="CREDITS:",
                      font='FreeMono',
                      bg='black',
                      fg='white',
                      borderwidth=5,
                      highlightthickness=5,
                      highlightbackground="#c4a200",
                      padx=20,
                      pady=5
                      )
credits_label.place(x=260,y=20)
label1 = Label(window,
               image=fig1.image,
               borderwidth=10,
               highlightthickness=10,
               highlightbackground='black')
label1.place(x=fig1.posX,y=fig1.posY)
label2 = Label(window,
               image=fig2.image,
               borderwidth=10,
               highlightthickness=10,
               highlightbackground='black')
label2.place(x=fig2.posX,y=fig2.posY)
label3 = Label(window,
               image=fig3.image,
               borderwidth=10,
               highlightthickness=10,
               highlightbackground='black')
label3.place(x=fig3.posX,y=fig3.posY)




#BUTTON CONFIGURATION
#--------------------------------------------
play_button = Button(window,
                     text='PLAY',
                     bd=5,
                     fg="white",
                     bg="#e5a200")
play_button.place(x=540,y=620)


window.mainloop()
