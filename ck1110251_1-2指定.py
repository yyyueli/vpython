from vpython import *
#Web VPython 3.2
x = arrow(pos=vector(0,0,0), axis=vector(1,0,0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,1,0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,1), shaftwidth=0.02, color=color.blue)
ball = sphere(radius=0.06, color=color.yellow, pos=vector(0,0,0), v=vector(3,0,0),a=vector(-1,-0.5,0))

dt = 0.001    
t = 0.0

while t<5:          
    rate(1/dt)
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt 
    plot_t = t%0.4
    
    if ball.v.x > 0 and ball.v.x + ball.a.x*dt < 0:
        print (t)
        print (ball.pos)
        print (ball.v)
            
    if plot_t + dt >= 0.4 and plot_t < 0.4:    
        arrow(color=color.red, pos=ball.pos, axis=ball.v, shaftwidth=0.05)    
        arrow(color=color.green, pos=ball.pos, axis=ball.a, shaftwidth=0.05)    
        sphere(color=color.yellow, pos=ball.pos, radius=0.06)
    t = t+dt