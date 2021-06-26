# This code was done by following a Youtube video: https://www.youtube.com/watch?v=JavJqJHLo_M

import os, time

os.system('cls')
fileNames = ["waterfall1.txt", "waterfall2.txt", "waterfall3.txt"]
frames = []

for name in fileNames:
	with open(name, "r", encoding="utf8") as f:
		frames.append(f.readlines())
		
for i in range(10):
	for frame in frames:
		print("".join(frame))
		time.sleep(0.1)
		os.system('cls')
