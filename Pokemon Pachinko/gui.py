from multiprocessing.sharedctypes import Value
from random import randint
from tkinter import Button, PhotoImage, Tk, Label, Toplevel, messagebox
from PIL import  ImageTk
from figure import figure
from image_confi import *
from image_prize_confi import *
from player import *


import pygame


def execute():
    window = Tk()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/music/Pokemon_OST.mp3')
    pygame.mixer.music.play()
    #WINDOW CONFIGURATION
    #--------------------------------------------------
    #--------------------------------------------------
    window.geometry("1080x720")
    window.title("Pokemon Slot Coin")
    window.iconbitmap('C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pokeball_title.png')
    icon = PhotoImage(file='C:/Users/usuario1/Documents/UNIVERSIDAD/Python/PROJECTS/JACKPOT/images/Pokeball_title.png')
    window.iconphoto(False,icon)
    flag = True

    #BACKGROUND CONFIGURATION
    #-------------------------------------------------
    background_ = ImageTk.PhotoImage(resize_Background)
    background2_ = ImageTk.PhotoImage(prize_resize_Background2) 
    Image1 = ImageTk.PhotoImage(resize_Image1)
    Image2 = ImageTk.PhotoImage(resize_Image2)
    Image3 = ImageTk.PhotoImage(resize_Image3)
    Image4 = ImageTk.PhotoImage(resize_Image4)
    Image5 = ImageTk.PhotoImage(resize_Image5)
    Image6 = ImageTk.PhotoImage(resize_Image6)
    Image7 = ImageTk.PhotoImage(resize_Image7)
    decor1 = ImageTk.PhotoImage(resize_decor1)

    final_Prize1 = ImageTk.PhotoImage(prize_resize_Image7)
    final_Prize2 = ImageTk.PhotoImage(prize_resize_Image6)
    final_Prize3 = ImageTk.PhotoImage(prize_resize_Image5)
    final_Prize4 = ImageTk.PhotoImage(prize_resize_Image4)
    final_Prize5 = ImageTk.PhotoImage(prize_resize_Image3)
    final_Prize6 = ImageTk.PhotoImage(prize_resize_Image2)
    final_Prize7 = ImageTk.PhotoImage(prize_resize_Image1)

    #LABEL CONFIGURATION
    #------------------------------------------
    #------------------------------------------
    fig1 = figure(1,220,280,resize_Image1)
    fig2 = figure(2,460,280,resize_Image2)
    fig3 = figure(3,700,280,resize_Image3)
    fig4 = figure(-1,-1,-1,resize_Image4)
    fig5 = figure(-1,-1,-1,resize_Image5)
    fig6 = figure(-1,-1,-1,resize_Image6)
    fig7 = figure(-1,-1,-1,resize_Image7)
    play3r = player(0,0)


    background_label = Label(window,image=background_)
    background_label.place(x=0,y=0)
    decor1_label = Label(window,image=decor1)
    decor1_label.place(x=100,y=600)
    decor2_label = Label(window,image=decor1)
    decor2_label.place(x=900,y=600)
    money_label = Label(window,
                        text="MONEY:",
                        font='FreeMono',
                        bg='black',
                        fg='white',
                        borderwidth=5,
                        highlightthickness=5,
                        highlightbackground="#c4a200",
                        padx=20,
                        pady=5
                        )
    money_label.place(x=435,y=20)
    money_count_label = Label(window,
                        text=play3r.money,
                        font='FreeMono',
                        bg='black',
                        fg='white',
                        borderwidth=5,
                        highlightthickness=5,
                        highlightbackground="#c4a200",
                        padx = 5,
                        pady=5
                        )
    money_count_label.place(x=550,y=20)
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
    credits_count_label = Label(window,
                        text=play3r.credits,
                        font='FreeMono',
                        bg='black',
                        fg='white',
                        borderwidth=5,
                        highlightthickness=5,
                        highlightbackground="#c4a200",
                        padx = 5,
                        pady=5
                        )
    credits_count_label.place(x=390,y=20)
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

    def withdrawMoney():
        cred = play3r.credits/ 19.90   #formula for coin to dollar conversion
        money = round(cred,2)
        play3r.credits = 0
        play3r.money += money
        play3r.money = round(play3r.money,2)
        money_count_label.config(text=play3r.money)
        credits_count_label.config(text=play3r.credits)
        messagebox.showinfo('WITHDRAW',"You have withdrawed {value} dollars".format(value = money))

    def winPrize(self,self2,self3):
        count = 0
        if self.ID == 1 and self2.ID == 1 and self3.ID == 1:
            play3r.credits += 20
            messagebox.showinfo('WINNER','You have won 20 credits')
            credits_count_label.config(text=play3r.credits)
        elif ((self.ID == 1 and self2.ID == 1) or (self.ID == 1 and self3.ID == 1) or (self2.ID == 1 and self3.ID == 1)):
            play3r.credits += 10
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 10 credits')
        elif self.ID == 2 and self2.ID == 2 and self3.ID == 2:
            play3r.credits += 50
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 50 credits')
        elif ((self.ID == 2 and self2.ID == 2) or (self.ID == 2 and self3.ID == 2) or (self2.ID == 2 and self3.ID == 2)):
            play3r.credits += 25
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 25 credits')
        elif self.ID == 3 and self2.ID == 3 and self3.ID == 3:
            play3r.credits += 100
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 100 credits')
        elif ((self.ID == 3 and self2.ID == 3) or (self.ID == 3 and self3.ID == 3) or (self2.ID == 3 and self3.ID == 3)):
            play3r.credits += 50
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 50 credits')
        elif self.ID == 4 and self2.ID == 4 and self3.ID == 4:
            play3r.credits += 250
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 250 credits')
        elif ((self.ID == 4 and self2.ID == 4) or (self.ID == 4 and self3.ID == 4) or (self2.ID == 4 and self3.ID == 4)):
            play3r.credits += 100
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 100 credits')
        elif self.ID == 5 and self2.ID == 5 and self3.ID == 5:
            play3r.credits += 350
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 350 credits')
        elif ((self.ID == 5 and self2.ID == 5) or (self.ID == 5 and self3.ID == 5) or (self2.ID == 5 and self3.ID == 5)):
            play3r.credits += 150
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 150 credits')
        elif self.ID == 6 and self2.ID == 6 and self3.ID == 6:
            play3r.credits += 450
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 450 credits')
        elif ((self.ID == 6 and self2.ID == 6) or (self.ID == 6 and self3.ID == 6) or (self2.ID == 6 and self3.ID == 6)):
            play3r.credits += 200
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 200 credits')
        elif self.ID == 7 and self2.ID == 7 and self3.ID == 7:
            play3r.credits += 1000
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 1000 credits')
        elif ((self.ID == 7 and self2.ID == 7) or (self.ID == 7 and self3.ID == 7) or (self2.ID == 7 and self3.ID == 7)):
            play3r.credits += 500
            credits_count_label.config(text=play3r.credits)
            messagebox.showinfo('WINNER','You have won 500 credits')

    def openPrizes():
        prize_window = Toplevel(window)
        prize_window.geometry("400x720")
        background_label2 = Label(prize_window,image=background2_)
        background_label2.place(x=0,y=0)
        creds_label = Label(prize_window,
                            text=" 1 CREDIT = 10 MONEY",
                            font=('FreeMono',10),
                            borderwidth=5,
                            bg='red',
                            fg='white',
                            bd=5
                            )
        creds_label.place(x=75,y=125)
        prize1_label = Label(prize_window,
                            text='X3 = 1000 CREDITS\nX2 = 500 CREDITS')
        prize1_label.place(x=72,y=200)
        prize1_label_image = Label(prize_window,
                                image=final_Prize1)
        prize1_label_image.place(x=20,y=200)
        prize2_label = Label(prize_window,
                            text='X3 = 450 CREDITS\nX2 = 200 CREDITS')
        prize2_label.place(x=72,y=250)
        prize2_label_image = Label(prize_window,
                                image=final_Prize2)
        prize2_label_image.place(x=20,y=250)
        prize3_label = Label(prize_window,
                            text='X3 = 350 CREDITS\nX2 = 150 CREDITS')
        prize3_label.place(x=72,y=300)
        prize3_label_image = Label(prize_window,
                                image=final_Prize3)
        prize3_label_image.place(x=20,y=300)
        prize4_label = Label(prize_window,
                            text='X3 = 250 CREDITS\nX2 = 100 CREDITS')
        prize4_label.place(x=72,y=350)
        prize4_label_image = Label(prize_window,
                                image=final_Prize4)
        prize4_label_image.place(x=20,y=350)
        prize5_label = Label(prize_window,
                            text='X3 = 100 CREDITS\nX2 = 50 CREDITS')
        prize5_label.place(x=72,y=400)
        prize5_label_image = Label(prize_window,
                                image=final_Prize5)
        prize5_label_image.place(x=20,y=400)
        prize6_label = Label(prize_window,
                            text='X3 = 50 CREDITS\nX2 = 25 CREDITS')
        prize6_label.place(x=72,y=450)
        prize6_label_image = Label(prize_window,
                                image=final_Prize6)
        prize6_label_image.place(x=20,y=450)
        prize7_label = Label(prize_window,
                            text='X3 = 20 CREDITS\nX2 = 10 CREDITS')
        prize7_label.place(x=72,y=500)
        prize7_label_image = Label(prize_window,
                                image=final_Prize7)
        prize7_label_image.place(x=20,y=500)
        prize_window.mainloop()

    def addCredits():
        play3r.credits += 1
        credits_count_label.config(text=play3r.credits)

    def move(self,self2):
        rand = randint(1,7)
        self.ID = rand
        if self.ID == 1:
            self2.config(image=fig1.image)
        elif self.ID == 2:
            self2.config(image=fig2.image)
        elif self.ID == 3:
            self2.config(image=fig3.image)
        elif self.ID == 4:
            self2.config(image=fig4.image)
        elif self.ID == 5:
            self2.config(image=fig5.image)
        elif self.ID == 6:
            self2.config(image=fig6.image)
        elif self.ID == 7:
            self2.config(image=fig7.image)
        
    def stop():
        global flag
        if flag == False:
            play3r.credits = play3r.credits
        elif flag == False and play3r.credits == 0:
            play3r.credits = play3r.credits
        else:
            flag = False
            play3r.credits -= 1
            credits_count_label.config(text=play3r.credits)
            winPrize(fig1,fig2,fig3)

    def start():
        global flag
        flag = True
        change()
        


    def change():
        global flag
        if play3r.credits <= 0:
            flag = False
        if flag == True:
            move(fig1,label1)
            move(fig2,label2)
            move(fig3,label3)
        window.after(50,change)

    money_button = Button(window,
                        text='WITHDRAW',
                        bd=5,
                        fg='white',
                        bg='#e5a200',
                        command=withdrawMoney)
    money_button.place(x=376,y=69)

    prizes_button = Button(window,
                        text='PRIZES',
                        bd=5,
                        fg='white',
                        bg='#e5a200',
                        command=openPrizes)
    prizes_button.place(x=325,y=69)
        
    credits_button = Button(window,
                            text='ADD CREDITS',
                            bd=5,
                            fg='white',
                            bg='#e5a200',
                            command=addCredits)
    credits_button.place(x=240,y=69)


    start_button = Button(window,
                        text='PLAY',
                        bd=5,
                        fg="white",
                        bg="#e5a200",
                        command=start)
    start_button.place(x=480,y=620)

    stop_button = Button(window,
                        text='STOP',
                        bd=5,
                        fg="white",
                        bg="#e5a200",
                        command=stop)
    stop_button.place(x=600,y=620)










    window.mainloop()