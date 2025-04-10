# Author: James Kowalik
# Created: 25/04/04
# Revised: 25/04/07
# Description: Integrated Chinese lesson 02 question 01

import pygame
import os
import random
import sys

IMAGE_FOLDER = sys.argv[1]
exercise_choice = sys.argv[2]

# === PYGAME SETUP ===

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Integrated Chinese Lesson 02 Exercise 01")

l02_q02 = {"01": "elder_brother", "02": "mum", "03": "dad", "04": "son", "05": "daughter"}

def choose_random():
	img_id = random.choice(list(l02_q02.keys()))
	demon = random.choice(["this", "that"])
	return img_id, demon

def load_image(img_id):
	img_path = os.path.join(IMAGE_FOLDER, [x for x in image_files if "_" + img_id in x][0])
	image = pygame.image.load(img_path)
	scale = max(image.get_width()/WIDTH, image.get_height()/HEIGHT)
	return pygame.transform.scale(image, (image.get_width()/scale, image.get_height()/scale))

image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")) and f"q{exercise_choice}_" in f]

# === MAIN LOOP ===

running = True
count = 0
img_id, demon = choose_random()
current_image = load_image(img_id)
font = pygame.font.SysFont("Noto Sans", 80)
helpscreen = None
while running:
	screen.fill((0, 0, 0))
	
	if count > 0:
		font = pygame.font.SysFont("Noto Sans", 120)
	
	if not helpscreen and count == 0:
		intro_lines = [
			"Who is that?",
			"Who is this?"
		]
		line_height = 80  # Adjust spacing as needed
		start_y = HEIGHT // 2 - (len(intro_lines) * line_height) // 2
	
		for i, line in enumerate(intro_lines):
			text_surface = font.render(line, True, (200, 200, 200))
			text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * line_height))
			screen.blit(text_surface, text_rect)
	
	elif not helpscreen and count % 2:
		text_surface = font.render(demon + " + " + "?", True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	elif helpscreen:
		font = pygame.font.SysFont("Noto Sans", 20)
		
		help_lines = [
			"Who is .. ? = ... shì shéi?",
			"that ... = nà ...",
			"this ... = zhè ...",
			"daughter = nǔ:'ér",
			"son = érzi",
			"eldest brother = dàgē",
			"dad = bàba",
			"mum = māma",
			"",
			"Jobe = eldest brother",
			"Lucille = mum",
			"George = dad",
			"George Michael = son",
			"Lily = daughter",
			"",
			"Who is that? = nà shì shéi?",
			"Who is this? = zhè shì shéi?",
			"That's my mum = nà shì wǒ māma",
			"That's my son = nà shì wǒ érzi"
		]
		line_height = 27.5  # Adjust spacing as needed
		start_y = 50
	
		for i, line in enumerate(help_lines):
			text_surface = font.render(line, True, (200, 200, 200))
			text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * line_height))
			screen.blit(text_surface, text_rect)
	
	else:
		img_rect = current_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(current_image, img_rect.topleft)
	
	pygame.display.flip()
	
	for event in pygame.event.get():
		helpscreen = None
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				count += 1
				if count and not count % 2:
					current_image = load_image(img_id)
				elif count % 2:
					img_id, demon = choose_random()
			elif event.key == pygame.K_TAB:
				helpscreen = "YES"
			elif event.key == pygame.K_RETURN:
				running = False

pygame.quit()


