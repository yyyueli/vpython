from vpython import *
#Web VPython 3.2
x = arrow(pos=vector(0,0,0), axis=vector(1,0,0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,1,0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,1), shaftwidth=0.02, color=color.blue)


ball = sphere(radius=0.5, color=color.yellow, pos=vector(0,0,0), v=vector(0,0,0),a=vector(5,0,0))
dt = 0.001    
t = 0.0
gd1 = graph(title = "x-t plot", width=600, height=400, xtitle="t", ytitle="x")
f1 = gcurve(color=color.blue)

gd2 = graph(title = "v-t plot", width=600, height=400, xtitle="t", ytitle="v")
f2 = gcurve(color=color.red)

gd3 = graph(title = "a-t plot", width=600, height=400, xtitle="t", ytitle="a")
f3 = gcurve(color=color.green)


while t<6:          
    rate(1/dt)
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt 
    
    if t>2:
        ball.a.x=-5
    f1.plot(pos=(t,ball.pos.x))
    f2.plot(pos=(t,ball.v.x))
    f3.plot(pos=(t,ball.a.x))
    if ball.v.x > 0 and ball.v.x + ball.a.x*dt < 0:
        print (t)
        print (ball.pos)
        print (ball.v)
    t = t+dt
