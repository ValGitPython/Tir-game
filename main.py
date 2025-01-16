import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
TARGET_RADIUS = 30
TARGET_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (246, 246,246)
FPS = 60

# Настройка окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир")

# Функция для создания мишени
def create_target():
    x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
    y = random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS)
    return (x, y)

# Основная функция игры
def main():
    clock = pygame.time.Clock()
    target = create_target()
    score = 0
    shots = 0  # Счетчик выстрелов
    hits = 0   # Счетчик попаданий

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:


                # Звук выстрела
                pygame.mixer.music.load('img/pistol-shot.mp3')
                pygame.mixer.music.play(0)


                shots += 1  # Увеличиваем счетчик выстрелов
                mouse_x, mouse_y = event.pos
                # Проверка попадания по мишени
                if (mouse_x - target[0]) ** 2 + (mouse_y - target[1]) ** 2 <= TARGET_RADIUS ** 2:
                    hits += 1
                    score += 1
                    target = create_target()  # Создаем новую мишень

        # Отрисовка
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.circle(screen, TARGET_COLOR, target, TARGET_RADIUS)
        
        # Отображение счета, выстрелов и процента попаданий
        font = pygame.font.Font(None, 36)
        
        # Счет
        score_text = font.render(f"Счет: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        
        # Выстрелы
        shots_text = font.render(f"Выстрелы: {shots}", True, (0, 0, 0))
        screen.blit(shots_text, (10, 50))
        
        # Процент попаданий
        if shots > 0:
            accuracy = (hits / shots) * 100
        else:
            accuracy = 0
        accuracy_text = font.render(f"Попадания: {accuracy:.2f}%", True, (0, 0, 0))
        screen.blit(accuracy_text, (10, 90))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()