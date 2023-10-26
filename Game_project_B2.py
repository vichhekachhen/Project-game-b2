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

# =============================LEVEL-TWO==================================

def level2(event):
    global player, keyPressed, score_id
    score = 0
    canvas.delete("all")
    #========== BG-LEVEL1-IMG==========
    canvas.create_image(400, 400, image=imglevel2) 
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home") 
    #========== OBJECT-GAME==========
    canvas.create_image(80, 600, image=objectofgame, tags="platform")
    canvas.create_image(500, 600, image=objectofgame, tags="platform")
    canvas.create_image(790, 470, image=objectofgame, tags="platform")
    canvas.create_image(500, 300, image=objectofgame, tags="platform")
    canvas.create_image(850, 200, image=objectofgame, tags="platform")
    canvas.create_image(1180, 200, image=objectofgame, tags="platform")
    #========== HEART ==========
    canvas.create_image(1160, 50, image=heart0flife)
    canvas.create_image(1195, 50, image=heart0flife)
    canvas.create_image(1230, 50, image=heart0flife)
    #========== PLAYER ==========   
    player = canvas.create_image(100, 150, image=player_img)   
    #========== APPLE-IMG==========    
    canvas.create_image(310, 465, image=img_apple, tags='coin')
    canvas.create_image(530, 500, image=img_apple, tags='coin')
    canvas.create_image(570, 500, image=img_apple, tags='coin')
    canvas.create_image(800, 390, image=img_apple, tags='coin')
    canvas.create_image(850, 390, image=img_apple, tags='coin')
    canvas.create_image(800, 120, image=img_apple, tags='coin')
    canvas.create_image(500, 220, image=img_apple, tags='coin')
    #========== DOOR$KEY-IMG==========
    canvas.create_image(1190,100, image = door_img, anchor = "nw", tags = "door")
    canvas.create_image(660,110, image = key_img, anchor = "nw", tags = "key")
    canvas.create_image(300, 545, image = money_img, anchor = 'nw', tags = "money")
    canvas.create_image(330,450, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1150,155, image =monster_img, anchor = 'nw', tags = "monster")
    #========== MONEY-IMG ==========
    canvas.create_image(240,280, image = money_img, anchor = 'nw', tags = "money")
    canvas.create_image(730,600, image = money_img, anchor = "nw", tags = "money")
    
    #========== DAIMOND-IMG ==========
    canvas.create_image(400,200, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1000,50, image = dimond_img, anchor = 'nw', tags = "dimond")

     #==========  COIN IMAGES ==========
    canvas.create_image(440,210, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1050,55, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(700,385, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(410,550, image = coin_img, anchor = 'nw', tags = "coin")

     #==========  MONSTER IMAGES ==========
    canvas.create_image(740,425, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(450,555, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(860,155, image =monster_img, anchor = 'nw', tags = "monster")
    x = 0
    for i in range(50):
        canvas.create_image(x,680, image =monster_img, anchor = 'nw', tags = "monster")
        x += monster_img.width()
     #==========  SHOW-LEVEL$SCORE ==========
    canvas.create_text(700,50,text='Levels: 2',font=('Arial',18,'bold'),fill='white') 
    score_id = canvas.create_text(190,50, text=" score : " + str(score), font=("Arial", 20, "bold"), fill="white")

    window.after(TIMED_LOOP, gravity)

# =============================LEVEL-THREE==================================


def level3(event):
    global player, keyPressed, score_id
    score = 0
    canvas.delete("all")
    #========== BG-LEVEL1-IMG==========
    canvas.create_image(400, 400, image=imglevel3) 
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
    #========== OBJECT-GAME==========
    canvas.create_image(370, 510, image=objectofgame, tags="platform")
    canvas.create_image(80, 650, image=objectofgame, tags="platform")
    canvas.create_image(810, 680, image=objectofgame, tags="platform")
    canvas.create_image(770, 370, image=objectofgame, tags="platform")
    canvas.create_image(1130, 550, image=objectofgame, tags="platform")
    canvas.create_image(1260, 295, image=objectofgame, tags="platform")
    #========== HEART ==========
    canvas.create_image(1160, 50, image=heart0flife)
    canvas.create_image(1195, 50, image=heart0flife)
    canvas.create_image(1230, 50, image=heart0flife)
    #========== PLAYER ==========
    player = canvas.create_image(100, 150, image=player_img)   
    #========== APPLE-IMG==========    
    canvas.create_image(300, 435, image=img_apple, tags='coin')
    canvas.create_image(350, 435, image=img_apple, tags='coin')
    canvas.create_image(790, 610, image=img_apple, tags='coin')
    canvas.create_image(840, 610, image=img_apple, tags='coin')
    canvas.create_image(810, 285, image=img_apple, tags='coin')
    canvas.create_image(840, 285, image=img_apple, tags='coin')
    canvas.create_image(1055, 470, image=img_apple, tags='coin')
    canvas.create_image(1090, 470, image=img_apple, tags='coin')
    #========== DOOR$KEY-IMG==========
    canvas.create_image(1265,200, image = door_img, anchor = "nw", tags = "door")
    canvas.create_image(1150,210, image = key_img, anchor = "nw", tags = "key")
    canvas.create_image(300, 545, image = money_img, anchor = 'nw', tags = "money")
    #========== MONEY-IMG ==========
    canvas.create_image(240,280, image = money_img, anchor = 'nw', tags = "money")
    canvas.create_image(730,600, image = money_img, anchor = "nw", tags = "money")
    
    #========== DAIMOND-IMG ==========
    canvas.create_image(380,420, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(420,420, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1200,200, image = dimond_img, anchor = 'nw', tags = "dimond")

     #==========  COIN IMAGES ==========
    canvas.create_image(680,280, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(715,280, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1110,460, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1140,460, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(870,600, image = coin_img, anchor = 'nw', tags = "coin")

     #==========  MONSTER IMAGES ==========
    canvas.create_image(760,275, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1250,210, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1185,455, image =monster_img, anchor = 'nw', tags = "monster")
    x = 0
    for i in range(50):
        canvas.create_image(x,700, image =monster_img, anchor = 'nw', tags = "monster")
        x += monster_img.width()
     #==========  SHOW-LEVEL$SCORE ==========
    canvas.create_text(700,50,text='Levels: 2',font=('Arial',18,'bold'),fill='white') 
    score_id = canvas.create_text(190,50, text=" score : " + str(score), font=("Arial", 20, "bold"), fill="white")
    window.after(TIMED_LOOP, gravity)

    
#=========================== LOSE AND WIN =======================
def lose():
    canvas.delete("all")
    # Lose_Sound()
    canvas.create_image(1,0, image = bg_lose ,anchor = "nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
    canvas.create_text(680, 474,  text="Your score is : " + str(score), font=("Arial", 30, "bold"), fill="red") 
    canvas.itemconfig(score_id, updatescore)
    


def win():
    if isKey and score > 24:
        canvas.delete("all")
        # Win_Sound()
        canvas.create_image(1,0, image = bg_win, anchor = "nw")
        canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
        canvas.create_text(700, 154,  text="Your score is : " + str(score), font=("Arial", 30, "bold"), fill="black") 
        canvas.itemconfig(score_id, updatescore)

       
#=========================== FUNCTIONS MOVE PLAYER =======================
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("platform")
    if coord[0] + dx < 0 or coord[1] + dx > WINDOW_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1] - 50) + player_img.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+ player_img.width() + dx, (coord[1] - 50) + player_img.height())
    for platform in platforms:
        if platform in overlap:
            return False
    return True
def check_movement_monster():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("monster")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_coin():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("coin")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_money():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("money")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_dimond():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("dimond")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_key():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("key")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_door():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("door")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_monster():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("monster")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

#================= JUMP-MOVEMENT===============
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)

#========================= START-MOVE =======================
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

#========================= MOVE-PLAYER =======================
def move():
    
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            canvas.itemconfig(player, image = player_left)
            x -= SPEED
        if "Right" in keyPressed:
            canvas.itemconfig(player, image = player_img)
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player, x, 0)
            window.after(TIMED_LOOP, move)
    movement()

#======================= CHECK-MOVE ======================
def movement():
    global score, coin , money, dimond, isKey, isRun
    monster_id = check_movement_monster()
    coin_id = check_movement_coin()
    money_id = check_movement_money()
    dimond_id = check_movement_dimond()
    key_id = check_movement_key()
    door_id = check_movement_door()
    if isRun:
        score = 0
        isRun = False
    if monster_id > 0:
        isRun = True
        lose()
    if key_id > 0:
        isKey = True
        # Eat_Sound()
        canvas.delete(key_id)
    if money_id > 0:
        score += money
        # Eat_Sound()
        canvas.delete(money_id)
        updatescore()
    if coin_id > 0:
        score += coin
        # Eat_Sound()
        canvas.delete(coin_id)
        updatescore()
    if dimond_id > 0:
        score += dimond
        # Eat_Sound()
        canvas.delete(dimond_id)
        updatescore()
    if door_id > 0:
        win()

#============================ CHECK_PLAYER_MOVE ============================
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

#======================== STOP_MOVE AND REMOVE KEY =====================
def stop_move(event):
    global keyPressedgi
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

#============================ RESULT SCORE ============================
def updatescore():
    canvas.itemconfig(score_id,text="Score: " + str(score) )
#============================ KEY EVENT ===============================
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

# =============================REMOTES==================================
canvas.tag_bind("start","<Button-1>",start)
canvas.tag_bind("help","<Button-1>",help)
canvas.tag_bind("exit","<Button-1>",exit)
canvas.tag_bind("level1","<Button-1>",level1)
canvas.tag_bind("level2","<Button-1>",level2)
canvas.tag_bind("level3","<Button-1>",level3)
canvas.tag_bind("back_home","<Button-1>",backHome)
home()

# =============================DISAPLAY-ROOT==================================

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()