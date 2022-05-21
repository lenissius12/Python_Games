from time import sleep
from os import system
from tkinter import *




#   ---------------------------     
#   |                         |
#   |                         |                  -------------
#   |   ----    ----   ----   |----------------->| PLAY      |
#   |  |  X |  |  X | |  X |  |                  -------------
#   |   ----    ----   ----   |
#   |                         |                 --------------
#   |                         |---------------->| CREDITS    |  
#   |                         |                 --------------
#   ---------------------------


tokens = 0
con1,con2,con3 = 0,0,0
strip1 = [1,1,3,1]
strip2 = [6,1,8,9,5]
strip3 = [1,1,3,4,5]

flag = False

while (flag == False):
    val1 = strip1[con1]
    val2 = strip2[con2]
    val3 = strip3[con3]
    system("cls")
    print("----------------------")
    print("| ----- ----- -----  |")
    print("| |",val1,"| |",val2,"| |",val3,"|  |")
    print("| ----- ----- -----  |")
    print("|                    |")
    print("| CREDITS ",tokens,"        |")
    print("|                    |")
    print("----------------------")

    sleep(0.5)
    if(con1 == len(strip1)-1):
        con1 = 0
        con2 = 0
        con3 = 0
    else:
        con1 += 1
        con2 += 1
        con3 += 1
