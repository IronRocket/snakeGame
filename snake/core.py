import pygame,pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button




class Engine:
    def __init__(self,width:int,height:int,gridSize:int) -> None:
        self.width = width
        self.height = height
        self.gridSize = gridSize
        self.border = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE, 32)
        pygame.display.set_caption('Snake')
        self.surface = pygame.Surface(self.screen.get_size())


    def updateScreen(self,width:int,height:int) -> None:
        self.surface = pygame.Surface(self.screen.get_size())
        self.width = width
        self.height = height

class Menu:
    def __init__(self,engine:Engine,snake,food,fps=10,background=(70,70,70)) -> None:
        self.engine = engine
        self.state = True
        self.fps = fps
        self.background = background
        self.snake = snake
        self.food = food
        self.widgetsAdapt()

    def widgetsAdapt(self):
        Xmidpoint = self.engine.width//2
        resetWidth,resetHeight = self.engine.width//10,self.engine.height//10
        self.reset = Button(self.engine.screen,
            Xmidpoint-resetWidth//2,self.engine.height-resetHeight,
            resetWidth,resetHeight,

            text='Close',
            fontSize=20,
            margin=20,
            inactiveColour=(200, 50, 0),
            hoverColour=(150, 0, 0),
            pressedColour=(0, 200, 20),
            radius=20,
            onClick=lambda: self.toggle()
        )
        borderWidth,borderHeight = self.engine.width//7,self.engine.height//10
        self.borderButton = Button(self.engine.screen,
            self.engine.width-borderWidth,0,
            borderWidth,borderHeight,

            text='Border On',
            fontSize=20,
            margin=20,
            inactiveColour=(200, 50, 0),
            hoverColour=(150, 0, 0),
            pressedColour=(0, 200, 20),
            radius=20,
            onClick=lambda: self.toggleBorderCollision()
        )
        self.font = pygame.font.SysFont('Comic Sans MS', resetHeight//3)
        self.help = self.font.render('Press m to toggle menu', True, (0,0,0))
        self.r1 = self.help.get_rect()
        self.r1.y = self.engine.height-self.r1.height


        sliderWidth,sliderHeight = self.engine.width//6,self.engine.height//15
        
        self.font = pygame.font.SysFont('Comic Sans MS', sliderHeight)
        self.text = self.font.render(f'fps:', True, (0,0,0))
        self.textRect = self.text.get_rect()
        self.textRect.y = sliderHeight//4


        self.framesPerSecond = Slider(
            self.engine.screen, 
            self.textRect.width+sliderWidth//2, sliderHeight//2, 
            sliderWidth, sliderHeight, 
            min=10, max=30, step=1, 
            handleRadius=sliderHeight//2
        )
        self.framesPerSecond.setValue(self.fps)
        self.framesPerSecond._x = self.textRect.width+self.framesPerSecond._width

    def toggle(self)->None:
        self.state = not self.state

    def toggleBorderCollision(self)->None:
        if self.engine.border:
            self.borderButton.setText('Border Off')
            self.engine.border = False
        else:
            self.borderButton.setText('Border On')
            self.engine.border = True

    def getGrayGame(self)->pygame.Surface:
        men = pygame.Surface(self.engine.screen.get_size())
        men.set_alpha(50)
        self.snake.render(men)
        self.food.render(men)
        return men

    def update(self,events:pygame.event) -> None:
        self.text = self.font.render(f'speed:{self.framesPerSecond.value}', True, (0,0,0))
        h = self.textRect.y
        self.textRect = self.text.get_rect()
        self.textRect.y = h

        
        self.engine.surface.fill(self.background)

        self.engine.screen.blit(self.engine.surface, (0, 0))
        self.engine.screen.blit(self.getGrayGame(), (0, 0))
        self.engine.screen.blit(self.text,self.textRect)
        self.engine.screen.blit(self.help,self.r1)
        pygame_widgets.update(events)

