import pygame
import sys

# LEVEL EDITOR CLASS RUNS THE LEVEL EDITOR LOOP
class LevelEditor:
	def __init__(self) -> None:
		pygame.init()

		# SET UP PYGAME WINDOW
		pygame.display.set_caption("LEVEL EDITOR")

		self.WIDTH= 640
		self.HEIGHT = 480
		self.TILE_SIZE = 16
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

		"""
		CREATE PIXEL ART EFFECT:
			RENDER ASSETS ONTO SMALLER DISPLAY
			SCALE THE, UP TO THE SCREEN SIZE
		"""
		self.PIXEL_WIDTH = 320
		self.PIXEL_HEIGHT = 240
		self.display = pygame.Surface((self.PIXEL_WIDTH, self.PIXEL_HEIGHT))

		# RUN GAME AT 60 FPS
		self.clock = pygame.time.Clock()
		self.fps = 60

		# DEFINE ASSETS USED IN OUR GAME

	def run(self):
		while True:
			#COLOR OF THE SKY
			self.display.fill((114, 116, 248))

			"""
			GET INPUT:
				pygame.event.get():
					GET INPUT BY INTERACTING WITH OS
			"""
			for event in pygame.event.get():
				"""
				WHEN EVENT TYPE IS pygame.quit():
					CLOSE GAME WINDOW
				"""
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			"""
			THE BLIT FUNCTION COPIES A SECTION OF MEMORY
			ONTO ANOTHER SURFACE

			WE ARE BLITTING THE SCALED DOWN DISPLAY SURFACE (PIXEL ART EFFECT),
			ONTO THE SIZE OF THE PLAYER'S SCREEN
			"""
			self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

			# UPDATE DISPLAY
			pygame.display.update()

			# FORCE LOOP TO RUN AT 60FPS
			self.clock.tick(self.fps)

# RUN LEVEL EDITOR WHEN SCRIPT IS EXECUTED
LevelEditor().run()
