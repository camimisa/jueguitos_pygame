import pygame
import random


class FlappyBird:
    run = True
    W, H = 400, 700
    window = pygame.display.set_mode((W, H))
    pygame.display.set_caption("FLAPPY BIRD")
    clock = pygame.time.Clock()

    # Game variables
    gravity = 0.25
    bird_movement = 0
    game_active = True

    bg_surface = pygame.image.load('flappy_bird_files/sprites/background-day.png').convert()
    bg_surface = pygame.transform.scale(bg_surface, (W, H))

    floor_surface = pygame.image.load('flappy_bird_files/sprites/base.png').convert()
    floor_surface = pygame.transform.scale(floor_surface, (W, 100))
    floor_x_pos = 0

    bird_surface = pygame.image.load('flappy_bird_files/sprites/yellowbird-midflap.png').convert()
    bird_surface = pygame.transform.scale(bird_surface, (50, 40))
    bird_rect = bird_surface.get_rect(center=(50, H / 2))

    pipe_surface = pygame.image.load('flappy_bird_files/sprites/pipe-green.png').convert()
    pipe_surface = pygame.transform.scale2x(pipe_surface)
    pipe_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1200)
    pipe_height = [250, 300, 350, 400, 450, 550]

    def main_flappy_bird(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_active:
                        self.bird_movement = 0
                        self.bird_movement -= 10
                    if event.key == pygame.K_SPACE and not self.game_active:
                        self.game_active = True
                        self.pipe_list.clear()
                        self.bird_rect.center = (50, self.H / 2)
                        self.bird_movement = 0
                if event.type == self.SPAWNPIPE:
                    self.pipe_list.extend(self.create_pipe())

            self.window.blit(self.bg_surface, (0, 0))
            if self.game_active:
                # Bird
                self.bird_movement += self.gravity
                self.bird_rect.centery += self.bird_movement
                self.window.blit(self.bird_surface, self.bird_rect)
                self.game_active = self.check_collision(self.pipe_list)

                # Pipes
                self.pipe_list = self.move_pipes(self.pipe_list)
                self.draw_pipes(self.pipe_list)

            # Floor
            self.floor_x_pos -= 1
            self.draw_floor()
            pygame.display.update()
            self.clock.tick(80)

    def draw_floor(self):
        self.window.blit(self.floor_surface, (self.floor_x_pos, self.H - 60))
        self.window.blit(self.floor_surface, (self.floor_x_pos + self.W, self.H - 60))
        if self.floor_x_pos <= -self.W:
            self.floor_x_pos = 0

    def create_pipe(self):
        random_pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe_surface.get_rect(midtop=(self.W + 200, random_pipe_pos))
        top_pipe = self.pipe_surface.get_rect(midbottom=(self.W + 200, random_pipe_pos - 200))
        return bottom_pipe, top_pipe

    def move_pipes(self, pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        return pipes

    def draw_pipes(self, pipes):
        for pipe in pipes:
            if pipe.bottom >= self.H:
                self.window.blit(self.pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
                self.window.blit(flip_pipe, pipe)

    def check_collision(self, pipes):
        for pipe in pipes:
            if self.bird_rect.colliderect(pipe):
                return False

        if self.bird_rect.top <= -50 or self.bird_rect.bottom >= self.H - 60:
            return False

        return True


# main
pygame.init()
juego2 = FlappyBird()
juego2.main_flappy_bird()
pygame.quit()
