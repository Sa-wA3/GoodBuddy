#!/usr_bin_env python
#-*- cording: utf-8 -*-

import pygame.mixer
import time

pygame.mixer.init()
pygame.mixer.music.load("ファイル名.mp3")
pygame.mixer.music.p;ay(-1)

time.sleep(60)
pygame.mixer.music.stop()

import wiringpi as w
import time

led_pin = 0;
cds_pin = 1;

w.wiringPiSetup()
w.pipMode(led_pin, 0)
w.pipMode(cds_pin, 1)

while 1:
  switch = w.digitalRead(0)
    if 1 == switch:
      #print(1)
      w.digitalWrite(led_pin,1)
    else
      #print(0)
      w.digitalWrite(cds_pin,0)
    time.sleep(1)
