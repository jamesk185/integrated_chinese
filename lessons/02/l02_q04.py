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
pygame.display.set_caption("Integrated Chinese Lesson 02 Exercise 04")

def choose_random():
	ans = random.choice([str(x) for x in list(range(2,11))])
	return ans

def load_image():
	img_path = os.path.join(IMAGE_FOLDER, [x for x in image_files if "_01" in x][0])
	image = pygame.image.load(img_path)
	scale = max(image.get_width()/WIDTH, image.get_height()/HEIGHT)
	return pygame.transform.scale(image, (image.get_width()/scale, image.get_height()/scale))

image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")) and f"q{exercise_choice}_" in f]


# === MAIN LOOP ===

running = True
count = 0
ans = choose_random()
current_image = load_image()
font = pygame.font.SysFont("Noto Sans", 40)
helpscreen = None
while running:
	screen.fill((0, 0, 0))
	
	if count > 0:
		font = pygame.font.Font("fonts/DejaVuSans.ttf", 220)
	
	if not helpscreen and count == 0:
		intro_lines = [
			"How many people are in your family?"
		]
		line_height = 80  # Adjust spacing as needed
		start_y = HEIGHT // 2 - (len(intro_lines) * line_height) // 2
	
		for i, line in enumerate(intro_lines):
			text_surface = font.render(line, True, (200, 200, 200))
			text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * line_height))
			screen.blit(text_surface, text_rect)
	
	elif not helpscreen and count == 2:
		text_surface = font.render(ans, True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	elif helpscreen:
		font = pygame.font.SysFont("Noto Sans", 20)
		
		help_lines = [
			"family/home = jiā",
			"how many = jǐ",
			"measure word for people in family = kǒu",
			"2 = liǎng",
			"3 = sān",
			"4 = sì",
			"5 = wǔ",
			"6 = liù",
			"7 = qī",
			"8 = bā",
			"9 = jiǔ",
			"10 = shí",
			"",
			"How many people are there in your family? = Nǐ jiā yǒu jǐ kǒu rén?",
			"There are five people in my family = Wǒ jiā yǒu wǔ kǒu rén"
		]
		line_height = 27.5  # Adjust spacing as needed
		start_y = 100
	
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
				if count == 3:
					count = 1
				if count == 1:
					current_image = load_image()
				elif count == 2:
					ans = choose_random()
			elif event.key == pygame.K_TAB:
				helpscreen = "YES"
			elif event.key == pygame.K_RETURN:
				running = False

pygame.quit()


