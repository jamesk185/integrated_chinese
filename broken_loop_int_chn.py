# Author: James Kowalik
# Created: 25/03/25
# Revised: 25/04/02
# Description: Create prompt cards for practising building sentences in Chinese
#			  corresponds to content of "Integrated Chinese Level 1 Part 1"

import pygame
import os
import random

# === MENU SETUP ===

lessons = {
	1: "Lesson 1",
	2: "Lesson 2",
	3: "Lesson 3"
}

exercises = {
	1: {
		1: "Who is... this/that... ?",
		2: "(empty for now)",
		3: "(empty for now)"
	},
	2: {
		1: "Who is... this/that... ?",  # this matches your current setup
		2: "(empty)",
		3: "(empty)"
	},
	3: {
		1: "(empty)",
		2: "(empty)",
		3: "(empty)"
	}
}

# === USER INPUT ===

print("Select a Lesson:")
for num, name in lessons.items():
	print(f"{num} - {name}")
lesson_choice = int(input("Enter lesson number: "))

print("\nSelect an Exercise:")
for num, name in exercises.get(lesson_choice, {}).items():
	print(f"{num} - {name}")
exercise_choice = int(input("Enter exercise number: "))

# === PYGAME SETUP ===

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Image Viewer")

l02_q01 = {"01": "woman", "02": "boy", "03": "girl", "04": "man"}

def choose_random():
	img_id = random.choice(list(l02_q01.keys()))
	demon = random.choice(["this", "that"])
	gender = "M" if l02_q01.get(img_id) in ["boy", "man"] else "F"
	return img_id, demon, gender

# Load images based on selected lesson/exercise
IMAGE_FOLDER = f"images/l{str(lesson_choice).zfill(2)}q{str(exercise_choice).zfill(2)}"  # folder structure must follow this
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif"))]

if not image_files:
	print("No images found in the selected folder!")
	pygame.quit()
	exit()

def load_image(img_id):
	img_path = os.path.join(IMAGE_FOLDER, [x for x in image_files if img_id in x][0])
	image = pygame.image.load(img_path)
	scale = max(image.get_width()/WIDTH, image.get_height()/HEIGHT)
	return pygame.transform.scale(image, (image.get_width()/scale, image.get_height()/scale))

current_image = load_image("01")

# === MAIN LOOP ===

running = True
count = 0
font = pygame.font.Font(None, 80)
while running:
	screen.fill((0, 0, 0))
	
	if count > 0:
		font = pygame.font.Font(None, 120)
	
	if count == 0:
		intro_lines = [
			"Who is that man?",
			"Who is this woman?",
			"Who is this boy?",
			"Who is that girl?"
		]
		line_height = 80  # Adjust spacing as needed
		start_y = HEIGHT // 2 - (len(intro_lines) * line_height) // 2
	
		for i, line in enumerate(intro_lines):
			text_surface = font.render(line, True, (200, 200, 200))
			text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * line_height))
			screen.blit(text_surface, text_rect)
	
	elif count % 2:
		img_id, demon, gender = choose_random()
		text_surface = font.render(demon + " + " + gender + " + " + "?", True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	else:
		img_rect = current_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(current_image, img_rect.topleft)
	
	pygame.display.flip()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				count += 1
				if count and not count % 2:
					current_image = load_image(img_id)
			elif event.key == pygame.K_RETURN:
				running = False

pygame.quit()


