import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Rocket Drawing
def draw_rocket(x, y):
    glColor3f(1, 1, 0)  # Yellow color
    glBegin(GL_TRIANGLES)
    # Rocket Head
    glVertex2f(x, y + 0.1)
    glVertex2f(x - 0.05, y)
    glVertex2f(x + 0.05, y)
    glEnd()
    glBegin(GL_QUADS)
    # Rocket Body
    glVertex2f(x - 0.025, y)
    glVertex2f(x - 0.025, y - 0.15)
    glVertex2f(x + 0.025, y - 0.15)
    glVertex2f(x + 0.025, y)
    glEnd()

# Bullet Drawing
def draw_bullet(x, y):
    glColor3f(1, 1, 1)  # White color
    glBegin(GL_QUADS)
    glVertex2f(x - 0.01, y)
    glVertex2f(x - 0.01, y + 0.05)
    glVertex2f(x + 0.01, y + 0.05)
    glVertex2f(x + 0.01, y)
    glEnd()

# Circle Target
def draw_circle(x, y, radius):
    glColor3f(1, 0, 0)  # Red color
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for angle in range(361):
        angle_rad = angle * 3.14159 / 180
        glVertex2f(x + radius * cos(angle_rad), y + radius * sin(angle_rad))
    glEnd()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluOrtho2D(-1, 1, -1, 1)

    # Rocket position
    rocket_x = 0
    rocket_y = -0.8

    # Bullets and targets
    bullets = []
    targets = [{"x": random.uniform(-0.9, 0.9), "y": 1, "radius": 0.05} for _ in range(5)]
    clock = pygame.time.Clock()

    while True:
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw rocket
        draw_rocket(rocket_x, rocket_y)

        # Draw bullets
        for bullet in bullets:
            bullet["y"] += 0.02  # Move bullets upward
            draw_bullet(bullet["x"], bullet["y"])

        # Remove bullets off-screen
        bullets = [bullet for bullet in bullets if bullet["y"] <= 1]

        # Draw targets
        for target in targets:
            target["y"] -= 0.005  # Move targets downward
            draw_circle(target["x"], target["y"], target["radius"])

        # Collision detection
        for bullet in bullets:
            for target in targets:
                if (
                    target["x"] - target["radius"] <= bullet["x"] <= target["x"] + target["radius"]
                    and target["y"] - target["radius"] <= bullet["y"] <= target["y"] + target["radius"]
                ):
                    targets.remove(target)
                    bullets.remove(bullet)
                    break

        # Add new targets
        if len(targets) < 5:
            targets.append({"x": random.uniform(-0.9, 0.9), "y": 1, "radius": 0.05})

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    rocket_x -= 0.1
                elif event.key == K_RIGHT:
                    rocket_x += 0.1
                elif event.key == K_SPACE:
                    bullets.append({"x": rocket_x, "y": rocket_y + 0.1})

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
