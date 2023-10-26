# =============================IMPORTS==================================
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import winsound
import time

# =============================CONSTANTS==================================

#============================ VARIABLES ============================
keyPressed = []
isKey = False
isRun = False
#============================ GLOBAL ============================
dimond = 5
money = 5
coin = 5
score=0
score_id=0

#============================ VARIABLES-JUMP ============================

GRAVITY_FORCE = 9
JUMP_FORCE = 35
SPEED = 5
TIMED_LOOP = 6


# =============================MAIN-ROOT==================================
window = tk.Tk()
window.title("JACK ADVANTURE")
frame = tk.Frame()
canvas = tk.Canvas(frame)

# =============================DISAPLAY-ROOT==================================

WINDOW_WIDTH= window.winfo_screenwidth()
WINDOW_HEIGHT=window.winfo_screenheight()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))


# =============================IMPORTS-IMAGE===============================

board_level_img=PhotoImage(file="IMAGE/level.png")
bg_img=ImageTk.PhotoImage(Image.open("IMAGE/bg_level.png"))
bg_level=ImageTk.PhotoImage(Image.open("IMAGE/level_bg.png"))
home_bg = ImageTk.PhotoImage(Image.open("IMAGE/home_bg1.png"))
start_img = ImageTk.PhotoImage(Image.open("IMAGE/start.png"))
help_img = ImageTk.PhotoImage(Image.open("IMAGE/help.png"))
exit_img = ImageTk.PhotoImage(Image.open("IMAGE/exit.png"))
back_img=ImageTk.PhotoImage(Image.open("IMAGE/back.png"))
bg_lose=ImageTk.PhotoImage(Image.open("IMAGE/bg_lose.png"))
bg_win=ImageTk.PhotoImage(Image.open("IMAGE/bg_win.png"))
dimond_img = PhotoImage(file="IMAGE/daimond.png")
coin_img = PhotoImage(file="IMAGE/coin.png")
door_img = PhotoImage(file="IMAGE/home.png")
key_img = PhotoImage(file="IMAGE/key.png")
money_img = PhotoImage(file="IMAGE/apple.png")
monster_img = PhotoImage(file="IMAGE/enermy.png")
img_level1 = Image.open("IMAGE/bg_level1.png")
img_level2 = Image.open("IMAGE/bg_level2.png")
img_level3 = Image.open("IMAGE/bg_level3.png")
bg_heart = Image.open('IMAGE/heart.png')
obj_home = Image.open('IMAGE/home.png')
apple = Image.open("IMAGE/apple.png")
objectgame = Image.open('IMAGE/object_game.png')
player_left = tk.PhotoImage(file="IMAGE/char-left.png") 
player_img = PhotoImage(file="IMAGE/char-right.png")

# =============================SIZE-OF-IMAGES==================================

heart = bg_heart.resize((40, 40))
home_size = obj_home.resize((40, 40))
objectgame_size = objectgame.resize((200, 40))
apple_size = apple.resize((35, 35))

heart0flife = ImageTk.PhotoImage(heart)
imglevel1 = ImageTk.PhotoImage(img_level1)
imglevel2 = ImageTk.PhotoImage(img_level2)
imglevel3 = ImageTk.PhotoImage(img_level3)
img_home = ImageTk.PhotoImage(home_size)
img_apple = ImageTk.PhotoImage(apple_size)
objectofgame = ImageTk.PhotoImage(objectgame_size)


# =============================HOME-PAGES==================================
def home():
    canvas.create_image(0, 0, image=home_bg, anchor="nw")
    canvas.create_image(650, 400, image=start_img, anchor="nw", tags="start")
    canvas.create_image(645, 475, image=help_img, anchor="nw", tags="help")
    canvas.create_image(665, 560, image=exit_img, anchor="nw", tags="exit")
    
    # winsound.PlaySound("sound/home.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
home()

# =============================CONSTANTS==================================

def start(event):
    canvas.create_image(0, 0, image=bg_level, anchor="nw")
                            #========== LEVEL-1 ==========
    canvas.create_image(650, 400, image=board_level_img, anchor="nw", tags="level1")
    canvas.create_text(760, 435, text="Level 1", font=("airal", 25, "bold"), fill="#FFFFFF",tags="level1")
                            #========== LEVEL-2 ==========
    canvas.create_image(650, 500, image=board_level_img, anchor="nw", tags="level2")
    canvas.create_text(760, 535, text="Level 2", font=("airal", 25, "bold"), fill="#FFFFFF",tags="level2")
                            #========== LEVEL-3 ==========
    canvas.create_image(650, 600, image=board_level_img, anchor="nw", tags="level3")
    canvas.create_text(760, 635, text="Level 3", font=("airal", 25, "bold"), fill="#FFFFFF",tags="level3")
                            #========== BACK-HOME ==========
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")

# =============================HELP==================================
def help(event):
    canvas.create_image(0,0 , image=bg_img, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
    # winsound.PlaySound("sound/home.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )

# =============================EXIT==================================
def exit(event):
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    window.destroy()

# =============================BACK-HOME==================================
def backHome(event):
    # winsound.PlaySound("sound/home.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    home()




# =============================FUNCTION-OF-LEVEL-ONE===========================================

def level1(event):
    global player, keyPressed, score_id
    score = 0
    canvas.delete("all")
    #========== BG-LEVEL1-IMG==========
    canvas.create_image(400, 400, image=imglevel1) 
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
    #========== OBJECT-GAME==========
    canvas.create_image(360, 580, image=objectofgame, tags="platform")
    canvas.create_image(50, 630, image=objectofgame, tags="platform")
    canvas.create_image(760, 580, image=objectofgame, tags="platform")
    canvas.create_image(900, 470, image=objectofgame, tags="platform")
    canvas.create_image(1080, 550, image=objectofgame, tags="platform")
    canvas.create_image(1200, 360, image=objectofgame, tags="platform")
    canvas.create_image(300, 360, image=objectofgame, tags="platform")
    #========== HEART ==========
    canvas.create_image(1160, 50, image=heart0flife)
    canvas.create_image(1195, 50, image=heart0flife)
    canvas.create_image(1230, 50, image=heart0flife)
    #========== PLAYER ==========
    player = canvas.create_image(100, 150, image=player_img)   
    #========== APPLE-IMG==========    
    canvas.create_image(300, 545, image=img_apple, tags='coin')
    canvas.create_image(700, 545, image=img_apple, tags='coin')
    canvas.create_image(800, 545, image=img_apple, tags='coin')
    canvas.create_image(1100, 515, image=img_apple, tags='coin')
    canvas.create_image(1020, 515, image=img_apple, tags='coin')
    #========== DOOR$KEY-IMG==========
    canvas.create_image(1265, 315, image = door_img, anchor = "nw", tags = "door")
    canvas.create_image(900,250, image = key_img, anchor = "nw", tags = "key")
    #========== MONEY-IMG ==========
    canvas.create_image(350, 345, image = money_img, anchor = 'nw', tags = "money")
    canvas.create_image(240,280, image = money_img, anchor = 'nw', tags = "money")
    canvas.create_image(730,600, image = money_img, anchor = "nw", tags = "money")
    canvas.create_image(730,600, image = money_img, anchor = "nw", tags = "money")
    canvas.create_image(430,600, image = money_img, anchor = "nw", tags = "money")
    
    #========== DAIMOND-IMG ==========
    canvas.create_image(400,420, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(400,420, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1130,100, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1130,100, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1100,100, image = dimond_img, anchor = 'nw', tags = "dimond")

     #==========  COIN IMAGES ==========
    canvas.create_image(550,300, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1100,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1170,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(680,470, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(380,470, image = coin_img, anchor = 'nw', tags = "coin")

     #==========  MONSTER IMAGES ==========
    canvas.create_image(300,400, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(200,100, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(550, 446, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1000,100, image =monster_img, anchor = 'nw', tags = "monster")
    x = 0
    for i in range(50):
        canvas.create_image(x,700, image =monster_img, anchor = 'nw', tags = "monster")
        x += monster_img.width()
    #  #==========  SHOW-LEVEL$SCORE ==========
    canvas.create_text(700,50,text='Levels: 1',font=('Arial',18,'bold'),fill='white') 
    score_id = canvas.create_text(190,50, text=" score : " + str(score), font=("Arial", 20, "bold"), fill="white")
    window.after(TIMED_LOOP, gravity)  