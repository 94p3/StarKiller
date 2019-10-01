from graph import *
from random import *


windowSize(1200, 700)
canvasSize(1200, 700)


# ФОН
brushColor(50, 50, 100)
bg=rectangle(0, 0, 1200, 700)



# РАКЕТА
brushColor(100,100,100)
telo = circle(100, 350, 80)
penSize(30)
penColor(30,30,30)
strip = line(20,350,180,350)
penColor(0,0,0)
penSize(5)
brushColor(200,0,0)
gun = circle(150,350,20)
penSize(1)

# ПОЯВЛЕИЕ ЗВЁЗД
starAmount = 20
count = 0
count1=0

starMas = [line(0,0,0,0)]*starAmount

def starLaunch():
    global count1, count2, count
    ran = random()
    if count1>60:
        loses()
    if (count2 > 45) and (count1 <= 60):
        win()

    brushColor(100 + int(100 * ran), 100 + int(100 * ran), 60)

    a = 0.9 * ran + 0.1
    y = 700 * random()
    #deleteObject(starMas[count % starAmount])

    starMas[count % starAmount] = polygon([(1200 + 50 * a, y + 0 * a), (1200 + 60 * a, y + 40 * a), (1200 + 100 * a, y + 50 * a), (1200 + 60 * a, y + 60 * a), (1200 + 50 * a, y + 100 * a), (1200 + 40 * a, y + 60 * a), (1200 + 0 * a, y + 50 * a), (1200 + 40 * a, y + 40 * a)])
    count += 1
    if count2<=45:
        count1 +=0.5

def win():
    global bg
    penColor('purple')
    brushColor('purple')
    changeFillColor(bg,'purple')
    changePenColor(bg, 'purple')
    changeFillColor(telo,'purple')
    changePenColor(telo, 'purple')
    changeFillColor(strip, 'purple')
    changeFillColor(gun, 'purple')
    changePenColor(gun, 'purple')
    penColor('white')
    brushColor('white')
    label('you have destroyed the galaxy',90,310,bg='purple',font="Arial 54")
    label('sooo klubnichna', 340, 390, bg='purple', font="Arial 54")

def loses():
    global bg
    penColor('black')
    brushColor('black')
    changeFillColor(bg, 'black')
    changePenColor(bg, 'black')
    changeFillColor(telo, 'black')
    changePenColor(telo, 'black')
    changeFillColor(strip, 'black')
    changeFillColor(gun, 'black')
    changePenColor(gun, 'black')
    penColor('white')
    brushColor('white')
    label('you lost', 360, 310, bg='black', font="Arial 54",fg='white')
    label('disgusting', 340, 390, bg='black', font="Arial 54",fg='white')

onTimer(starLaunch, 500 )


# ДВИЖЕНИЕ
def starPush():
    for i in range(starAmount):
        moveObjectBy(starMas[i], -2-count2 // 4, 0)

onTimer(starPush, 10)

# КОНТРОЛЬ
count2 = 0
def control(event):
    global shot, count2
    # ДВИЖЕНИЕ РАКЕТЫ
    if event.keycode == VK_UP:
        moveObjectBy(telo, 0, -14)
        moveObjectBy(strip, 0, -14)
        moveObjectBy(gun, 0, -14)
    if event.keycode == VK_DOWN:
        moveObjectBy(telo, 0, 14)
        moveObjectBy(strip, 0, 14)
        moveObjectBy(gun, 0, 14)
    # СТРЕЛЬБА
    if event.keycode == VK_SPACE:
        penSize(30)
        penColor(220,0,0)
        shot = line(150,yCoord(gun)+22,1200,yCoord(gun)+22)
        penColor(0, 0, 0)
        penSize(1)
        for i in range(starAmount):
            if yCoord(gun)+15 > coords(starMas[i])[1] and yCoord(gun)+15 < coords(starMas[i])[3] :
                deleteObject(starMas[i])
                starMas[i] = line(0,0,0,0)
                count2 +=1


onKey(control)
shot = line(0,0,0,0)


# ЗАДЕРЖКА УДАЛЕНИЯ
def zaderahka():
    global shot
    deleteObject(shot)

onTimer(zaderahka,120)

def lose():
    print()
run()
