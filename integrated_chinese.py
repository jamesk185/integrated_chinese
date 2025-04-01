# Author: James Kowalik
# Created: 25/03/25
# Revised: 
# Description: 

import pygame
import os
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600  # Adjust as needed
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Image Viewer")
font = pygame.font.Font(None, 120)

# Load images from the "images" folder
IMAGE_FOLDER = "images"  # Change this to your image folder path
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif"))]

if not image_files:
	print("No images found in the folder!")
	pygame.quit()
	exit()

# Function to load and scale an image
def load_random_image():
	img_path = os.path.join(IMAGE_FOLDER, random.choice(image_files))
	image = pygame.image.load(img_path)
	scale = max(image.get_width()/WIDTH, image.get_height()/HEIGHT)
	return pygame.transform.scale(image, (image.get_width()/scale, image.get_height()/scale))

# Load the first image
current_image = load_random_image()

# Main loop
running = True
count = 1
while running:
	screen.fill((0, 0, 0))  # Clear screen
	
	if count % 2:
		# Show question mark
		text_surface = font.render("?", True, (255, 255, 255))  # White question mark
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	else:
		# Show image
		img_rect = current_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(current_image, img_rect.topleft)
	
	pygame.display.flip()  # Update display
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				count += 1
				if count % 2 == 0:
					current_image = load_random_image()
			elif event.key == pygame.K_RETURN:
				running = False

# Quit pygame
pygame.quit()
