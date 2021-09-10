#!/usr/bin/python
import time

import Adafruit_DHT

hum_total = 0
count = 0

while True:
	hum, temp = Adafruit_DHT.read_retry(11, 4)
	# print('Temp: ,' temperature, '\n', 'Humidity: ', humidity)
	print('\nHumidity: ', hum, '\nTemperature: ', temp)
	hum_total += hum
	count += 1
	hum_avg = hum_total / count
	print("Humidity Average: ", hum_avg)
	time.sleep(10)
