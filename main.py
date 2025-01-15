import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
TARGET_RADIUS = 30
TARGET_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

# Настройка окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир")

# Функция для создания мишени
def create_target():
    x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
    y = random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS)
    return (x, y)

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    score = 0
    target = create_target()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                target_x, target_y = target
                if (mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2 <= TARGET_RADIUS ** 2:
                    score += 1
                    target = create_target()

        # Отрисовка
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.circle(screen, TARGET_COLOR, target, TARGET_RADIUS)
        
        # Отображение счета
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()