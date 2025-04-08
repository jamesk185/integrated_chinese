# Author: James Kowalik
# Created: 25/04/08
# Revised: 
# Description: Integrated Chinese lesson 02 question 03

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
pygame.display.set_caption("Integrated Chinese Lesson 02 Exercise 03")

l02_q03 = {"01": "older_sister", "02": "younger_brother", "03": "oldest_brother"}

def choose_random():
	img_id = random.choice(list(l02_q03.keys()))
	child = random.choice(["👨‍👩‍👧", "👪"])
#	ans = random.choice(["✓", "✗"])
	ans = random.choice(["+", "-"])
	return img_id, child, ans

def load_image(img_id):
	img_path = os.path.join(IMAGE_FOLDER, [x for x in image_files if "_" + img_id in x][0])
	image = pygame.image.load(img_path)
	scale = max(image.get_width()/WIDTH, image.get_height()/HEIGHT)
	return pygame.transform.scale(image, (image.get_width()/scale, image.get_height()/scale))

image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")) and f"q{exercise_choice}_" in f]


# === MAIN LOOP ===

running = True
count = 0
img_id, child, ans = choose_random()
current_image = load_image(img_id)
font = pygame.font.SysFont("Noto Sans", 80)
helpscreen = None
while running:
	screen.fill((0, 0, 0))
	
	if count > 0:
		font = pygame.font.SysFont("Noto Sans", 120)
	
	if not helpscreen and count == 0:
		intro_lines = [
			"Does your eldest brother have a daughter?",
			"Does your younger brother have a son?",
			"Does your older sister have a daughter?",
		]
		line_height = 80  # Adjust spacing as needed
		start_y = HEIGHT // 2 - (len(intro_lines) * line_height) // 2
	
		for i, line in enumerate(intro_lines):
			text_surface = font.render(line, True, (200, 200, 200))
			text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * line_height))
			screen.blit(text_surface, text_rect)
	
	elif not helpscreen and not count % 2:
		text_surface = font.render(ans, True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	elif helpscreen:
		font = pygame.font.SysFont("Noto Sans", 20)
		
		help_lines = [
			"older sister = jiějie",
			"younger brother = dìdi",
			"eldest brother = dàgē"
			"child = háizi",
			"daughter = nǚ'ér",
			"son = érzi",
			"you = ní",
			"have = yǒu",
			"",
			"Does your eldest brother gāo have a daughter? = Gāo dàgē yǒu nǚ'ér ma?",
			"No = Méiyǒu, tā méiyǒu nǚ'ér",
			"Does gāo whenzong have an older sister? = Gāo whénzhōng yǒu jiějie ma?",
			"Who is that girl = nà ge nǚ háizi shì shéi",
			"No = méiyǒu, tā méiyǒu jiějie",
			"Does your eldest brother gāo have a son? = Gāo dàgē yǒu érzi ma?",
			"Yes = shi, tá yǒu érzi"
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
				if count and count % 2:
					current_image = load_image(img_id)
				elif not count % 2:
					img_id, child, ans = choose_random()
			elif event.key == pygame.K_TAB:
				helpscreen = "YES"
			elif event.key == pygame.K_RETURN:
				running = False

pygame.quit()


