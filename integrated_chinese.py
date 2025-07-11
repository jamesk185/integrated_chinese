# Author: James Kowalik
# Created: 25/03/25
# Revised: 25/04/05
# Description: Create prompt cards for practising building sentences in Chinese
#              corresponds to content of "Integrated Chinese Level 1 Part 1"

import pygame
import os
import random
import subprocess

# === MENU SETUP ===

lessons = {
	1: "Lesson 1",
	2: "Lesson 2",
	3: "Lesson 3"
}

exercises = {
	1: {
		1: "Hello. What's your name?",
		2: "(empty)",
		3: "(empty)"
	},
	2: {
		1: "Who is this/that... ? That/that is {name}.",  # this matches your current setup
		2: "Who is this/that? That's my... .",
		3: "Does your... have a... ?",
		4: "How many people are in your family?"
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

# Select lesson folder
lesson_folder = f"lessons/{str(lesson_choice).zfill(2)}"
exercise_choice = str(exercise_choice).zfill(2)
lesson_py = lesson_folder + f"/l{str(lesson_choice).zfill(2)}_q{exercise_choice}.py"

# Load images based on selected lesson/exercise
IMAGE_FOLDER = lesson_folder + "/images"
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")) and f"q{str(exercise_choice).zfill(2)}_" in f]

subprocess.run(["python3", lesson_py, IMAGE_FOLDER, exercise_choice])


