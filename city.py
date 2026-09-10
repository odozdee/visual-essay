import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("City - Community")

# Clock to control frame rate
clock = pygame.time.Clock()

# Colors (RGB)
SKY_BLUE = (135, 206, 235)
GROUND_GRAY = (80, 80, 80)
SIDEWALK_GRAY = (160, 160, 160)
CITY_HALL_COLOR = (120, 140, 160)
ROOF_COLOR = (180, 50, 50)
HOUSE_COLOR = (210, 180, 140)
DOOR_VOID = (30, 20, 10)  # Dark inside for open door
YELLOW = (255, 255, 0)
LAMP_POST = (40, 40, 40)
LAMP_GLOW = (255, 255, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Traffic light variables for the "broken" effect
flash_timer = 0
traffic_light_on = True

# Main game loop
running = True
while running:
    # 1. Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update Logic (Broken traffic light timer)
    flash_timer += clock.get_rawtime()
    if flash_timer > 400:  # Switch state every 400 milliseconds
        traffic_light_on = not traffic_light_on
        flash_timer = 0

    # 3. Drawing the Scene
    # Sky
    screen.fill(SKY_BLUE)

    # Road and Sidewalk
    pygame.draw.rect(screen, GROUND_GRAY, (0, 480, SCREEN_WIDTH, 120))
    pygame.draw.rect(screen, SIDEWALK_GRAY, (0, 450, SCREEN_WIDTH, 30))
    # Road lines
    for x in range(10, SCREEN_WIDTH, 80):
        pygame.draw.rect(screen, YELLOW, (x, 530, 40, 10))

    # --- CITY HALL ---
    # Main structure
    pygame.draw.rect(screen, CITY_HALL_COLOR, (50, 180, 300, 270))
    # Roof triangle
    pygame.draw.polygon(screen, ROOF_COLOR, [(50, 180), (200, 100), (350, 180)])
    # Pillars
    for x_offset in [70, 140, 210, 280]:
        pygame.draw.rect(screen, (200, 210, 220), (x_offset, 240, 30, 210))
    # City Hall Door
    pygame.draw.rect(screen, (100, 60, 30), (160, 370, 80, 80))

    # --- HOUSE WITH OPEN DOOR ---
    # Main structure
    pygame.draw.rect(screen, HOUSE_COLOR, (450, 250, 200, 200))
    # Roof
    pygame.draw.polygon(screen, ROOF_COLOR, [(430, 250), (550, 160), (670, 250)])
    # Windows
    pygame.draw.rect(screen, SKY_BLUE, (480, 280, 40, 40))
    pygame.draw.rect(screen, SKY_BLUE, (580, 280, 40, 40))
    # Open Door (Dark inside interior, door swung open to the side)
    pygame.draw.rect(screen, DOOR_VOID, (525, 350, 50, 100))  # The open doorway
    pygame.draw.rect(screen, (139, 69, 19), (490, 350, 35, 100))  # The door panel swung open

    # --- STREET LAMP ---
    # Post
    pygame.draw.rect(screen, LAMP_POST, (400, 220, 10, 230))
    # Arm
    pygame.draw.rect(screen, LAMP_POST, (370, 220, 40, 10))
    # Lantern
    pygame.draw.rect(screen, LAMP_POST, (365, 230, 20, 15))
    # Light Glow (Yellow polygon simulating light casting down)
    lamp_glow_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    pygame.draw.polygon(lamp_glow_surface, (255, 255, 150, 80), [(375, 245), (320, 450), (430, 450)])
    screen.blit(lamp_glow_surface, (0, 0))

    # --- BROKEN TRAFFIC LIGHT ---
    # Post
    pygame.draw.rect(screen, BLACK, (710, 280, 10, 170))
    # Box
    pygame.draw.rect(screen, BLACK, (695, 200, 40, 80))
    
    # Red light (Broken/Blinking)
    if traffic_light_on:
        pygame.draw.circle(screen, RED, (715, 220), 10)
    else:
        pygame.draw.circle(screen, (50, 0, 0), (715, 220), 10) # Dull red when off
        
    # Other dead lights (Yellow and Green are completely broken/off)
    pygame.draw.circle(screen, (50, 50, 0), (715, 240), 10)
    pygame.draw.circle(screen, (0, 50, 0), (715, 260), 10)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()