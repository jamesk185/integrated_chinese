# Author: James Kowalik
# Created: 25/04/11
# Revised: 
# Description: Integrated Chinese lesson 01 question 01

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
pygame.display.set_caption("Integrated Chinese Lesson 01 Exercise 01")

# === MAIN LOOP ===

running = True
count = 0
font = pygame.font.SysFont("Noto Sans", 75)
helpscreen = None
while running:
	screen.fill((0, 0, 0))
	
	if count > 0:
		font = pygame.font.SysFont("Noto Sans", 100)
	
	if not helpscreen and count == 0:
		intro_lines = [
			"What's your name?"
		]
		line_height = 80  # Adjust spacing as needed
		start_y = HEIGHT // 2 - (len(intro_lines) * line_height) // 2
	
		for i, line in enumerate(intro_lines):
			text_surface = font.render(line, True, (200, 200, 200))
			text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * line_height))
			screen.blit(text_surface, text_rect)
	
	elif not helpscreen and count == 1:
		font = pygame.font.Font("fonts/seguiemj.ttf", 220)
		text_surface = font.render("A: 👋", True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	elif not helpscreen and count == 2:
		font = pygame.font.Font("fonts/seguiemj.ttf", 220)
		text_surface = font.render("B: 👋", True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	elif not helpscreen and count == 3:
		text_surface = font.render("A: family name?", True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	elif not helpscreen and count == 4:
		text_surface = font.render("B: ans. you?", True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	elif not helpscreen and count == 5:
		font = pygame.font.SysFont("Noto Sans", 50)
		text_surface = font.render("A: ans. first name. first name?", True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	elif not helpscreen and count == 6:
		text_surface = font.render("B: ans", True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		screen.blit(text_surface, text_rect)
	
	elif helpscreen:
		font = pygame.font.SysFont("Noto Sans", 20)
		
		help_lines = [
			"hello = nǐ hǎo",
			"excuse me, may I please ask... = qǐng wèn",
			"I = wǒ",
			"you = nǐ",
			"guì = honorable; expensive",
			"to be surnamed (v) / surname (n) = xìng",
			"to be called = jiào",
			"and you? = nǐ ne?",
			"what = shénme",
			"name = míngzi",
			"",
			"May I ask, what is your surname? = qǐng wèn, nǐ guì xìng?",
			"What is your name? = nǐ jiào shénme míngzi?",
			"I am called (surnamed) Wang = wǒ xìng Wáng",
			"I am called Wang Peng = wǒ jiào Wáng Péng"
		]
		line_height = 27.5  # Adjust spacing as needed
		start_y = 100
	
		for i, line in enumerate(help_lines):
			text_surface = font.render(line, True, (200, 200, 200))
			text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * line_height))
			screen.blit(text_surface, text_rect)
	
	pygame.display.flip()
	
	for event in pygame.event.get():
		helpscreen = None
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				count += 1
				if count == 7:
					count = 1
			elif event.key == pygame.K_TAB:
				helpscreen = "YES"
			elif event.key == pygame.K_RETURN:
				running = False

pygame.quit()


