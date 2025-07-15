import pygame

pygame.font.init()
font = pygame.font.Font(None, 20)

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onClickFuntion=None, onPress=False):
    
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttonText = buttonText
        self.onClickFuntion = onClickFuntion
        self.onPress = onPress
        self.alreadyPressed = False
        
        self.fillColors = {
                'normal': '#ffffff',
                'hover': '#666666',
                'pressed': '#333333',
                }

        #self.buttonSurface = pygame.Surface((width, height))
        #self.buttonRect = pygame.Rect((x, y, width, height))
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        needed_width = self.buttonSurf.get_rect().width + 20
        needed_height = self.buttonSurf.get_rect().height + 10

        required_width = needed_width if width <= needed_width else width 
        required_height = needed_height if height <= needed_height else height 
        
        self.buttonSurface = pygame.Surface((required_width, required_height))
        self.buttonRect = pygame.Rect((x, y, required_width, required_height))


    def process(self, screen):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onPress:
                    self.onClickFuntion()
                elif not self.alreadyPressed:
                    self.onClickFuntion()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False


        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
            ])
        screen.blit(self.buttonSurface, self.buttonRect)

