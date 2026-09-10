import pygame
import sys
import math

# --- Initialization & Setup ---
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Five Little Indians Visual Essay")

clock = pygame.time.Clock()

# --- Shared Color Palette ---
SKY_BLUE = (135, 206, 235)
BEACH_SKY_BLUE = (175, 215, 245)
SUN_GOLD = (255, 245, 200)
OCEAN_DEEP = (30, 80, 135)
TIDE_BLUE_DARK = (55, 115, 165)
TIDE_BLUE_LIGHT = (90, 150, 195)
WAVE_RIPPLE = (110, 170, 215) 
SAND_DRY = (225, 198, 153)
SAND_WET = (185, 156, 112)
CASTLE_SHADOW = (175, 148, 105) 
FOOTPRINT_COLOR = (155, 127, 85)
CLIFF_GRAY = (90, 95, 100)
LIGHTHOUSE_WHITE = (240, 240, 240)
LIGHTHOUSE_RED = (190, 40, 40)
LIGHTHOUSE_ROOF = (40, 40, 40)

GROUND_GRAY = (80, 80, 80)
SIDEWALK_GRAY = (160, 160, 160)
CITY_HALL_COLOR = (120, 140, 160)
ROOF_COLOR = (180, 50, 50)
HOUSE_COLOR = (210, 180, 140)
DOOR_VOID = (30, 20, 10)
YELLOW = (255, 255, 0)
LAMP_POST = (40, 40, 40)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

NATURE_SKY = (140, 180, 210)
FOREST_DARK = (20, 50, 25)
FOREST_LIGHT = (35, 75, 45)
LEAF_GREEN = (40, 90, 45)
OLD_LEAF_GREEN = (30, 70, 35)
TRUNK_BROWN = (85, 55, 30)
RIVER_BLUE = (45, 95, 150)
RIVER_MID = (65, 120, 180)
RIVER_LIGHT = (95, 150, 210)

# Text Screen Colors
TEXT_BG = (25, 35, 45)
TEXT_WHITE = (240, 240, 240)
TEXT_GOLD = (230, 185, 85)

# --- Fonts ---
font_title = pygame.font.SysFont("georgia", 48)
font_body = pygame.font.SysFont("arial", 24)

# --- Navigation & Logic State ---
# 0: Title, 1: Theme, 2: City, 3: Nature, 4: Beach, 5: The End
current_state = 0  
TOTAL_STATES = 6

# Traffic Light Variables
flash_timer = 0
traffic_light_on = True

# --- Helper Function for Text Wrapping ---
def render_wrapped_text(surface, text, font, color, rect, line_spacing=5):
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < rect.width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    
    y = rect.top
    for line in lines:
        text_surf = font.render(line.strip(), True, color)
        surface.blit(text_surf, (rect.left, y))
        y += font.size(line)[1] + line_spacing

#MAIN LOOP
running = True
while running:
    # Frame delta time for city animations
    dt = clock.tick(60)
    
    # 1. Universal Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if current_state < TOTAL_STATES - 1:
                    current_state += 1
            elif event.key == pygame.K_LEFT:
                if current_state > 0:
                    current_state -= 1

    # 2. Update Logic (Blinking Traffic Light)
    if current_state == 2:
        flash_timer += dt
        if flash_timer > 400:
            traffic_light_on = not traffic_light_on
            flash_timer = 0

    # 3. Scene Rendering based on State
    if current_state == 0:
        # TITLE SCREEN
        screen.fill(TEXT_BG)
        title_surf = font_title.render("Five Little Indians Visual Essay", True, TEXT_GOLD)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(title_surf, title_rect)

    elif current_state == 1:
        # THEME SCREEN
        screen.fill(TEXT_BG)
        
        theme_title = font_title.render("THEME", True, TEXT_GOLD)
        screen.blit(theme_title, (80, 120))
        
        theme_text = (
            "Healing from trauma can be achieved through supporting each other "
            "as a community, reconnecting with culture, and finding a purpose in life."
        )
        text_box = pygame.Rect(80, 220, 640, 300)
        render_wrapped_text(screen, theme_text, font_body, TEXT_WHITE, text_box, line_spacing=8)

    elif current_state == 2:
        # CITY SCREEN
        screen.fill(SKY_BLUE)

        # Road and Sidewalk
        pygame.draw.rect(screen, GROUND_GRAY, (0, 480, SCREEN_WIDTH, 120))
        pygame.draw.rect(screen, SIDEWALK_GRAY, (0, 450, SCREEN_WIDTH, 30))
        for x in range(10, SCREEN_WIDTH, 80):
            pygame.draw.rect(screen, YELLOW, (x, 530, 40, 10))

        # City Hall
        pygame.draw.rect(screen, CITY_HALL_COLOR, (50, 180, 300, 270))
        pygame.draw.polygon(screen, ROOF_COLOR, [(50, 180), (200, 100), (350, 180)])
        for x_offset in [70, 140, 210, 280]:
            pygame.draw.rect(screen, (200, 210, 220), (x_offset, 240, 30, 210))
        pygame.draw.rect(screen, (100, 60, 30), (160, 370, 80, 80))

        # House
        pygame.draw.rect(screen, HOUSE_COLOR, (450, 250, 200, 200))
        pygame.draw.polygon(screen, ROOF_COLOR, [(430, 250), (550, 160), (670, 250)])
        pygame.draw.rect(screen, SKY_BLUE, (480, 280, 40, 40))
        pygame.draw.rect(screen, SKY_BLUE, (580, 280, 40, 40))
        pygame.draw.rect(screen, DOOR_VOID, (525, 350, 50, 100))
        pygame.draw.rect(screen, (139, 69, 19), (490, 350, 35, 100))

        # Street Lamp
        pygame.draw.rect(screen, LAMP_POST, (400, 220, 10, 230))
        pygame.draw.rect(screen, LAMP_POST, (370, 220, 40, 10))
        pygame.draw.rect(screen, LAMP_POST, (365, 230, 20, 15))
        lamp_glow_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        pygame.draw.polygon(lamp_glow_surface, (255, 255, 150, 80), [(375, 245), (320, 450), (430, 450)])
        screen.blit(lamp_glow_surface, (0, 0))

        # Broken Traffic Light
        pygame.draw.rect(screen, BLACK, (710, 280, 10, 170))
        pygame.draw.rect(screen, BLACK, (695, 200, 40, 80))
        if traffic_light_on:
            pygame.draw.circle(screen, RED, (715, 220), 10)
        else:
            pygame.draw.circle(screen, (50, 0, 0), (715, 220), 10)
        pygame.draw.circle(screen, (50, 50, 0), (715, 240), 10)
        pygame.draw.circle(screen, (0, 50, 0), (715, 260), 10)

    elif current_state == 3:
        # NATURE SCREEN
        screen.fill(NATURE_SKY)

        # Forest Background
        pygame.draw.rect(screen, FOREST_DARK, (0, 200, SCREEN_WIDTH, 400))
        for x in range(0, SCREEN_WIDTH, 40):
            pygame.draw.polygon(screen, FOREST_DARK, [(x, 200), (x + 30, 130), (x + 60, 200)])
        
        pygame.draw.rect(screen, FOREST_LIGHT, (0, 280, SCREEN_WIDTH, 320))
        for x in range(-20, SCREEN_WIDTH, 50):
            pygame.draw.polygon(screen, FOREST_LIGHT, [(x, 280), (x + 40, 180), (x + 80, 280)])

        # River
        river_points = [
            ((460, 280), (480, 280)), ((440, 310), (465, 310)), ((410, 340), (440, 340)),
            ((390, 370), (425, 370)), ((400, 400), (445, 400)), ((440, 430), (495, 430)),
            ((500, 470), (570, 470)), ((560, 510), (650, 510)), ((580, 550), (700, 550)),
            ((540, 600), (720, 600))
        ]

        for i in range(len(river_points) - 1):
            p1_left, p1_right = river_points[i]
            p2_left, p2_right = river_points[i+1]
            
            pygame.draw.polygon(screen, RIVER_BLUE, [p1_left, p1_right, p2_right, p2_left])
            
            m1_left = (p1_left[0] + 5, p1_left[1])
            m1_right = (p1_right[0] - 5, p1_right[1])
            m2_left = (p2_left[0] + 8, p2_left[1])
            m2_right = (p2_right[0] - 8, p2_right[1])
            pygame.draw.polygon(screen, RIVER_MID, [m1_left, m1_right, m2_right, m2_left])

            h1_left = (p1_left[0] + 12, p1_left[1])
            h1_right = (p1_right[0] - 12, p1_right[1])
            h2_left = (p2_left[0] + 16, p2_left[1])
            h2_right = (p2_right[0] - 16, p2_right[1])
            pygame.draw.polygon(screen, RIVER_LIGHT, [h1_left, h1_right, h2_right, h2_left])

        # Old Growth Tree
        pygame.draw.polygon(screen, TRUNK_BROWN, [(80, 600), (160, 350), (240, 350), (320, 600)])
        pygame.draw.rect(screen, TRUNK_BROWN, (160, 300, 80, 100))
        pygame.draw.line(screen, TRUNK_BROWN, (160, 330), (80, 260), 30)
        pygame.draw.line(screen, TRUNK_BROWN, (240, 330), (320, 250), 25)
        pygame.draw.line(screen, TRUNK_BROWN, (200, 300), (200, 200), 35)

        pygame.draw.circle(screen, OLD_LEAF_GREEN, (80, 240), 75)
        pygame.draw.circle(screen, OLD_LEAF_GREEN, (320, 230), 80)
        pygame.draw.circle(screen, OLD_LEAF_GREEN, (200, 160), 100)
        
        pygame.draw.circle(screen, LEAF_GREEN, (110, 220), 65)
        pygame.draw.circle(screen, LEAF_GREEN, (290, 210), 70)
        pygame.draw.circle(screen, LEAF_GREEN, (200, 130), 85)
        pygame.draw.circle(screen, LEAF_GREEN, (150, 100), 60)
        pygame.draw.circle(screen, LEAF_GREEN, (250, 100), 60)

    elif current_state == 4:
        # BEACH SCREEN
        screen.fill(BEACH_SKY_BLUE)
        pygame.draw.circle(screen, SUN_GOLD, (120, 130), 45)

        # Distant Ocean Base
        pygame.draw.rect(screen, OCEAN_DEEP, (0, 280, SCREEN_WIDTH, 120))

        # Dry Beach Base Layer
        pygame.draw.rect(screen, SAND_DRY, (0, 380, SCREEN_WIDTH, 220))

        # Rocky Cliff & Lighthouse Base
        pygame.draw.polygon(screen, CLIFF_GRAY, [(650, 450), (800, 410), (800, 220), (710, 220), (670, 300)])

        # Generative Tides & Waves
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
        
        # Dark Tide Layer
        dark_tide_poly = [(p[0], p[1] - 8) for p in wave_points] + [(800, 460), (0, 375)]
        pygame.draw.polygon(screen, TIDE_BLUE_DARK, dark_tide_poly)
        
        # Light Tide Layer
        light_tide_poly = wave_points + [(800, 452), (0, 367)]
        pygame.draw.polygon(screen, TIDE_BLUE_LIGHT, light_tide_poly)

        # Capping ripples
        for x, final_y in wave_points:
            pygame.draw.line(screen, WAVE_RIPPLE, (x, int(final_y)), (x, int(final_y) + 4), 2)

        # Footprints 
        footprints = [
            (100, 560), (115, 550), (140, 530), (155, 520), (185, 502), (200, 492),
            (230, 478), (245, 470), (280, 455), (295, 448), (335, 435), (350, 430),
            (395, 420), (410, 417), (460, 412), (475, 411), (525, 412), (540, 414),
            (595, 419), (610, 423), (660, 432), (672, 438)
        ]
        for pos in footprints:
            pygame.draw.ellipse(screen, FOOTPRINT_COLOR, (pos[0], pos[1], 10, 6))

        # Sandcastle 
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
        
        # Sandcastle Flag
        pygame.draw.line(screen, (100, 75, 45), (sc_x + 55, sc_y - 40), (sc_x + 55, sc_y - 65), 2) 
        pygame.draw.polygon(screen, (200, 70, 70), [(sc_x + 55, sc_y - 65), (sc_x + 75, sc_y - 58), (sc_x + 55, sc_y - 50)])

        # Lighthouse
        pygame.draw.rect(screen, LIGHTHOUSE_WHITE, (725, 120, 40, 100))
        pygame.draw.rect(screen, LIGHTHOUSE_RED, (725, 145, 40, 20))
        pygame.draw.rect(screen, LIGHTHOUSE_RED, (725, 185, 40, 20))
        pygame.draw.rect(screen, LIGHTHOUSE_ROOF, (720, 115, 50, 5))
        pygame.draw.rect(screen, LIGHTHOUSE_WHITE, (730, 95, 30, 20))
        pygame.draw.polygon(screen, LIGHTHOUSE_ROOF, [(725, 95), (745, 75), (765, 95)])
        
        # Light
        glow_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        pygame.draw.polygon(glow_surface, (255, 255, 170, 60), [(745, 105), (0, 120), (0, 260)])
        screen.blit(glow_surface, (0, 0))

    elif current_state == 5:
        # END SCREEN
        screen.fill(TEXT_BG)
        
        end_surf = font_title.render("The End", True, TEXT_GOLD)
        end_rect = end_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(end_surf, end_rect)

    # Update Display Surface
    pygame.display.flip()

pygame.quit()
sys.exit()