import pygame,sys
from core import Engine,Menu
from entity import Snake,Food
from constants import *

# Initialize Pygame
pygame.init()

def main():
    e = Engine(600, 400,20)
    snake = Snake(e)
    food = Food(e)
    m = Menu(e,snake,food)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.direction = UP
                elif event.key == pygame.K_s:
                    snake.direction = DOWN
                elif event.key == pygame.K_a:
                    snake.direction = LEFT
                elif event.key == pygame.K_d:
                    snake.direction = RIGHT
                elif event.key == pygame.K_m:
                    m.toggle()

            elif event.type == pygame.VIDEORESIZE or event.type == pygame.VIDEOEXPOSE: #Handles window resizing
                i = pygame.display.Info()
                e.updateScreen(i.current_w, i.current_h)
                m.widgetsAdapt()

        if m.state:
            m.update(events)
            pygame.display.update()
            e.clock.tick(30)
        else:
            e.clock.tick(m.framesPerSecond.value)
            snake.update()

            # Check for collision with food
            if snake.get_head_position() == food.position:
                snake.length += 1
                food.randomize_position()

            e.surface.fill(BLACK)
            snake.render(e.surface)
            food.render(e.surface)

            e.screen.blit(e.surface, (0, 0))
            pygame.display.update()
        

if __name__ == "__main__":
    main()