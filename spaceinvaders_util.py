#
# Utilities for making a 2.5D game using pygame and gl_relativity.
# 

from pygame.sprite import Sprite as PygameSprite
from pygame.sprite import Group as PygameGroup

from pygame import time

from gl_relativity_py.objects import Worldline, Object, Mesh, primitives

class GL_Sprite(PygameSprite):
    def __init__(self,*groups):
        super().__init__(groups)
        self.depth = 0
        self.object = None
        
    def gl_draw(self):
        # Perform OpenGL draw calls
        # Lazy way of converting keeping wl up to date
        self.object.wl._events.append( [time.get_ticks(), (self.rect.x-400), (300-self.rect.y), -self.depth] )
        self.object.wl.dirty = True
        self.object.draw()
        
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
        
