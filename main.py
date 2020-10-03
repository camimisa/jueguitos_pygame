import pygame
import flappy_bird
import tateti

pygame.init()
run = True
W, H = 800, 600
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("MENU")
game_rect_pressed = False
game_font = pygame.font.Font('retro_computer_personal_use.ttf', 40)
game_font.set_bold(True)
white = (255, 255, 255)
color = (215, 16, 16)
# main menu


while run:
    window.fill((0, 0, 0))
    message_surface = game_font.render("CLASSIC GAMES", True, white)
    message_rect = message_surface.get_rect(center=(W // 2, H // 2))
    window.blit(message_surface, message_rect)
    listGamesIcons = [pygame.draw.rect(window, color, (200, 140, 100, 100)),
                      pygame.draw.rect(window, white, (310, 140, 100, 100)),
                      pygame.draw.rect(window, white, (420, 140, 100, 100)),
                      pygame.draw.rect(window, white, (530, 140, 100, 100)),
                      pygame.draw.rect(window, white, (240, 350, 100, 100)),
                      pygame.draw.rect(window, white, (350, 350, 100, 100)),
                      pygame.draw.rect(window, white, (460, 350, 100, 100))]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if listGamesIcons[0].collidepoint(pos):
                tateti.main_game()
                pygame.display.set_caption("MENU")
            if listGamesIcons[1].collidepoint(pos):
                flappy_bird.main_game()
                pygame.display.set_caption("MENU")
            if listGamesIcons[2].collidepoint(pos):
                print('Se presiono una tecla')
            if listGamesIcons[3].collidepoint(pos):
                print('Se presiono una tecla')
            if listGamesIcons[4].collidepoint(pos):
                print('Se presiono una tecla')
            if listGamesIcons[5].collidepoint(pos):
                print('Se presiono una tecla')
            if listGamesIcons[6].collidepoint(pos):
                print('Se presiono una tecla')
    pygame.display.update()

pygame.quit()
