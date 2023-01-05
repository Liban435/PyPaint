#Liban Guled 
#Paint Project 
from pygame import *
from random import *
from math import *
from glob import *
import pygame 
screen = display.set_mode((1024,768)) #When importing pic only use this size 
#wpPic = image.load("wp.jpg") #This code and the one below is pic code 
colourPic = image.load("colour.jpg") 
pencilPic = image.load("Pencil.png") 
eraserPic = image.load("Eraser.png")
brushPic = image.load("Brush.png") 
bombPic = image.load("Bomb.png") 
fillPic = image.load("fill.png") 
spraycanPic = image.load("spraycan.png")
linePic = image.load("line.png")
#ellipsePic = image.load("ellipse.png")
#fellipsePic = image.load("fellipse.jpg")
#RectToolPic = image.load("RectTool.png")
#FRectToolPic = image.load("FRectTool.png")

  
#screen.blit(wpPic,(0,0)) 
colourRect = screen.blit(colourPic,(10,580))


stampRect = Rect(320,580,700,150)
draw.rect(screen,(255,255,255),stampRect)
allen=image.load("allen.jpg")
screen.blit(allen,(320,580))
drose=image.load("drose.jpg")
screen.blit(drose,(420,580))
kevind=image.load("kevind.jpg")
screen.blit(kevind,(520,580))
kobe=image.load("kobe.png")
screen.blit(kobe,(620,580))
#court1=image.load("court1.jpg")
#screen.blit(court1,(700,580))
#court2=image.load("court2.jpg")
#screen.blit(court2,(800,580))
#court3=image.load("court3.jpg")
#screen.blit(court3,(900,580))
allen = transform.smoothscale(allen,(100,260))
drose = transform.smoothscale(drose,(100,260))
kevind = transform.smoothscale(kevind,(100,260))
kobe = transform.smoothscale(kobe,(100,260))


screen.set_clip(stampRect)
for i in range(320,1020,100):
    for q in range(580,1020,100):
        z=i+100
        draw.line(screen,(0,0,0),(z,580),(z,q))
screen.set_clip(None)

  
      
pencilRect = Rect(20,80,40,40) #Draws the s squars that have the painting 
eraserRect = Rect(20,135,40,40) #functions 
brushRect = Rect(20,190,40,40) 
clearRect = Rect(20,245,40,40) 
fillRect = Rect(20,300,40,40) 
sprayRect = Rect(20,355,40,40)
lineRect = Rect(75,80,40,40)
elipseRect = Rect(75,135,40,40)
FellipseRect = Rect(75,190,40,40)
RectTool = Rect(75,245,40,40)
FRectTool = Rect(75,300,40,40)
InputtextRect = Rect(75,355,40,40)
undoRect = Rect(130,80,40,40)
redoRect = Rect(130,135,40,40)
saveRect = Rect(130,190,40,40)
loadRect = Rect(130,245,40,40)
allenRect = Rect(320,580,100,260)
droseRect = Rect(420,580,100,260)
kevindRect = Rect(520,580,100,260)
kobeRect = Rect(620,580,100,260)




  
draw.rect(screen,(0,255,0),pencilRect) #Makes the paint functions square 
draw.rect(screen,(0,255,0),eraserRect) #White 
draw.rect(screen,(0,255,0),brushRect) 
draw.rect(screen,(0,255,0),clearRect) 
draw.rect(screen,(0,255,0),fillRect) 
draw.rect(screen,(0,255,0),sprayRect)
draw.rect(screen,(0,255,0),lineRect)
draw.rect(screen,(0,255,0),elipseRect)
draw.rect(screen,(0,255,0),FellipseRect)
draw.rect(screen,(0,255,0),RectTool)
draw.rect(screen,(0,255,0),FRectTool)
draw.rect(screen,(0,255,0),InputtextRect)
draw.rect(screen,(0,255,0),undoRect)
draw.rect(screen,(0,255,0),redoRect)
draw.rect(screen,(0,255,0),saveRect)
draw.rect(screen,(0,255,0),loadRect)



screen.blit(pencilPic,(20,80)) 
screen.blit(eraserPic,(20,135)) 
screen.blit(brushPic,(20,190)) 
screen.blit(bombPic,(20,245)) 
screen.blit(fillPic,(20,300)) 
screen.blit(spraycanPic,(20,355))
screen.blit(linePic,(75,80))
#screen.blit(ellipsePic,(75,135))
#screen.blit(fellipsePic,(75,190))
#screen.blit(RectToolPic,(75,245))
#screen.blit(FRectToolPic,(75,300))
            

  
canvasRect = Rect(320,20,700,550) 
draw.rect(screen,(255,255,255),canvasRect) #Draws the canvas 
#image.save(screen,subssurface(canvas),"saves/"+picturename) 
tool="pencil"
mx,my=0,0
drawColour = (0,0,0) 
c=(randint(0,255), randint(0,255),randint(0,255)) 
start = 0,0
sz=10
sz2=10
undo=[]
redo=[]
firstScreen=screen.subsurface(canvasRect).copy()
undo.append(firstScreen)
  
def Fill(mx,my,clickedcol,chosencol):   # mx,my point where you click 
    listfill = [(mx,my)]
    if clickedcol==chosencol:return #if where you clicked equals color set, then stop
    while len(listfill)>0: 
        x,y = listfill.pop() #gets the last values of the list 
        if screen.get_at((x,y))==clickedcol: #if the color where you cllicked on is the same as your old color 
            screen.set_at((x,y),chosencol) #set the color of the points to the chosen color
            listfill+=[(x+1,y), (x-1,y),(x,y+1),(x,y-1)]#gets all the around the clicked pixel untill it reaches a different color

def getName():
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(mx,my,200,25) # make changes here.
    textArea = Rect(30,490,200,20)
    pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
    n = len(pics)
    choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
    draw.rect(screen,(220,220,220),choiceArea)        # draw the text window and the text.
    draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
    for i in range(n):
        txtPic = arialFont.render(pics[i], True, (0,111,0))   #
        screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))

    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = arialFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            #
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans

font.init()
myfont = font.SysFont("Comic Sans MS", 20)
textRect = Rect(10,410,260,160)
draw.rect(screen,(226,199,141),textRect)
  
  
running = True
while running: 
    for e in event.get(): 
        if e.type == QUIT: 
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mouse.set_visible(True)  
            if e.button == 1:
                ex,ey = mouse.get_pos()
                startx,starty = e.pos
                copy = screen.copy() 
                start = e.pos 
        if e.type == MOUSEBUTTONUP: 
            mouse.set_visible(True) 
        if e.type == MOUSEBUTTONDOWN: 
            if e.button == 1:
                start = e.pos 
            if e.button == 4: 
                sz += 3
                sz2 += 1
            if e.button == 5: 
                sz = max(sz-3,1)
                sz2 = max(sz2-1,0)


            if e.button == 1 or e.button == 3  : #undo and redo statements                
                u_r = screen.subsurface(canvasRect).copy() #take a copy of canvasRect everytime user left clicks
                back = screen.copy()
            if e.button == 1:
                if undoRect.collidepoint(mx,my) and len(undo) > 1: #if the length of undo list if more 1, get last value
                    redo.append(undo[-1]) #adds to undo list
                    undo = undo[:-1]
                    screen.blit(undo[-1],(canvasRect)) # draws last value to screen from undo list
                if redoRect.collidepoint(mx,my) and len(redo) > 0: # if length of redo list is more than 0, get last value
                    undo.append(redo[-1]) #adds to redo list
                    redo = redo[:-1]
                    screen.blit(undo[-1],(canvasRect))
                if canvasRect.collidepoint(startx,starty) and tool == "redo":
                    redo = []


                        
        if e.type == MOUSEBUTTONUP: #copies screen when mouse button is no longer held down then adds the picture to the undo list
##            width2= mx-selectx
##            height2= my-selecty
            end = True
            if canvasRect.collidepoint(mx,my) and e.button == 1 : 
                undo.append(screen.subsurface(canvasRect).copy())
    keys = key.get_pressed()



#r=Rect(100,50,-20,10)
#r.normalize()
#elipse tool
  
    mb = mouse.get_pressed()
    omx,omy = mx,my
    mx,my = mouse.get_pos()



    h = randint(mx-20,mx+20)
    k = randint(my-20,my+20)
      
      
    draw.rect(screen,(0,255,0),pencilRect,1) #Makes the paint functions square 
    draw.rect(screen,(0,255,0),eraserRect,1) #White 
    draw.rect(screen,(0,255,0),brushRect,1) 
    draw.rect(screen,(0,255,0),clearRect,1) 
    draw.rect(screen,(0,255,0),fillRect,1) 
    draw.rect(screen,(0,255,0),sprayRect,1)
    draw.rect(screen,(0,255,0),lineRect,1)
    draw.rect(screen,(0,255,0),elipseRect,1)
    draw.rect(screen,(0,255,0),FellipseRect,1)
    draw.rect(screen,(0,255,0),RectTool,1)
    draw.rect(screen,(0,255,0),FRectTool,1)
    draw.rect(screen,(0,255,0),textRect,1)
    draw.rect(screen,(0,255,0),undoRect,1)
    draw.rect(screen,(0,255,0),redoRect,1)
    draw.rect(screen,(0,255,0),saveRect,1)
    draw.rect(screen,(0,255,0),loadRect,1)

    if keys[K_l]:
        screen.set_clip(text)
        txt = getName(True)
        image.save(screen.subsurface(page),txt) 
    if keys[K_s]:
        img=image.load(txt)
        screen.blit(img,(mx,my))
      
    if mb[0]==1 and colourRect.collidepoint(mx,my):#Allows you to select the pencil function 
        drawColour = screen.get_at((mx,my)) 
        draw.rect(screen,drawColour,(280,540,30,30)) 
  
              
    if pencilRect.collidepoint(mx,my):#Allows you to select the pencil function 
        draw.rect(screen,(255,0,0),pencilRect,1) 
        if mb[0]==1:
            tool="pencil"
            draw.rect(screen,(226,199,141),textRect)
            pt1 = myfont.render(("Pencil Tool"),1,(0,0,0))
            pt2 = myfont.render(("This draws a basic line in"),1,(0,0,0))
            pt3 = myfont.render(("which you can draw"),1,(0,0,0))
            pt4 = myfont.render(("whatever you want."),1,(0,0,0))
            screen.blit(pt1,(15,415))
            screen.blit(pt2,(15,440))
            screen.blit(pt3,(15,465))
            screen.blit(pt4,(15,490))
            

  
    if eraserRect.collidepoint(mx,my):#Allows you to select the eraser function 
        draw.rect(screen,(255,0,0),eraserRect,1)
        if mb[0]==1:
            tool="eraser"
            draw.rect(screen,(226,199,141),textRect)
            et1 = myfont.render(("Eraser Tool"),1,(0,0,0))
            et2 = myfont.render(("This uses a cirles to"),1,(0,0,0))
            et3 = myfont.render(("erase any mistake you "),1,(0,0,0))
            et4 = myfont.render(("made."),1,(0,0,0))
            screen.blit(et1,(15,415))
            screen.blit(et2,(15,440))
            screen.blit(et3,(15,465))
            screen.blit(et4,(15,490))
        
  
    if brushRect.collidepoint(mx,my):#Allows you to select the brush function 
        draw.rect(screen,(255,0,0),brushRect,1)
        if mb[0]==1:
            tool="brush"
            draw.rect(screen,(226,199,141),textRect)
            bt1 = myfont.render(("Brush Tool"),1,(0,0,0))
            bt2 = myfont.render(("Uses a series of cirlces to"),1,(0,0,0))
            bt3 = myfont.render(("draw a smooth brush. Use"),1,(0,0,0))
            bt4 = myfont.render(("the scroll to"),1,(0,0,0))
            bt5 = myfont.render(("change brush size."),1,(0,0,0))
            screen.blit(bt1,(15,415))
            screen.blit(bt2,(15,440))
            screen.blit(bt3,(15,465))
            screen.blit(bt4,(15,490))
            screen.blit(bt5,(15,515))
                            
                            
        
  
    if clearRect.collidepoint(mx,my):#Allows you to select the clear function 
        draw.rect(screen,(255,0,0),clearRect,1)
        if mb[0]==1:
            tool="clear"
            draw.rect(screen,(226,199,141),textRect)
            ct1 = myfont.render(("Clear Tool"),1,(0,0,0))
            ct2 = myfont.render(("WARNING:"),1,(0,0,0))
            ct3 = myfont.render(("IT COMPLETLY"),1,(0,0,0))
            ct4 = myfont.render(("erases everything on"),1,(0,0,0))
            ct5 = myfont.render(("your screen."),1,(0,0,0))
            screen.blit(ct1,(15,415))
            screen.blit(ct2,(15,440))
            screen.blit(ct3,(15,465))
            screen.blit(ct4,(15,490))
            screen.blit(ct5,(15,515))
        
  
    if fillRect.collidepoint(mx,my):#Allows you to select the fill function 
        draw.rect(screen,(255,0,0),fillRect,1) 
        if mb[0]==1:
            tool="fill"
            draw.rect(screen,(226,199,141),textRect)
            ft1 = myfont.render(("Fill Tool"),1,(0,0,0))
            ft2 = myfont.render(("Completly fills the whole"),1,(0,0,0))
            ft3 = myfont.render(("screen with a colour"),1,(0,0,0))
            ft4 = myfont.render(("of your choice."),1,(0,0,0))
            screen.blit(ft1,(15,415))
            screen.blit(ft2,(15,440))
            screen.blit(ft3,(15,465))
            screen.blit(ft4,(15,490))        
  
    if sprayRect.collidepoint(mx,my):#Allows you to select the spray function 
        draw.rect(screen,(255,0,0),sprayRect,1) 
        if mb[0]==1:
            tool="spray"
            draw.rect(screen,(226,199,141),textRect)
            st1 = myfont.render(("Spray Tool"),1,(0,0,0))
            st2 = myfont.render(("Makes a bunch of little"),1,(0,0,0))
            st3 = myfont.render(("circles that create"),1,(0,0,0))
            st4 = myfont.render(("a spray."),1,(0,0,0))
            screen.blit(st1,(15,415))
            screen.blit(st2,(15,440))
            screen.blit(st3,(15,465))
            screen.blit(st4,(15,490))

            
    if lineRect.collidepoint(mx,my):#Allows you to select the line function 
        draw.rect(screen,(255,0,0),lineRect,1)
        if mb[0]==1:
            tool="line"
            draw.rect(screen,(226,199,141),textRect)
            lt1 = myfont.render(("Line Tool"),1,(0,0,0))
            lt2 = myfont.render(("Makes a straight line"),1,(0,0,0))
            lt3 = myfont.render(("that can have the"),1,(0,0,0))
            lt4 = myfont.render(("size changed by using"),1,(0,0,0))
            lt5 = myfont.render(("the scroll."),1,(0,0,0))
            screen.blit(lt1,(15,415))
            screen.blit(lt2,(15,440))
            screen.blit(lt3,(15,465))
            screen.blit(lt4,(15,490))
            screen.blit(lt5,(15,515))

    if elipseRect.collidepoint(mx,my):#Allows you to select the elipse function 
        draw.rect(screen,(255,0,0),elipseRect,1) 
        if mb[0]==1:
            tool="elipse"
            draw.rect(screen,(226,199,141),textRect)
            elt1 = myfont.render(("Elipse Tool"),1,(0,0,0))
            elt2 = myfont.render(("Draws a circle"),1,(0,0,0))
            elt3 = myfont.render(("that you can change"),1,(0,0,0))
            elt4 = myfont.render(("the size."),1,(0,0,0))
            screen.blit(elt1,(15,415))
            screen.blit(elt2,(15,440))
            screen.blit(elt3,(15,465))
            screen.blit(elt4,(15,490))

    if FellipseRect.collidepoint(mx,my):#Allows you to select the elipse function 
        draw.rect(screen,(255,0,0),FellipseRect,1) 
        if mb[0]==1:
            tool="Fellipse"
            draw.rect(screen,(226,199,141),textRect)
            elt1 = myfont.render(("Elipse Tool(Filled)"),1,(0,0,0))
            elt2 = myfont.render(("Draws a circle"),1,(0,0,0))
            elt3 = myfont.render(("thats filled and you"),1,(0,0,0))
            elt4 = myfont.render(("can change the size."),1,(0,0,0))
            screen.blit(elt1,(15,415))
            screen.blit(elt2,(15,440))
            screen.blit(elt3,(15,465))
            screen.blit(elt4,(15,490))

    if RectTool.collidepoint(mx,my):#Allows you to select the elipse function 
        draw.rect(screen,(255,0,0),RectTool,1) 
        if mb[0]==1:
            tool="RectTool"
            draw.rect(screen,(226,199,141),textRect)
            rt1 = myfont.render(("Rectangle Tool"),1,(0,0,0))
            rt2 = myfont.render(("Draws a rectangle"),1,(0,0,0))
            rt3 = myfont.render(("in which you can"),1,(0,0,0))
            rt4 = myfont.render(("change the size."),1,(0,0,0))
            screen.blit(rt1,(15,415))
            screen.blit(rt2,(15,440))
            screen.blit(rt3,(15,465))
            screen.blit(rt4,(15,490))

    if FRectTool.collidepoint(mx,my):#Allows you to select the elipse function 
        draw.rect(screen,(255,0,0),FRectTool,1) 
        if mb[0]==1:
            tool="FRectTool"
            draw.rect(screen,(226,199,141),textRect)
            frt1 = myfont.render(("Rectangle Tool(Filled)"),1,(0,0,0))
            frt2 = myfont.render(("Draws a rectangle"),1,(0,0,0))
            frt3 = myfont.render(("thats filled and you"),1,(0,0,0))
            frt4 = myfont.render(("can change the size."),1,(0,0,0))
            screen.blit(frt1,(15,415))
            screen.blit(frt2,(15,440))
            screen.blit(frt3,(15,465))
            screen.blit(frt4,(15,490))

    if InputtextRect.collidepoint(mx,my):#Allows you to select the line function 
        draw.rect(screen,(255,0,0),InputtextRect,1)
        if mb[0]==1:
            tool="Inputtext"
            draw.rect(screen,(226,199,141),textRect)
            tt1 = myfont.render(("Text Tool"),1,(0,0,0))
            tt2 = myfont.render(("Allows the user to "),1,(0,0,0))
            tt3 = myfont.render(("to input text on "),1,(0,0,0))
            tt4 = myfont.render(("the canvas."),1,(0,0,0))
            screen.blit(tt1,(15,415))
            screen.blit(tt2,(15,440))
            screen.blit(tt3,(15,465))
            screen.blit(tt4,(15,490))

    if undoRect.collidepoint(mx,my):#Allows you to select the line function 
        draw.rect(screen,(255,0,0),undoRect,1)
        if mb[0]==1:
            tool="undo"
            draw.rect(screen,(226,199,141),textRect)
            ut1 = myfont.render(("Undo Tool"),1,(0,0,0))
            ut2 = myfont.render(("Allows the user to "),1,(0,0,0))
            ut3 = myfont.render(("refresh the previous "),1,(0,0,0))
            ut4 = myfont.render(("command one has made"),1,(0,0,0))
            ut5 = myfont.render(("after making a mistake."),1,(0,0,0))
            screen.blit(ut1,(15,415))
            screen.blit(ut2,(15,440))
            screen.blit(ut3,(15,465))
            screen.blit(ut4,(15,490))
            screen.blit(ut5,(15,515))

    if redoRect.collidepoint(mx,my):#Allows you to select the line function 
        draw.rect(screen,(255,0,0),redoRect,1)
        if mb[0]==1:
            tool="redo"
            draw.rect(screen,(226,199,141),textRect)
            rt1 = myfont.render(("Redo Tool"),1,(0,0,0))
            rt2 = myfont.render(("Allows the user to "),1,(0,0,0))
            rt3 = myfont.render(("restore the previous "),1,(0,0,0))
            rt4 = myfont.render(("command one has made"),1,(0,0,0))
            rt5 = myfont.render(("after deleting something."),1,(0,0,0))
            screen.blit(rt1,(15,415))
            screen.blit(rt2,(15,440))
            screen.blit(rt3,(15,465))
            screen.blit(rt4,(15,490))
            screen.blit(rt5,(15,515))

    if saveRect.collidepoint(mx,my):#Allows you to select the line function 
        draw.rect(screen,(255,0,0),saveRect,1)
        if mb[0]==1:
            tool="save"
            draw.rect(screen,(226,199,141),textRect)
            sat1 = myfont.render(("Save Tool"),1,(0,0,0))
            sat2 = myfont.render(("Saves the painting"),1,(0,0,0))
            sat3 = myfont.render(("you have made to"),1,(0,0,0))
            sat4 = myfont.render(("the paint folder."),1,(0,0,0))
            screen.blit(sat1,(15,415))
            screen.blit(sat2,(15,440))
            screen.blit(sat3,(15,465))
            screen.blit(sat4,(15,490))

    if loadRect.collidepoint(mx,my):#Allows you to select the line function 
        draw.rect(screen,(255,0,0),loadRect,1)
        if mb[0]==1:
            tool="load"
            draw.rect(screen,(226,199,141),textRect)
            lot1 = myfont.render(("Load Tool"),1,(0,0,0))
            lot2 = myfont.render(("Retrieves images and"),1,(0,0,0))
            lot3 = myfont.render(("paintings you have"),1,(0,0,0))
            lot4 = myfont.render(("already made from"),1,(0,0,0))
            lot5 = myfont.render(("the paint folder."),1,(0,0,0))
            screen.blit(lot1,(15,415))
            screen.blit(lot2,(15,440))
            screen.blit(lot3,(15,465))
            screen.blit(lot4,(15,490))
            screen.blit(lot5,(15,515))

    if stampRect.collidepoint(mx,my):
        if mb[0]==1:
            draw.rect(screen,(226,199,141),textRect)
            stamptt1 = myfont.render(("Stamp Tool"),1,(0,0,0))
            stamptt2 = myfont.render(("Allows the user to "),1,(0,0,0))
            stamptt3 = myfont.render(("select a stamp from the "),1,(0,0,0))
            stamptt4 = myfont.render(("options below and place"),1,(0,0,0))
            stamptt5 = myfont.render(("it on the canvas."),1,(0,0,0))
            screen.blit(stamptt1,(15,415))
            screen.blit(stamptt2,(15,440))
            screen.blit(stamptt3,(15,465))
            screen.blit(stamptt4,(15,490))
            screen.blit(stamptt5,(15,515))
            
  
    if mb[0]==1 and canvasRect.collidepoint(mx,my): 
        screen.set_clip(canvasRect) #Makes sure you dont draw out of the canvas 
  
        if tool == "pencil": #Allows you to use the pencil function on the 
            draw.line(screen,drawColour,(omx,omy),(mx,my)) #Canvas
            
  
        if tool == "eraser": #Allows you to use the eraser function on the 
            draw.circle(screen,(255,255,255),(mx,my),20) #canvas 
  
        if tool == "clear": #Allows you to use the clear function on the 
            draw.rect(screen,(255,255,255),(300,100,700,600),1000) #canvas 
  
        if tool == "brush": 
            x=mx-omx 
            y=my-omy 
            d = int(((x)**2+(y)**2)**0.5) 
            if d == 0: 
                d = 1
            for i in range(int(d)): 
                dx = int(omx+i/d*x) 
                dy = int(omy+i/d*y) 
                draw.circle(screen,drawColour,(dx,dy),sz)     
  
        if tool == "fill": #Allows you to use the spray function on the 
            draw.rect(screen,drawColour,(300,100,700,600),1000) #canvas 
  
        if tool == "spray": 
            c=(randint(0,255), randint(0,255),randint(0,255)) 
            x2,y2 = (randint(mx-40,mx+40),randint(my-40,my+40)) 
            if hypot(x2-mx,y2-my)<40: 
                draw.circle(screen,drawColour,(x2,y2),0)

        if tool == "line":
            screen.blit(copy,(0,0))
            draw.line(screen,drawColour,start,(mx,my),sz)

        if tool == "elipse":
            screen.blit(copy,(0,0))
            oval = Rect(ex,ey,mx-ex,my-ey)
            oval.normalize()
            if oval.height<sz2*2 or oval.width<sz2*2:
                draw.ellipse(screen,drawColour,oval)
            else:
                draw.ellipse(screen,drawColour,oval,sz2)

        if tool == "Fellipse":
            screen.blit(copy,(0,0))
            oval = Rect(ex,ey,mx-ex,my-ey)
            oval.normalize()
            draw.ellipse(screen,drawColour,oval)

        if tool == "RectTool":
            screen.blit(copy,(0,0))
            draw.rect(screen,drawColour,(ex,ey,mx-ex,my-ey),sz2)

        if tool == "FRectTool":
            screen.blit(copy,(0,0))
            draw.rect(screen,drawColour,(ex,ey,mx-ex,my-ey))

        if tool == "Inputtext":
            txt = getName(False)     # this is how you would call my getName function
                                # your main loop will stop looping until user hits enter
            txtPic = myfont.render(txt, True, (drawColour))
            screen.blit(txtPic,(mx,my))

        if tool == "save":
            txt = getName()                                 #Calls getName
            pygame.image.save(screen.subsurface(canvasRect),'text.png')    #Saves Image
            
            

        if tool == "load":
            txt = loading()
            img = pygame.image.load(txt)                        #Loads Image
            screen.blit(img,(10,10))                           #Blits image onto canvas


#    if mb[0]==1 and canvasRect.collidepoint(mx,my):
#        screen.set_clip(canvasRect)
 #           if tool=="allen":
#                screen.blit(copy,(0,0))
#                screen.blit(allen,(mx-100,my-260))
 #       if drose.collidepoint(mx,my):
##                screen.blit(copy,(0,0))
 #               screen.blit(drose,(mx-100,my-260))
#       if kevind.collidepoint(mx,my):
 #           if tool=="kevind":
#                screen.blit(copy,(0,0))
#                screen.blit(kevind,(mx-100,my-260))
 #       if kobe.collidepoint(mx,my):
#            if tool=="kobe":
#                screen.blit(copy,(0,0))
#                screen.blit(kobe,(mx-100,my-260))
 #       screen.set_clip(None)
            
            






   
        screen.set_clip(None) #Makes sure you dont draw out of the canvas


  
          
  
    display.flip() 
  
  
quit() 
