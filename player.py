import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_MAX_LIVES,SCREEN_HEIGHT,SCREEN_WIDTH

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.score = 0
        self.lives = PLAYER_MAX_LIVES
    
    def centerPosition(self):
        self.position.x = SCREEN_WIDTH/2
        self.position.y = SCREEN_HEIGHT/2
            
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation+90) * self.radius / 1.5
        a = self.position + forward *self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]
    
    def draw(self,screen):
        color = "green"
        points = self.triangle()
        line_width = 2
        pygame.draw.polygon(screen,color=color,points=points,width=line_width)
        
    def rotate(self,dt):
        print(f"Delta time: {dt}, current rotation: {self.rotation}")
        self.rotation += PLAYER_TURN_SPEED * dt
        print(f"Updated rotation: {self.rotation}")
        
    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        print(f"Forward vector: {forward}, position: {self.position}")
        self.position += forward * PLAYER_SPEED * dt
        print(f"Position update: {self.position}")
    
    def shoot(self):
        if self.shoot_timer <= 0:
            shot = Shot(self.position.x,self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        
    
    def update(self,dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)
            
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_w]:
            self.move(dt) 
        
        if keys[pygame.K_SPACE]:
            self.shoot()