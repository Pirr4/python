x = 250
y = 250
vx = 450
vy = 450 
s = 0
d = 0
r = True
active = False
game = False
x1 = 0
y1 = 0
g = 'Game by Pirr4'
slo = False
vsx = 0.5
vsy = 0.5
pers = False
mp = [[1,0,0,0,0,1,0,0,0,0],
      [0,0,0,0,0,0,0,1,0,1],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,1,0,1,0,0,0],
      [0,0,0,0,0,0,1,0,0,0],
      [0,1,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,1,0,1,0,0,1,0,0],
      [0,1,0,0,0,0,0,0,0,0],
      [0,1,1,0,0,1,0,0,0,0],
      ]
def setup () :
    global ply,vrg,yab
    ply = loadImage(u'сердце-removebg-preview.png')
    vrg = loadImage(u'череп-removebg-preview.png')
    yab = loadImage(u'яблоко-removebg-preview.png')
    size (500,500)
    textSize(50)
    imageMode(CENTER)
    frameRate(60)
def draw () :
    background(255)
    global x,y,active,ax,ay,x1,y1,r,d,vx,vy,game,slo,vsx,vsy
    if game:
#Карта
        for q in range(len(mp)):
            for w in range(len(mp[q])):
                if mp[q][w] == 1 :
                    fill(255)
                    circle(q*50+25,w*50+25,50)
#Спавн яблочек
        if r == True :
            x1=random(5,495)
            y1=random(5,495)
            active = True
            r = False
        if active:
           image(yab,x1,y1,25,25)
# Сбор яблочек
        ax=x-x1
        ay=y-y1
        if sqrt(ax*ax+ay*ay) <= 25 :
            d+=1
            active = False
            r=True
      
# Клетка
        image(vrg,vx,vy,40,40)
        if vy > y :
            vy = vy - (vsy + d/10*0.2)
        if vy < y :
            vy = vy + (vsy+ d/10*0.2)
        if vx > x :
            vx = vx - (vsx+ d/10*0.2)
        if vx < x :
            vx = vx + (vsx+ d/10*0.2)
            
        print(vsy + d/10*0.2 , vsx + d/10*0.2)
        sx=x-vx
        sy=y-vy
        p1 = sqrt(sx*sx+sy*sy)
        if p1 <= 32.5 :
            game = False 
# Стены
        if y == 500 :
            y = y - 10
        if y == 0 :
            y = y + 10
        if x == 500 :
            x = x - 10
        if x == 0 :
            x = x + 10
# Персонаж
        image(ply,x,y,25 ,25)
#Баллы
        fill(0)
        text(d,20,60)
#Меню
    else :
        background(0,255,0)
        fill(0)
        text('Game by Pirr4',20,60)
        text('Press R to restart',20,110)
        text('Your score:' + str(d),20,170)
# Управление    
def keyPressed () :
    global x,y,x1,y1,game,x,y,vx,vy,d
    if key == 'r' or key == 'R' :
        x = 250
        y = 250
        vx = 450
        vy = 450
        d = 0 
        game = True
    if keyCode == UP :
        y=y-10
    if keyCode == RIGHT :
        x=x+10
    if keyCode == LEFT :
        x=x-10
    if keyCode == DOWN :
        y=y+10
