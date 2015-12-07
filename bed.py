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


def play_video():
	video = random.choice(os.listdir(path))
	vidpath = path + video
	child = pexpect.spawn('omxplayer -o local %s' % vidpath)
	while child.isalive():
		if GPIO.input(channel) == 1:
			time.sleep(1)
			if GPIO.input(channel) == 1:
				child.sendline('q')
				lights_up()
				break
	lights_up(False)


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


def pressed(c):
	if GPIO.input(channel) == 0:
		lights_down(False)
		time.sleep(1)
		play_video()


if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(lights, GPIO.OUT)
	GPIO.add_event_detect(channel, GPIO.FALLING,  bouncetime=200)
	GPIO.add_event_callback(channel, pressed)
	lights_up()
	while True:
		time.sleep(1)
		
		
