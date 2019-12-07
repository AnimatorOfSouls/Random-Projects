### Created by Solaris :> ###
## MIT LICENSE ###

# V O I D --- R U N N E R #
# As your run, blocks fall from beneath your feet. How long can you stay alive?

from mine import *
from drawing import *
import time

mc = Minecraft()
d = Drawing()





### CONFIGS ###
platform_block = block.WOOL_BLACK       #The block you want the falling floor to be made out of (default: WOOL_BLACK)
radius = 7                          #Set the radius of your arena (default: 7)
countdown = 3                       #Length of countdown (default: 3)





### MODULES ###
#Sends some intro messages in chat, including instructions and a countdown to the game starting.
def welcome_message(cd):
    mc.postToChat("Welcome to Void Runner!")
    time.sleep(2)

    mc.postToChat("As your run, blocks fall from beneath your feet.")
    mc.postToChat("Try to survive for as long as possible without falling into the void.")
    time.sleep(3)

    #Countdown
    for i in range(cd):
        mc.postToChat(cd-i)
        time.sleep(1)

    mc.postToChat("RUN!")



def build_arena(x,y,z,block,radius):
    for x_range in range(-radius, radius+1):
        for z_range in range(-radius, radius+1):
            if x_range**2+z_range**2 <= radius**2:
                d.point(x+x_range,y-1,z+z_range,block)



def runner(orig_pos):
    alive = True

    while alive == True:
        pos = mc.player.getPos()
        mc.setBlock((pos.x,pos.y-1,pos.z), block.AIR)
        time.sleep(0.3)

        ## Things that cause you to die - more can be added later
        #Die - if you fall of the platform
        if pos.y < orig_pos.y-2:
            mc.postToChat("You Died!")
            alive=False





### GAME ###
pos = mc.player.getPos()

build_arena(pos.x,pos.y,pos.z,platform_block,radius)
time.sleep(1)
welcome_message(countdown)
runner(pos)
