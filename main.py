# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    pygame.font.init
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_text(screen, text, pos, font_size, color, font):
    font = pygame.font.Font(font , font_size)
    display_text = font.render(str(text), True, color)
    screen.blit(display_text, (pos))

def draw_rect(screen, color, x, y, width, height, thickness):
    pygame.draw.rect(screen, color, (x, y, width, height), thickness)



def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here

    text1 = 'PJ VanDussen'
    text2 = 'Career Tech'
    text3 = 'This is bouncy'

    x1 = 125
    y1 = 40
    

    
    square_x = 10
    square_y = 20
    square_change_x = 10
    square_change_y = 15


    running = True
    while running:
        running = handle_events()
        screen.fill(config.GREEN) # Use color from config
        mouse_pos = pygame.mouse.get_pos()
        draw_text(screen, mouse_pos, mouse_pos, 15, config.BLACK, 'c:\Font\BigShouldersInline-VariableFont_opsz,wght.ttf') # Tells user mouse coordinates
        
        draw_rect(screen, config.WHITE, square_x, square_y, 50, 50, thickness=0)

        draw_text(screen, text1, (x1, y1), 50, config.BLUE, 'c:\Font\EmblemaOne-Regular.ttf')
        draw_text(screen, text2, (x1, 80), 50, config.PURPLE, 'c:\Font\RubikGlitch-Regular.ttf')
        draw_text(screen, text3, (x1, 120), 50, config.PINK, 'c:\Font\Tektur-VariableFont_wdth,wght.ttf')

        
        square_x = square_x + square_change_x
        square_y = square_y + square_change_y

        if square_x >  750 or square_x < 0:
            square_change_x = square_change_x * -1
        else:
            square_change_x += 5
        if square_y > 550 or square_y < 0:
            square_change_y = square_change_y * -1
        # else:
        #     square_change_y += 5
            
        
        

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



