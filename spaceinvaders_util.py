#
# Utilities for making a 2.5D game using pygame and gl_relativity.
# 

import numpy as np

from pygame.sprite import Sprite as PygameSprite
from pygame.sprite import Group as PygameGroup

#from pygame import time

from gl_relativity_py.objects import Worldline, Object, Mesh, primitives
from gl_relativity_py import camera 

time = 0

class GL_Sprite(PygameSprite):
    def __init__(self,*groups):
        super().__init__(groups)
        self.depth = 0
        self.object = None
        
        # Default to vel tracking being unused (slow)
        self.gl_dirty = 2
        self._vel = np.array([0.0,0.0])
        
    def gl_draw(self):
        global time 

        # Perform OpenGL draw calls
        if self.gl_dirty == 2:
            # _gl_dirty is 2, ie reload wl every frame
            self.object.wl._events.append( [time, (self.rect.x-400), (300-self.rect.y), -self.depth] )
            self.object.wl.dirty = True
        elif self.gl_dirty == 1:
            # _gl_dirty is 1, velocity has changed, update wl
            self.object.wl._events.append( [time, (self.rect.x-400), (300-self.rect.y), -self.depth] )
            self.object.wl.final_vel = np.array([self.vel[0],-self.vel[1],0.0])
            self.object.wl.initial_vel = np.array([self.vel[0],-self.vel[1],0.0])
            self.object.wl.dirty = True
            self.gl_dirty = 0
        
        self.object.draw()
        
        # Handle position updates
        if self.gl_dirty != 2:
            self.rect.x += self.vel[0]
            self.rect.y += self.vel[1]
        
    @property
    def vel(self):
        return self._vel
    
    @vel.setter
    def vel(self, vel):
        if not np.array_equal(vel, self._vel):
            self._vel = vel
            # Only set dirty if dirty is set to 0
            self.gl_dirty = 1 if self.gl_dirty == 0 else self.gl_dirty


        
class GL_Group(PygameGroup):
    def __init__(self,*groups):
        super().__init__(groups)
        
    def draw(self, surface=None, *args):
        if surface is not None:
            PygameGroup.draw(self, surface, args)
        else:
            # If no surface is given, drawing gl object
            for sprite in self.sprites():
                if isinstance(sprite, GL_Sprite):
                    sprite.gl_draw()
        
def set_time(t):
    global time
    camera.set_time(t)
    time = t