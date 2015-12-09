#! /usr/bin/env python

import pexpect
import os
import random
import time
import RPi.GPIO as GPIO

#Setup
GPIO.cleanup()
path = "/home/pi/Videos/"
channel = 18
lights = [3, 5, 7, 11, 13, 15, 19, 31]
playing = False


def play_video():
	global playing
	playing = True
	video = random.choice(os.listdir(path))
	vidpath = path + video
	child = pexpect.spawn('omxplayer -o local %s' % vidpath)
	while child.isalive():
		if GPIO.input(channel) == 1:
			time.sleep(1)
			if GPIO.input(channel) == 1:
				child.sendline('q')
				lights_up()
				playing = False
				break
	lights_up(False)
	time.sleep(15)
	playing = False


def lights_up(all=True):
	if all == True:
		GPIO.output(lights, GPIO.LOW)
	else:
		for l in lights:
				GPIO.output(l, GPIO.LOW)
				time.sleep(1)


def lights_down(all=True):
	if all == True:
		GPIO.output(lights, GPIO.HIGH)
	else:
		for l in reversed(lights):
				GPIO.output(l, GPIO.HIGH)
				time.sleep(1)



if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(lights, GPIO.OUT)
	lights_up()
	while True:
		if (playing == False and GPIO.input(channel) == 0):
                	print "GO!"
                	lights_down(False)
                	play_video()

