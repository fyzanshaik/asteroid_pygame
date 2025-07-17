import pygame 

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
        
    
    # def radius(self,screen):
    #     pass
    
    def update(self,dt):
        pass
    
    def checkCollision(self,other):
        distance = self.position.distance_to(other.position)
        r1 = self.radius
        r2 = other.radius
        
        return distance < (r1+r2)