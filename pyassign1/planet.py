import math
import turtle

turtle.colormode(255)
sun=turtle.Turtle()
sun.color('yellow')
trls=[]
radi=[57.9,108.2,149.6,227.9,778.3,1427.0]
period=[87.97,224.7,365.26,686.98,11.86*365.25,29.46*365.25]
es=[0.206,0.007,0.017,0.093,0.048,0.056]
a=[]
b=[]
C=[(0,0,255),(0,255,0),(255,0,0),(0,0,0),(255,179,0),(0,255,255)]
for i in range(6):
    a.append(radi[i]/5)
    b.append(a[i]*math.sqrt(1-es[i]**2))
    trls.append(turtle.Turtle())
    trls[i].color((C[i]), (C[i]))
    trls[i].pu()
    trls[i].goto(a[i],0)
    trls[i].pd()
    trls[i].shape('circle')
for t in range(1000000):
    w=2*math.pi*t*10 
    for i in range(6):
        trls[i].goto(a[i]*math.cos(w/period[i]),b[i]*math.sin(w/period[i]))
        
