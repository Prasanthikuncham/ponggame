import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = 5 * (-1) ** (pygame.time.get_ticks() % 2)  # Random initial direction
        self.speed_y = 5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y = -self.speed_y

        # Reset ball when it goes out of bounds
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.reset()

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = 5 * (-1) ** (pygame.time.get_ticks() % 2)
        self.speed_y = 5

# Paddle class
class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[down] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

# Main game loop
def main():
    clock = pygame.time.Clock()
    ball = Ball()
    player1 = Paddle(30)
    player2 = Paddle(WIDTH - 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move paddles
        player1.move(pygame.K_w, pygame.K_s)
        player2.move(pygame.K_UP, pygame.K_DOWN)

        # Move ball
        ball.move()

        # Ball collision with paddles
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            ball.speed_x = -ball.speed_x

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw everything
        pygame.draw.ellipse(screen, WHITE, ball.rect)
        pygame.draw.rect(screen, WHITE, player1.rect)
        pygame.draw.rect(screen, WHITE, player2.rect)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
