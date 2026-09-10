import pygame
import sys
import math

# --- Initialization & Setup ---
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Beach Scene - Connected Waves")

# --- Color Palette ---
SKY_BLUE = (175, 215, 245)
SUN_GOLD = (255, 245, 200)
OCEAN_DEEP = (30, 80, 135)
TIDE_BLUE_DARK = (55, 115, 165)
TIDE_BLUE_LIGHT = (90, 150, 195)
WAVE_RIPPLE = (110, 170, 215) 
SAND_DRY = (225, 198, 153)
SAND_WET = (185, 156, 112)
CASTLE_SHADOW = (175, 148, 105) 
FOOTPRINT_COLOR = (155, 127, 85)

# Structural Colors
CLIFF_GRAY = (90, 95, 100)
LIGHTHOUSE_WHITE = (240, 240, 240)
LIGHTHOUSE_RED = (190, 40, 40)
LIGHTHOUSE_ROOF = (40, 40, 40)

# Main Loop Control
running = True

while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Sky and Sun
    screen.fill(SKY_BLUE)
    pygame.draw.circle(screen, SUN_GOLD, (120, 130), 45)

    # 2. Distant Ocean Base
    pygame.draw.rect(screen, OCEAN_DEEP, (0, 280, SCREEN_WIDTH, 120))

    # 3. Dry Beach Base Layer
    pygame.draw.rect(screen, SAND_DRY, (0, 380, SCREEN_WIDTH, 220))

    # 4. Rocky Cliff & Lighthouse Base (Pre-drawn layer)
    pygame.draw.polygon(screen, CLIFF_GRAY, [(650, 450), (800, 410), (800, 220), (710, 220), (670, 300)])

    # 5. Generative Tides & Waves (Calculated dynamically together to eliminate spaces)
    # Generate the exact points for the wave line first
    wave_points = []
    for x in range(0, SCREEN_WIDTH):
        if x < 600:
            base_y = 360 + (x * 0.11)
        else:
            base_y = 360 + (600 * 0.11) 

        wave_1 = math.sin(x * 0.05) * 6 
        wave_2 = math.cos(x * 0.2) * 2
        final_y = base_y + wave_1 + wave_2
        wave_points.append((x, final_y))

    # Wet Sand Layer
    wet_sand_poly = wave_points + [(800, 520), (540, 475), (280, 410), (0, 410)]
    pygame.draw.polygon(screen, SAND_WET, wet_sand_poly)
    
    # Dark Tide Layer (Offset slightly lower manually, or follows the main flow)
    dark_tide_poly = [(p[0], p[1] - 8) for p in wave_points] + [(800, 460), (0, 375)]
    pygame.draw.polygon(screen, TIDE_BLUE_DARK, dark_tide_poly)
    
    # Light Tide Layer (Connects directly underneath the ripple caps)
    light_tide_poly = wave_points + [(800, 452), (0, 367)]
    pygame.draw.polygon(screen, TIDE_BLUE_LIGHT, light_tide_poly)

    # Draw the capping ripple layer directly onto the top edge of the light blue polygon
    for x, final_y in wave_points:
        pygame.draw.line(screen, WAVE_RIPPLE, (x, int(final_y)), (x, int(final_y) + 4), 2)

    # 6. Footprints 
    footprints = [
        (100, 560), (115, 550), (140, 530), (155, 520), (185, 502), (200, 492),
        (230, 478), (245, 470), (280, 455), (295, 448), (335, 435), (350, 430),
        (395, 420), (410, 417), (460, 412), (475, 411), (525, 412), (540, 414),
        (595, 419), (610, 423), (660, 432), (672, 438)
    ]
    for pos in footprints:
        pygame.draw.ellipse(screen, FOOTPRINT_COLOR, (pos[0], pos[1], 10, 6))

    # 7. Sandcastle 
    sc_x, sc_y = 60, 450
    pygame.draw.rect(screen, SAND_DRY, (sc_x, sc_y, 110, 50))
    pygame.draw.rect(screen, CASTLE_SHADOW, (sc_x, sc_y, 110, 50), 2)
    
    for mx in range(sc_x + 5, sc_x + 105, 20):
        pygame.draw.rect(screen, SAND_DRY, (mx, sc_y - 10, 10, 10))
        pygame.draw.rect(screen, CASTLE_SHADOW, (mx, sc_y - 10, 10, 10), 2)
        pygame.draw.line(screen, SAND_DRY, (mx + 1, sc_y), (mx + 9, sc_y), 2)

    # Left Tower
    pygame.draw.rect(screen, SAND_DRY, (sc_x - 20, sc_y - 25, 25, 75))
    pygame.draw.rect(screen, CASTLE_SHADOW, (sc_x - 20, sc_y - 25, 25, 75), 2)
    pygame.draw.polygon(screen, SAND_DRY, [(sc_x - 20, sc_y - 25), (sc_x - 7, sc_y - 50), (sc_x + 5, sc_y - 25)])
    pygame.draw.polygon(screen, CASTLE_SHADOW, [(sc_x - 20, sc_y - 25), (sc_x - 7, sc_y - 50), (sc_x + 5, sc_y - 25)], 2)

    # Right Tower
    pygame.draw.rect(screen, SAND_DRY, (sc_x + 105, sc_y - 10, 25, 60))
    pygame.draw.rect(screen, CASTLE_SHADOW, (sc_x + 105, sc_y - 10, 25, 60), 2)

    # Center Keep
    pygame.draw.rect(screen, SAND_DRY, (sc_x + 35, sc_y - 40, 40, 40))
    pygame.draw.rect(screen, CASTLE_SHADOW, (sc_x + 35, sc_y - 40, 40, 40), 2)
    pygame.draw.rect(screen, CASTLE_SHADOW, (sc_x + 45, sc_y - 15, 20, 15))
    
    # Flag
    pygame.draw.line(screen, (100, 75, 45), (sc_x + 55, sc_y - 40), (sc_x + 55, sc_y - 65), 2) 
    pygame.draw.polygon(screen, (200, 70, 70), [(sc_x + 55, sc_y - 65), (sc_x + 75, sc_y - 58), (sc_x + 55, sc_y - 50)])

    # 8. Lighthouse Tower
    pygame.draw.rect(screen, LIGHTHOUSE_WHITE, (725, 120, 40, 100))
    pygame.draw.rect(screen, LIGHTHOUSE_RED, (725, 145, 40, 20))
    pygame.draw.rect(screen, LIGHTHOUSE_RED, (725, 185, 40, 20))
    pygame.draw.rect(screen, LIGHTHOUSE_ROOF, (720, 115, 50, 5))
    pygame.draw.rect(screen, LIGHTHOUSE_WHITE, (730, 95, 30, 20))
    pygame.draw.polygon(screen, LIGHTHOUSE_ROOF, [(725, 95), (745, 75), (765, 95)])
    
    # Light beam glow
    glow_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    pygame.draw.polygon(glow_surface, (255, 255, 170, 60), [(745, 105), (0, 120), (0, 260)])
    screen.blit(glow_surface, (0, 0))

    # Update Frame
    pygame.display.flip()

pygame.quit()
sys.exit()