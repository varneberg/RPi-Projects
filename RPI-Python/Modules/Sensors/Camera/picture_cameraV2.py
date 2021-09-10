from time import sleep

from picamera import PiCamera

camera = PiCamera()
camera.rotation = 180
sleep(0.1)

camera.capture('/home/pi/Pictures/Camera/test2.jpg')
