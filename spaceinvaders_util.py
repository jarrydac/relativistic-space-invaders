from pygame.sprite import Sprite as PygameSprite

from gl_relativity_py.objects import Worldline, Object, Mesh, primitives

class GL_Sprite(PygameSprite):
    def __init__(self,*groups):
        super().__init__(groups)

    

