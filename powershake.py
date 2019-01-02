from itertools import cycle
import math
import random
import socket
from struct import *
import sys
import time

import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    from pygame.locals import *
	
	
class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()  # to squash errors for the time being


FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 400
# amount by which base can maximum shift to left
PIPEGAPSIZE  = 100 # gap between upper and lower part of pipe
BASEY        = SCREENHEIGHT * 0.79
# image, sound and hitmask  dicts
IMAGES, SOUNDS, HITMASKS = {}, {}, {}

# list of backgrounds
BACKGROUNDS_LIST = (
    'assets/sprites/background-day.png',
    'assets/sprites/background-night.png',
)


def euclidean(x, y, z):
    return (float(x)**2 + float(y)**2 + float(z)**2)**0.5
	
	
def retrieve_UDP_values():
    UDP_IP = socket.gethostbyname(socket.gethostname())
    #UDP_IP = "192.168.43.136"
    UDP_PORT = 5001
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(.02)
    sock.bind((UDP_IP, UDP_PORT))
    try:
        data, addr = sock.recvfrom(1024)
        A_X = "%1.4f" %unpack_from ('!f', data, 0)
        A_Y = "%1.4f" %unpack_from ('!f', data, 4)
        A_Z = "%1.4f" %unpack_from ('!f', data, 8)
        return euclidean(float(A_X), float(A_Y), float(A_Z))
    except socket.timeout:
        return 0

		
def showScore(score, ratio = 0.1):
	"""displays score in center of screen"""
	scoreDigits = list(str(score))
	totalWidth = 0 # total width of all numbers to be printed

	for digit in scoreDigits:
		if digit == '.':
			digit = 10
		else:
			digit = int(digit)
		totalWidth += IMAGES['numbers'][digit].get_width()

	Xoffset = (SCREENWIDTH - totalWidth) / 2

	for digit in scoreDigits:
		if digit == '.':
			digit = 10
			scaled_dot = pygame.transform.scale(IMAGES['numbers'][digit], (10, 10))
			SCREEN.blit(scaled_dot, (Xoffset + 7, SCREENHEIGHT * (ratio + 0.07)))
		else:
			digit = int(digit)
			SCREEN.blit(IMAGES['numbers'][digit], (Xoffset, SCREENHEIGHT * ratio))
		Xoffset += IMAGES['numbers'][digit].get_width()

		
def main():
	global SCREEN, FPSCLOCK
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
	pygame.display.set_caption('Power Shake')

    # numbers sprites for score display
	IMAGES['numbers'] = (
		pygame.image.load('assets/sprites/0.png').convert_alpha(),
		pygame.image.load('assets/sprites/1.png').convert_alpha(),
		pygame.image.load('assets/sprites/2.png').convert_alpha(),
		pygame.image.load('assets/sprites/3.png').convert_alpha(),
		pygame.image.load('assets/sprites/4.png').convert_alpha(),
		pygame.image.load('assets/sprites/5.png').convert_alpha(),
		pygame.image.load('assets/sprites/6.png').convert_alpha(),
		pygame.image.load('assets/sprites/7.png').convert_alpha(),
		pygame.image.load('assets/sprites/8.png').convert_alpha(),
		pygame.image.load('assets/sprites/9.png').convert_alpha(),
		pygame.image.load('assets/sprites/dot.png').convert_alpha()
	)
	
	# game over sprite
	IMAGES['gameover'] = pygame.image.load('assets/sprites/gameover.png').convert_alpha()
	IMAGES['timetaken'] = pygame.image.load('assets/sprites/timetaken.png').convert_alpha()
	IMAGES['seconds'] = pygame.image.load('assets/sprites/seconds.png').convert_alpha()
	# message sprite for welcome screen
	IMAGES['power'] = pygame.image.load('assets/sprites/power.png').convert_alpha()
	IMAGES['shake'] = pygame.image.load('assets/sprites/shake.png').convert_alpha()
	IMAGES['team14'] = pygame.image.load('assets/sprites/team14.png').convert_alpha()
	IMAGES['countdown'] = pygame.image.load('assets/sprites/countdown.png').convert_alpha()
	# base (ground) sprite
	IMAGES['base'] = pygame.image.load('assets/sprites/base.png').convert_alpha()
	# game animation sprite
	IMAGES['phoneshake'] = pygame.image.load('assets/sprites/phoneshake.png').convert_alpha()

	while True:
		# select random background sprites
		randBg = random.randint(0, len(BACKGROUNDS_LIST) - 1)
		IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert()
		showWelcomeAnimation()
		elapsed_time = mainGame()
		showGameOverScreen(elapsed_time)


def showWelcomeAnimation():

	tapped = False
	
	powerx = int((SCREENWIDTH - IMAGES['power'].get_width()) / 2)
	powery = int(SCREENHEIGHT * 0.10)
	shakex = int((SCREENWIDTH - IMAGES['shake'].get_width()) / 2)
	shakey = int(SCREENHEIGHT * 0.20)
	team14x = int((SCREENWIDTH - IMAGES['team14'].get_width()) / 2)
	team14y = int(SCREENHEIGHT * 0.45)
	countdownx = int((SCREENWIDTH - IMAGES['countdown'].get_width()) / 2)
	countdowny = int(SCREENHEIGHT * 0.35)

	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				#sys.exit()
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				tapped = True
	
		SCREEN.blit(IMAGES['background'], (0,0))
		SCREEN.blit(IMAGES['power'], (powerx, powery))
		SCREEN.blit(IMAGES['shake'], (shakex, shakey))
		SCREEN.blit(IMAGES['team14'], (team14x, team14y))
		A_XYZ = retrieve_UDP_values()
		
		if A_XYZ > 2 or tapped:
			SCREEN.blit(IMAGES['background'], (0,0))
			SCREEN.blit(IMAGES['power'], (powerx, powery))
			SCREEN.blit(IMAGES['shake'], (shakex, shakey))
			SCREEN.blit(IMAGES['countdown'], (countdownx, countdowny))
			showScore(3, 0.45)
			pygame.display.update()
			FPSCLOCK.tick(FPS)
			time.sleep(1)
			SCREEN.blit(IMAGES['background'], (0,0))
			SCREEN.blit(IMAGES['power'], (powerx, powery))
			SCREEN.blit(IMAGES['shake'], (shakex, shakey))
			SCREEN.blit(IMAGES['countdown'], (countdownx, countdowny))
			showScore(2, 0.45)
			pygame.display.update()
			FPSCLOCK.tick(FPS)
			time.sleep(1)
			SCREEN.blit(IMAGES['background'], (0,0))
			SCREEN.blit(IMAGES['power'], (powerx, powery))
			SCREEN.blit(IMAGES['shake'], (shakex, shakey))
			SCREEN.blit(IMAGES['countdown'], (countdownx, countdowny))
			showScore(1, 0.45)
			pygame.display.update()
			FPSCLOCK.tick(FPS)
			time.sleep(1)
			return
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def mainGame():
	
	tapped = False
	shake = 1
	
	score = 0
	start_time = time.time()
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				#sys.exit()
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				tapped = True	
	
		# draw sprites
		SCREEN.blit(IMAGES['background'], (0,0))
		
		A_XYZ = retrieve_UDP_values()
		
		if A_XYZ > 2 or tapped:
			shake = -shake
			score += 1
			if score == 100:
				return time.time() - start_time
				
		showScore(score)
		shaker = pygame.transform.rotate(IMAGES['phoneshake'], shake * 15)
		SCREEN.blit(shaker, (30,100))

		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
	return
	

def showGameOverScreen(elapsed_time):

	tapped = False
	truncated_time = str(math.ceil(elapsed_time * 1000.0) / 1000.0)
	reset = 0

	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				#sys.exit()
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				tapped = True
		
		A_XYZ = retrieve_UDP_values()
		
		if A_XYZ > 2 or tapped:
			reset += 1
			if reset == 10:
				return
		
		# draw sprites
		SCREEN.blit(IMAGES['background'], (0, 0))
		SCREEN.blit(IMAGES['gameover'], (50, 75))
		SCREEN.blit(IMAGES['timetaken'], ((SCREENWIDTH - IMAGES['timetaken'].get_width()) / 2, SCREENHEIGHT * 0.42))
		showScore(truncated_time, 0.5)
		SCREEN.blit(IMAGES['seconds'], ((SCREENWIDTH - IMAGES['seconds'].get_width()) / 2, SCREENHEIGHT * 0.62))
		
		FPSCLOCK.tick(FPS)
		pygame.display.update()

	
	
if __name__ == '__main__':
    main()