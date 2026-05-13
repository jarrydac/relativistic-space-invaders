from pygame.sprite import Sprite as PygameSprite

class GL_Sprite(PygameSprite):
    def __init__(self,*groups):
        super().__init__(groups)
        self.mesh = None
    

