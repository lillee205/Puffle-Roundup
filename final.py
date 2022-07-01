GlowScript 3.0 VPython

scene.bind('keydown', keydown_fun)     # Function for key presses
scene.bind('click', click_fun)         # Function for mouse clicks
scene.background = vec(0.3,.5,1)    # Light gray (0.8 out of 1.0)
scene.width = 640                      # Make the 3D canvas larger
scene.height = 480
ground = box(size = vec(20, 1, 20), pos = vec(0, -1, 0), color = .9999*vec(1,1,1))

T = text(text='secret, ooooo',
     pos = vec(0,-2,0), align='center', color=color.green)

T.rotate(axis = vec(1, 0, 0), angle=(pi/2))

winCount = 0

# +++ start of OBJECT_CREATION section
# These functions create "container" objects, called "compounds"
def make_penguin(starting_position, starting_vel = vec(0, 0, 0)):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vec(0, 0, 0).

       Compounds can have any number of components.  Here are the
       penguin's components:
    """
    #print instructions for game in terminal
    print("Welcome to Puffle Roundup!")
    print("Instructions: Herd the puffles by chasing them into the pen with the penguin!")
    print("Keys:", "Move with the arrow keys, press spacebar to restart")
    print("Hint:", "Click using your mouse or trackpad to win instantly,")
    print("         note that this is not recommended if you wish to have the full experience.")
    penguin_body = ellipsoid(length = 2, width = 2, height = 3, pos = vec(0, 1, 0), color = color.blue)
    penguin_eye1 = sphere(size = 2*0.5*vec(1, 1, 1), pos = vec(.2, 1.5, .5), color = color.white)
    penguin_eye2 = sphere(size = 2*0.5*vec(1, 1, 1), pos = vec(-.2, 1.5, .5), color = color.white)
    penguin_pupil1 = sphere(size = 2*0.3*vec(1, 1, 1), pos = vec(.25, 1.5, 1), color = color.black)
    penguin_pupil2 = sphere(size = 2*0.3*vec(1, 1, 1), pos = vec(-.25, 1.5, 1), color = color.black)
    penguin_mouth = ellipsoid(length = 0.8, width = 0.4, height = 0.4, pos = vec(0, 1, 1), color = color.orange)
    # make a list to "fuse" with a compound
    penguin_objects = [penguin_body, penguin_eye1, penguin_eye2, penguin_pupil1, penguin_pupil2, penguin_mouth]
    # now, we create a compound -- we'll name it com_alien:
    com_penguin = compound(penguin_objects, pos = starting_position)
    com_penguin.vel = starting_vel    # set the initial velocity
    return com_penguin
    
def make_puffle(starting_position, starting_vel = vec(0,0,0)):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to puffle allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vec(0, 0, 0).
       Compounds can have any number of components.  Here are the
       puffle's components:
    """
    colList = [color.green, color.white, color.yellow, color.red, color.orange, color.purple, color.cyan]
    puffle_color = vec(choice(colList))
    puffle_body = ellipsoid(size = 1.0*vec(1, 1, 1), pos = vec(0, 0, 0), length = 1, width = 1.2, height = 1, color = puffle_color)
    puffle_eye1 = sphere(size = 0.5*vec(1, 1, 1), pos = vec(.25, .1, .2), color = color.white)
    puffle_eye2 = sphere(size = 0.5*vec(1, 1, 1), pos = vec(.25, .1, -.2), color = color.white)
    puffle_pupil1 = sphere(size = 0.3*vec(1, 1, 1), pos = vec(.4, .1, -.21), color = color.black)
    puffle_pupil2 = sphere(size = 0.3*vec(1, 1, 1), pos = vec(.4, .1, .21), color = color.black)
    puffle_hair1 = cone(pos = 0.42*vec(0, .9, .1), axis = vec(0, .2, 0.05), size = 0.3*vec(1, 1, 1), radius = vec(0.1, 0.1, 0.1),  color = puffle_color)
    puffle_hair6 = cone(pos = 0.42*vec(0, .9, -.1), axis = vec(0, .2, -0.05), size = 0.3*vec(1, 1, 1), radius = vec(0.1, 0.1, 0.1),  color = puffle_color)
    puffle_hair2 = cone(pos = 0.42*vec(0 , .9, .4), axis = vec(0, .2, 0.1), size = 0.3*vec(1, 1, 1), radius = vec(0.1, 0.1, 0.1),  color = puffle_color)
    puffle_hair3 = cone(pos = 0.42*vec(0 , .9, -.4), axis = vec(0, .2, -0.1), size = 0.3*vec(1, 1, 1), radius = vec(0.1, 0.1, 0.1),  color = puffle_color)
    puffle_hair4 = cone(pos = 0.42*vec(0 , .9, -.6), axis = vec(0, .2, -0.2), size = 0.3*vec(1, 1, 1), radius = vec(0.01, 0.01, 0.01),  color = puffle_color)
    puffle_hair5 = cone(pos = 0.42*vec(0 , .9, .6), axis = vec(0, .2, 0.2), size = 0.3*vec(1, 1, 1), radius = vec(0.01, 0.01, 0.01),  color = puffle_color)
    puffle_hair7 = cone(pos = 0.42*vec(0 , .9, .8), axis = vec(0, .2, 0.4), size = 0.3*vec(1, 1, 1), radius = vec(0.01, 0.01, 0.01),  color = puffle_color)
    puffle_hair8 = cone(pos = 0.42*vec(0 , .9, -.8), axis = vec(0, .2, -0.4), size = 0.3*vec(1, 1, 1), radius = vec(0.01, 0.01, 0.01),  color = puffle_color)
    # make a list to "fuse" with a compound
    puffle_objects = [puffle_body, puffle_eye1, puffle_eye2, puffle_pupil1, puffle_pupil2, puffle_hair1, puffle_hair6, puffle_hair2, puffle_hair3, puffle_hair4, puffle_hair5, puffle_hair7, puffle_hair8]
    # now, we create a compound -- we'll name it com_alien:
    com_puffle = compound(puffle_objects, pos = starting_position)
    com_puffle.vel = starting_vel    # set the initial velocity
    com_puffle.move = True
    
    return com_puffle
    
def make_tree(starting_position):
    """ The lines below make a tree at a position starting_position
    """
    height = 2
    wide = 2
    thickness = 2
    tree_leaves1 = cone(size = vec(wide,height,thickness), axis = vec(0,1,0), pos = vec(0,2,0), color = vec(0,.5,0))
    tree_leaves2 = cone(size = .8*vec(wide,height,thickness), axis = vec(0,1,0), pos = vec(0,3,0), color = vec(0,.5,0))
    tree_leaves3 = cone(size = .6*vec(wide,height,thickness), axis = vec(0,1,0), pos = vec(0,4.0,0), color = vec(0,.5,0))
    snow_leaves1 = cone(size = vec(wide,height,thickness), axis = vec(0,1,0), pos = vec(0,2.2,0), color = .9999*vec(1,1,1))
    snow_leaves2 = cone(size = .8*vec(wide,height,thickness), axis = vec(0,1,0), pos = vec(0,3.2,0), color = .9999*vec(1,1,1))
    snow_leaves3 = cone(size = .6*vec(wide,height,thickness), axis = vec(0,1,0), pos = vec(0,4.2,0), color = .9999*vec(1,1,1))
    tree_trunk = cylinder(size = 1.0*vec(.5,.5,.5), axis = vec(0,1,0), pos = vec(0,1,0), color = .4*vec(1.0, 0.7, 0.3))
    tree_trunk1 = cylinder(size = 1.0*vec(.5,.5,.5), axis = vec(0,1,0), pos = vec(0,1.5,0), color = .4*vec(1.0, 0.7, 0.3))
    tree_objects = [tree_leaves1, tree_leaves2, tree_leaves3, snow_leaves1, snow_leaves2, snow_leaves3, tree_trunk, tree_trunk1]
    com_tree = compound(tree_objects, pos = starting_position)
    com_tree.pos.y = 1.5
    return com_tree

def make_fence1(starting_position):
    """ The lines below make a fence at a position starting_position
    """
    pOst = cylinder(size = 1.0*vec(1,.5,.5), axis = vec(0,1,0), pos = vec(0,1,0), color = .35*vec(1.0, 0.7, 0.3))
    pOst1 = cylinder(size = 1.0*vec(1,.5,.5), axis = vec(0,1,0), pos = vec(3,1,0), color = .35*vec(1.0, 0.7, 0.3))
    pOst2 = cylinder(size = 1.0*vec(1,.5,.5), axis = vec(0,1,0), pos = vec(-3,1,0), color = .35*vec(1.0, 0.7, 0.3))
   
    slat1 = box(size = vec(.1, .5, 6), axis = vec(0,0,1), pos = vec(0,1.7,0), color = .35*vec(1.0, 0.7, 0.3))
   
    fence1_objects = [pOst, pOst1, pOst2,slat1]
    com_fence1 = compound(fence1_objects, pos = starting_position)
    com_fence1.pos.y = 0
    return com_fence1
   
   
def make_fence2(starting_position):
    """ The lines below make a fence at a position starting_position
    """

    pOst3 = cylinder(size = 1.0*vec(1,.5,.5), axis = vec(0,1,0), pos = vec(3,1,-2.5), color = .35*vec(1.0, 0.7, 0.3))
    pOst4 = cylinder(size = 1.0*vec(1,.5,.5), axis = vec(0,1,0), pos = vec(3,1,-5), color = .35*vec(1.0, 0.7, 0.3))
    slat2 = box(size = vec(.1, .5, 5.2), axis = vec(1,0,0), pos = vec(3,1.7,-2.2), color = .35*vec(1.0, 0.7, 0.3))
 

    fence2_objects = [pOst3, pOst4, slat2]
    com_fence2 = compound(fence2_objects, pos = starting_position)
    com_fence2.pos.y = 0
    return com_fence2
   
   
def make_fence3(starting_position):
    """ The lines below make a fence at a position starting_position
    """

    pOst5 = cylinder(size = 1.0*vec(1,.5,.5), axis = vec(0,1,0), pos = vec(-3,1,-2.5), color = .35*vec(1.0, 0.7, 0.3))
    pOst6 = cylinder(size = 1.0*vec(1,.5,.5), axis = vec(0,1,0), pos = vec(-3,1,-5), color = .35*vec(1.0, 0.7, 0.3))
    slat3 = box(size = vec(.1, .5, 5.2), axis = vec(1,0,0), pos = vec(-3,1.7,-2.2), color = .35*vec(1.0, 0.7, 0.3))
       
    fence3_objects = [pOst5, pOst6, slat3]
    com_fence3 = compound(fence3_objects, pos = starting_position)
    com_fence3.pos.y = 0
    return com_fence3
    
def make_snow(starting_position):
    """ The lines below make a snowflake that falls from position starting_position
    """
    rod1 = cylinder(size = 1.0*vec(1,.15,.15), axis = vec(0,1,0), pos = vec(0,0,0), color = vec(.8, .95, .999))
    rod2 = cylinder(size = 1.0*vec(1,.15,.15), axis = vec(.6,.4,0), pos = vec(-.4,.2,0), color = vec(.8, .95, .999))
    rod3 = cylinder(size = 1.0*vec(1,.15,.15), axis = vec(-.6,.4,0), pos = vec(.4,.2,0), color = vec(.8, .95, .999))
    rod4 = cylinder(size = 1.0*vec(1,.15,.15), axis = vec(0,.4,.6), pos = vec(0,.2,-.4), color = vec(.8, .95, .999))
    rod5 = cylinder(size = 1.0*vec(1,.15,.15), axis = vec(0,.4,-.6), pos = vec(0,.2,0.4), color = vec(.8, .95, .999))
    
    snow_objects = [rod1, rod2, rod3, rod4, rod5]
    com_snow = compound(snow_objects, pos = starting_position)
    com_snow.pos.y = 5
    return com_snow
    
def make_sleigh(starting_position, starting_vel):
    sleighBox = box(size = 3*vec(1.5,.8,1), pos = vec(0,0,0), color = .5*vec(1.0, 0.7, 0.3))
    sleighBack = cylinder(size = 3*vec(1,1,1), axis = vec(0,0,1), pos = vec(-2.5,.3,-1.5), color = .5*vec(1.0, 0.7, 0.3))
    sleighFront = cylinder(size = 1.5*vec(2,1,1), axis = vec(0,0,1), pos = vec(2.1,1,-1.5), color = .5*vec(1.0, 0.7, 0.3))
    sleighTrackRail1= box(size = vec(.7,.3,.2), pos = vec(-1.75,-1.3,1.35), color = .5*vec(1.0, 0.7, 0.3))
    sleighTrackRail2= box(size = vec(.7,.3,.2), pos = vec(1.75,-1.3,1.35), color = .5*vec(1.0, 0.7, 0.3))
    sleighTrackRail21= box(size = vec(.7,.3,.2), pos = vec(-1.75,-1.3,-1.35), color = .5*vec(1.0, 0.7, 0.3))
    sleighTrackRail22= box(size = vec(.7,.3,.2), pos = vec(1.75,-1.3,-1.35), color = .5*vec(1.0, 0.7, 0.3))
    sleighTrack1= box(size = vec(6,.1,.3), pos = vec(-0.25,-1.5,1.35), color = .5*vec(1.0, 0.7, 0.3))
    sleighTrack2= box(size = vec(5,.1,.3), pos = vec(-0.25,-1.5,-1.35), color = .5*vec(1.0, 0.7, 0.3))
    sleigh_objects = [sleighBox, sleighBack, sleighFront, sleighTrackRail1, sleighTrackRail2, sleighTrackRail21, sleighTrackRail22, sleighTrack1, sleighTrack2]
    com_sleigh = compound(sleigh_objects, pos = starting_position)
    com_sleigh.vel = starting_vel
    return com_sleigh


def make_penguin1(starting_position, starting_axis, nose_color, body_color, antler, starting_vel):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vec(0, 0, 0).

       Compounds can have any number of components.  Here are the
       penguin's components:
    """
    penguin_body = ellipsoid(length = 2, width = 2, height = 3, pos = vec(0, 1, 0), color = body_color)
    penguin_eye1 = sphere(size = 2*0.5*vec(1, 1, 1), pos = vec(.2, 1.5, .5), color = color.white)
    penguin_eye2 = sphere(size = 2*0.5*vec(1, 1, 1), pos = vec(-.2, 1.5, .5), color = color.white)
    penguin_pupil1 = sphere(size = 2*0.3*vec(1, 1, 1), pos = vec(.25, 1.5, 1), color = color.black)
    penguin_pupil2 = sphere(size = 2*0.3*vec(1, 1, 1), pos = vec(-.25, 1.5, 1), color = color.black)
    penguin_mouth = ellipsoid(length = 0.8, width = 0.4, height = 0.4, pos = vec(0, 1, 1), color = nose_color)
    
    # make a list to "fuse" with a compound
    if antler == True:
        antler1 = cylinder(size = 1.0*vec(1,.15,.15), axis = vec(.6,.4,0), pos = vec(.3,2.4,0), color = .5*vec(1.0, 0.7, 0.3))
        antler2 = cylinder(size = 1.0*vec(1,.15,.15), axis = vec(-.6,.4,0), pos = vec(-.3,2.4,0), color = .5*vec(1.0, 0.7, 0.3))
        penguin_objects = [penguin_body, penguin_eye1, penguin_eye2, penguin_pupil1, penguin_pupil2, penguin_mouth, antler1, antler2]
    if antler == False:
        penguin_objects = [penguin_body, penguin_eye1, penguin_eye2, penguin_pupil1, penguin_pupil2, penguin_mouth]
    # now, we create a compound -- we'll name it com_alien:
    com_penguin = compound(penguin_objects, pos = starting_position)
    com_penguin.axis = starting_axis    # set the initial velocity
    com_penguin.vel = starting_vel
    return com_penguin
    
sleigh = make_sleigh(starting_position = vec(-0.5, 1,-17), starting_vel = vec(0,0,0))
deer1 = make_penguin1(starting_position = vec(5.5, 1, -17), starting_axis = vec(0,0,-1), nose_color = color.orange, body_color = vec(1.0, 0.7, 0.3), antler = True, starting_vel = vec(0,0,0))  # ball is an object of class sphere
deer2 = make_penguin1(starting_position = vec(9, 1, -17), starting_axis = vec(0,0,-1), nose_color = color.red, body_color = vec(1.0, 0.7, 0.3), antler = True, starting_vel = vec(0,0,0))  # ball is an object of class sphere
deer0 = make_penguin1(starting_position = vec(-.8, 2.5, -17), starting_axis = vec(0,0,-1), nose_color = color.orange, body_color = color.red, antler = False, starting_vel = vec(0,0,0))  # ball is an object of class sphere    

# create boundaries for environment
wallA = box(pos = vec(0, 0, -10), axis = vec(1, 0, 0), size = vec(20, 1, .2), color = vec(.7, .85, .98))
wallB = box(pos = vec(-10, 0, 0), axis = vec(0, 0, 1), size = vec(20, 1, .2), color = vec(.7, .85, .98))
wallC = box(pos = vec(0, 0, 10), axis = vec(1, 0, 0), size = vec(20, 1, .2), color = vec(.7, .85, .98))
wallD = box(pos = vec(10, 0, 0), axis = vec(0, 0, 1), size = vec(20, 1, .2), color = vec(.7, .85, .98))



# A ball that we will be able to control
ball = make_penguin(starting_position = vec(-5, 0, -5), starting_vel = vec(0, 0, 0))  # ball is an object of class sphere

# sleigh and deer and santa creation

# puffle creation
puffle1 = make_puffle(starting_position = vec(5, 0, -2), starting_vel = vec(-1.2, 0, 1))
puffle2 = make_puffle(starting_position = vec(-4, 0, 1), starting_vel = vec(1.1, 0, 1.4))
puffle3 = make_puffle(starting_position = vec(-5, 0, -4), starting_vel = vec(-1.2, 0, 1))
puffle4 = make_puffle(starting_position = vec(1, 0, -6), starting_vel = vec(1.1, 0, 1.3))
puffle5 = make_puffle(starting_position = vec(6, 0, -3), starting_vel =vec(-1.2, 0, -1))
puffle6 = make_puffle(starting_position = vec(-5, 0, -5), starting_vel = vec(1.2, 0, -1))
puffles = [puffle1, puffle2, puffle3, puffle4,puffle5,puffle6]
for i in range(len(puffles)): #rotating puffles so they face the right direction
    puffles[i].rotate(axis = vec(0, 1, 0), angle=(3*pi/2))
    
# tree creation
tree1 = make_tree(starting_position = vec(-7,0,6.5))
tree2 = make_tree(starting_position = vec(7,0,6.5))
tree3 = make_tree(starting_position = vec(-5.5,0,7.5))
tree3 = make_tree(starting_position = vec(5.5,0,7.5))
tree4 = make_tree(starting_position = vec(-8,0,7.5))
tree5 = make_tree(starting_position = vec(8,0,7.5))
tree6 = make_tree(starting_position = vec(-4.5,0,8.5))
tree7 = make_tree(starting_position = vec(4.5,0,8.5))
tree8 = make_tree(starting_position = vec(-8.5,0,8.5))
tree9 = make_tree(starting_position = vec(8.5,0,8.5))
tree10 = make_tree(starting_position = vec(-8.5,0,5.5))
tree11 = make_tree(starting_position = vec(8.5,0,5.5))

#fence 
fence1 = make_fence1(starting_position = vec(0,0,4))
fence2 = make_fence2(starting_position = vec(3,0,1))
fence3 = make_fence3(starting_position = vec(-3,0,1))

#snowflakes
snow = []
for i in range(60):
    snow += make_snow(starting_position = 20*vec.random())

for i in range(len(snow)):
    snow[i].vel = vec(0,-1,0)


# +++ end of OBJECT_CREATION section

# +++ start of ANIMATION section

# Other constants
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vec(0, -3, -2)  # Ask for a bird's-eye view of the scene...

# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt
#
time = 0 #keeps track of snowflakes
counts=[] # keeps track of time for puffle to change velocity randomly
for i in range(len(puffles)):
    counts += [0] 

while True:
    
    rate(RATE)       # maximum number of times per second the while loop runs
    for i in range(len(counts)):   # add frame to count
        counts[i]+= 1
    #for snowflakes falling
    time = time + dt
    for i in range(len(snow)):
        snow[i].pos = snow[i].pos + (snow[i].vel) * dt
        snowfall(snow[i])
        
    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step
    for i in range(len(counts)):
        if puffles[i].move:
            if counts[i] > randint(240, 300):
                counts[i] = 0
                puffles[i].vel = choice([randvel(1,1.5), randvel(-1.5, -1)])
            
       # Update the puffle's position
    for i in range(len(puffles)):
        puffleInPen(puffles[i])
        if puffles[i].move:
            puffles[i].pos = puffles[i].pos + puffles[i].vel/(1.0*RATE) 
        if mag(ball.pos - puffles[i].pos) < 1.0: #if penguin hits puffle, move the puffle with a little nudge
            puffles[i].pos.x += (ball.vel.x)*.01*RATE
            puffles[i].pos.z += -(ball.vel.z)*.01*RATE

    # +++ Start of COLLISIONS -- check for collisions & do the "right" thing

    # If the ball hits walls
    corral_collide(ball)
    for i in range(len(puffles)):
        corral_collide(puffles[i])
        if puffles[i].pos.x < 3 and puffles[i].pos.x > -3 and puffles[i].pos.z < -1.95 and puffles[i].pos.z > -2.05 and mag(puffles[i].pos - ball.pos) > 1.0: # puffle should not be able to go into pen unless penguin is pushing it
            puffles[i].pos.z = -2.05
            puffles[i].vel.z *= -1.0
    # +++ End of COLLISIONS
    
    # +++ holiday celebrations 
    
    sleighbounds()
    PenState = allInPen()
    if PenState == True:
        for i in range(len(snow)):
            snow[i].color = 5*vec.random()
        
        sleigh.vel = vec(1,1,0)
        deer0.vel = vec(1,1,0)
        deer1.vel = vec(1,1,0)
        deer2.vel = vec(1,1,0)
        
        winCount += 1
        if winCount == 1:
            print("You won Puffle Roundup! Congratulations!")

    sleigh.pos = sleigh.pos + sleigh.vel*dt
    deer0.pos = deer0.pos + deer0.vel*dt
    deer1.pos = deer1.pos + deer1.vel*dt
    deer2.pos = deer2.pos + deer2.vel*dt
    
        


# +++ start of EVENT_HANDLING section -- separate functions for
#                                keypresses and mouse clicks...
def snowfall(snow):
    """ Falling snow
        Snow must have a .pos field
    """
    if snow.pos.y < 0:          
        snow.pos.y = 6 + choice([1,2,3,4,5,6]) 
        snow.pos.x = 20*random()*choice([1,-1])
        snow.pos.z = 20*random()*choice([1,-1])
        
def keydown_fun(event):
    """This function is called each time a key is pressed."""
    # ball.color = randcolor()  # this turns out to be very distracting!
    key = event.key
    ri = randint(0, 10)
    amt = 0.6 
    # move the ball
    if key == 'up':
        ball.pos = ball.pos + vec(0, 0, -amt)
        ball.vel.z = 1
    elif key == 'left':
        ball.pos = ball.pos + vec(-amt, 0, 0)
        ball.vel.x = -1
    elif key == 'down':
        ball.pos = ball.pos + vec(0, 0, amt)
        ball.vel.z = -1
    elif key == 'right':
        ball.pos = ball.pos + vec(amt, 0, 0)
        ball.vel.x = 1
    elif key in ' rR':
        ball.vel = vec(0, 0, 0) # Reset! via the spacebar, " "
        ball.pos = vec(0, 0, 0)
        for i in range(len(puffles)):
            puffles[i].move = True
            puffles[i].vel = choice([randvel(1, 1.5), randvel(-1.5, 1)])
            puffles[i].pos = choice([vec(5,0,-2),vec(-4, 0, 1), vec(-5, 0, -4),vec(1, 0, -6), vec(6, 0, -3), vec(-5, 0, -5)])

def click_fun(event):
    """This is a cheating way to win the game :)."""
    for i in range(len(snow)):
        snow[i].color = 5*vec.random()
        
    sleigh.vel = vec(1,1,0)
    deer0.vel = vec(1,1,0)
    deer1.vel = vec(1,1,0)
    deer2.vel = vec(1,1,0)
    for i in range(len(puffles)):
        puffles[i].pos.x = randint(-2.8, 2.8)  
        puffles[i].pos.z = randint(-1.8, 3.8)
        puffles[i].vel = vec(0,0,0)
        

# +++ End of EVENT_HANDLING section

# win state
def allInPen():
    inPen = 0
    for i in range(len(puffles)):
        if not puffles[i].move:
            inPen += 1
    if inPen == len(puffles):
        return True
    else:
        return False


# +++ Other functions can go here...

def choice(L):
    """Implements Python's choice using the random() function."""
    LEN = len(L)                        # Get the length
    randomindex = int(LEN*random())     # Get a random index
    return L[randomindex]               # Return that element

def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low               # Swap if out of order!
    LEN = int(hi) - int(low) + 1.       # Get the span and add 1
    randvalue = LEN*random() + int(low) # Get a random value
    return int(randvalue)               # Return the integer part of it
def randvel(low, hi):
    """Returns velocity vector of random from low to hi"""
    if hi < low:
        low, hi = hi, low
    LEN = hi - low + 1
    randValue1 = LEN*random() + low
    randValue2 = LEN*random() + low
    return vec(randValue1, 0, randValue2)
def randcolor():
    """Returns a vector of (r, g, b) random from 0.0 to 1.0."""
    r = random(0.0, 1.0)
    g = random(0.0, 1.0)
    b = random(0.0, 1.0)
    return vec(r, g, b)                 # A color is a three-element vector

def corral_collide(ball):
    """Corral collisions!
       Ball must have a .vel field and a .pos field.
    """

    if ball.pos.z < wallA.pos.z:           # Hit -- check for z
        ball.pos.z = wallA.pos.z           # Bring back into bounds
        ball.vel.z *= -1.0    
        # Reverse the z velocity

    # If the ball hits wallB
    if ball.pos.x < wallB.pos.x:           # Hit -- check for x
        ball.pos.x = wallB.pos.x           # Bring back into bounds
        ball.vel.x *= -1.0                 # Reverse the x velocity
    
    if ball.pos.z > 5.5:
        ball.pos.z =  5.5
        ball.vel.z *= -1.0
    if ball.pos.x > wallD.pos.x:
        ball.pos.x = wallD.pos.x
        ball.vel.x *= -1.0
    if ball.pos.x < 3 and ball.pos.x > -3 and ball.pos.z > 3.95 and ball.pos.z < 4.05: # if ball hits bottom of pen from outside
        ball.pos.z = fence1.pos.z + 0.05
        ball.vel.z *= -1.0
    if ball.pos.z > -2 and ball.pos.z < 4 and ball.pos.x < 3.05 and ball.pos.x > 2.95: # if ball hits pen on right
        ball.pos.x = fence2.pos.x + 0.05
        ball.vel.x *= -1.0
    if ball.pos.z > -2 and ball.pos.z < 4 and ball.pos.x > -3.05 and ball.pos.x < -2.95: # if ball hits pen
        ball.pos.x = fence3.pos.x - 0.05
        ball.vel.x *= -1.0
def puffleInPen(puffle):
    '''if puffle is herded into pen, it will stop moving'''
    if puffle.pos.x < 2.8 and puffle.pos.x > -2.8 and puffle.pos.z > -1.8 and puffle.pos.z < 3.8:
        puffle.vel = vec(0,0,0) #IMPORTANT: cannot have puffle moving afterwards...maybe a variable of some type needs to be created?    
        puffle.move = False
        
def sleighbounds():
    if deer2.pos.x > 20:
        sleigh.pos.x -= 40
        deer0.pos.x -= 40
        deer1.pos.x -= 40
        deer2.pos.x -= 40
        sleigh.pos.y = 5
        deer0.pos.y = 6.5
        deer1.pos.y = 5
        deer2.pos.y = 5
        
