import turtle
import time
from pydub import AudioSegment
from pydub.playback import play


window = turtle.Screen()
window.title("Funny little dancing man look at him go")
window.bgcolor("white")

window.addshape("guy_default.gif")
window.addshape("guy_left.gif")
window.addshape("guy_right.gif")
window.addshape("guy_up1.gif")
window.addshape("guy_up2.gif")
window.addshape("guy_down.gif")

guy = turtle.Turtle()
guy.shape('guy_default.gif')

def updateLeft() :
    guy.shape('guy_left.gif')
    time.sleep(0.1)
    guy.shape('guy_default.gif')

def updateRight() :
    guy.shape('guy_right.gif')
    time.sleep(0.1)
    guy.shape('guy_default.gif')

def updateUp() :
    for x in range(5):
        guy.shape('guy_up1.gif')
        time.sleep(0.02)
        guy.shape('guy_up2.gif')
        time.sleep(0.02)
    guy.shape("guy_default.gif")

song = AudioSegment.from_wav("C:/Users/nitna/OneDrive/Documents/GitHub/DancingGuy/vine_boom.wav")

def updateDown() :
    guy.shape('guy_down.gif')
    play(song)
    guy.shape('guy_default.gif')
    
    

window.onkeypress(updateLeft, "Left")
window.onkeypress(updateRight, "Right")
window.onkeypress(updateUp, "Up")
window.onkeypress(updateDown, "Down")
window.listen()

window.mainloop()