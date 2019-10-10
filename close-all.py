import os

for file in os.listdir():
	if file.endswith(".ics"):
		f = open(file, 'a')
		print ("END:VCALENDAR", file=f)
		f.close()
