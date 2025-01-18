# This program is created by ChatGPT

import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Scrollable Font Preview')

# List of fonts to preview
font_names = [
    'arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath', 'candara', 'comicsansms', 'consolas',
    'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact',
    'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic',
    'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhenghei', 'microsoftjhengheiui', 'microsoftnewtailue',
    'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyahei', 'microsoftyaheiui', 'microsoftyibaiti',
    'mingliuextb', 'pmingliuextb', 'mingliuhkscsextb', 'mongolianbaiti', 'msgothic', 'msuigothic', 'mspgothic', 'mvboli',
    'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoeprint', 'segoescript',
    'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol',
    'simsun', 'nsimsun', 'simsunextb', 'sitkasmall', 'sitkatext', 'sitkasubheading', 'sitkaheading', 'sitkadisplay',
    'sitkabanner', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings',
    'yugothic', 'yugothicuisemibold', 'yugothicui', 'yugothicmedium', 'yugothicuiregular', 'yugothicregular', 
    'yugothicuisemilight', 'kartika', 'cascadiacoderegular', 'cascadiamonoregular'
]

# Font size
font_size = 24

# Create font objects
fonts = []
for font_name in font_names:
    try:
        fonts.append(pygame.font.SysFont(font_name, font_size))
    except:
        fonts.append(None)

# Scroll variables
scroll_y = 0
scroll_speed = 50
list_height = len(fonts) * (font_size + 10)  # Height of the entire list (each font + padding)
scroll_area_height = screen_height - 40  # Height of the scrollable area
is_scrolling = False
mouse_y_start = 0

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse wheel scrolling
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                scroll_y -= scroll_speed
            elif event.button == 5:  # Scroll down
                scroll_y += scroll_speed

        # Mouse drag scrolling
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            is_scrolling = True
            mouse_y_start = event.pos[1]

        if event.type == pygame.MOUSEMOTION and is_scrolling:
            delta_y = event.pos[1] - mouse_y_start
            scroll_y -= delta_y
            mouse_y_start = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_scrolling = False

    # Prevent scrolling out of bounds
    scroll_y = max(scroll_y, 0)
    scroll_y = min(scroll_y, list_height - scroll_area_height)

    # Draw the list of fonts
    for i, font in enumerate(fonts):
        if font is not None:
            font_surface = font.render(f"Preview of {font_names[i]}", True, (0, 0, 0))
            font_rect = font_surface.get_rect(topleft=(20, 20 + i * (font_size + 10) - scroll_y))
            screen.blit(font_surface, font_rect)

    # Update display
    pygame.display.flip()

    # Limit FPS
    pygame.time.Clock().tick(60)

pygame.quit()
