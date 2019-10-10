#!/usr/bin/env python
# coding: latin-1

# import a module we might need
##

import sys
import os
from datetime import date
from datetime import datetime


# we will want to iterate over the periods
##

period_list = ['1','2A','2B','3','4A','4B','5','6','7A','7B','TAP','Lunch']

# this is the period information shared
##

period_table = [
	('1','Monday','0815','0905'),
	('2A','Monday','0910','1000'),
	('2B','Monday','0910','1000'),
	('3','Monday','1020','1110'),
	('4A','Monday','1115','1205'),
	('4B','Monday','1205','1255'),
	('5','Monday','1300','1350'),
	('6','Monday','1355','1445'),
	('7A','Monday','1450','1540'),
	('7B','Monday','1450','1540'),
	('Lunch','Monday','1115','1255'),
	('1','Tuesday','1025','1140'),
	('2A','Tuesday','1145','1235'),
	('2B','Tuesday','1235','1325'),
	('3','Tuesday','1450','1540'),
	('6','Tuesday','0815','0930'),
	('7A','Tuesday','1330','1445'),
	('7B','Tuesday','1330','1445'),
	('Lunch','Tuesday','1145','1325'),
	('1','Wednesday','1355','1445'),
	('4A','Wednesday','0815','0930'),
	('4B','Wednesday','0815','0930'),
	('5','Wednesday','0950','1105'),
	('6','Wednesday','1450','1540'),
	('7A','Wednesday','1110','1200'),
	('7B','Wednesday','1200','1250'),
	('Lunch','Wednesday','1110','1250'),
	('2A','Thursday','0815','0930'),
	('2B','Thursday','0815','0930'),
	('3','Thursday','0935','1050'),
	('4A','Thursday','1055','1145'),
	('4B','Thursday','1145','1235'),
	('5','Thursday','1240','1330'),
	('TAP','Thursday','1330','1540'),
	('Lunch','Thursday','1055','1235'),
	('1','Friday','1450','1540'),
	('2A','Friday','1355','1445'),
	('2B','Friday','1355','1445'),
	('3','Friday','1300','1350'),
	('4A','Friday','1115','1205'),
	('4B','Friday','1205','1255'),
	('5','Friday','1020','1110'),
	('6','Friday','0910','1000'),
	('7A','Friday','0815','0905'),
	('7B','Friday','0815','0905'),
	('Lunch','Friday','1115','1255'),
	('1','First','0930','1005'),
	('2A','First','1010','1045'),
	('2B','First','1010','1045'),
	('3','First','1050','1125'),
	('4A','First','1130','1205'),
	('4B','First','1210','1245'),
	('5','First','1250','1325'),
	('6','First','1330','1405'),
	('7A','First','1410','1445'),
	('7B','First','1410','1445'),
	('Lunch','First','1130','1245'),
	('7A','Open','0815','0850'),
	('7B','Open','0815','0850'),
	('6','Open','0855','0930'),
	('5','Open','0950','1025'),
	('4A','Open','1110','1145'),
	('4B','Open','1145','1220'),
	('3','Open','1030','1105'),
	('2A','Open','1225','1300'),
	('2B','Open','1225','1300'),
	('1','Open','1305','1340'),
	('Lunch','Open','1110','1220'),
	]
# create a dict for period lookup
# concatenate the period and day to make a key for lookup
# the corresponding key is a tuple of period start and end times
# lookup is efficient because the dict is based on a hash function
##

period_dict = {}

for p in period_table:
	period_dict[p[0]+'-on-'+p[1]] = (p[2],p[3])

# tables of courses
# (SectionID.Period,CourseName,FacultyName,Room,S1,S2

course_table = [
	("170-01","1","English 7","Bilbo Baggins","8","Y","Y"),
	("170-02","2B","English 7","Bilbo Baggins","8","Y","Y"),
	("170-03","5","English 7","Bilbo Baggins","8","Y","Y"),
	("170-04","7B","English 7","Bilbo Baggins","8","Y","Y"),
	("180-01","3","English 8","Pippin Took","8","Y","Y"),
	("180-02","4B","English 8","Pippin Took","8","Y","Y"),
	("180-03","6","English 8","Pippin Took","8","Y","Y"),
	("180-04","7B","English 8","Pippin Took","11","Y","Y"),
	("190-01","1","English 9","Samwise Gamgee","23","Y","Y"),
	("190-02","2B","English 9","Samwise Gamgee","23","Y","Y"),
	("190-03","4B","English 9","Samwise Gamgee","23","Y","Y"),
	("190-04","5","English 9","Samwise Gamgee","23","Y","Y"),
	("100-01","1","English 10","Frodo Baggins","20","Y","Y"),
	("100-02","2A","English 10","Frodo Baggins","20","Y","Y"),
	("100-03","7A","English 10","Frodo Baggins","20","Y","Y"),
	("110-01","1","English 11","Tom Bombadil","19","Y","Y"),
	("110-02","2A","English 11","Tom Bombadil","19","Y","Y"),
	("110-04","4A","English 11","Tom Bombadil","19","Y","Y"),
	("110-03","5","English 11","Tom Bombadil","19","Y","Y"),
	("120-01","3","English 12","Gimli Gloin","20","Y","Y"),
	("120-02","4A","English 12","Gimli Gloin","20","Y","Y"),
	("120-03","5","English 12","Gimli Gloin","20","Y","Y"),
	("Lunch","Lunch","Lunch","Lunch","Dining","Y","Y"),
]
#leave 	("Lunch","Lunch","Lunch","Lunch","Dining","Y","Y"), as the last line above

course_by_period = [[] for x in period_list]

for course in course_table:
	course_by_period[period_list.index(course[1])].append(course)

days_table = [
	("20190821","First"),
	("20190822","Monday"),
	("20190823","Friday"),
	("20190826","Monday"),
	("20190827","Tuesday"),
	("20190828","Wednesday"),
	("20190829","Thursday"),
	("20190830","Friday"),
	("20191018","Open"),
	("20191021","Monday"),
	("20191022","Tuesday"),
	("20191023","Wednesday"),
	("20191024","Thursday"),
	("20191025","Friday"),
	("20191211","Monday"),
	("20191212","Friday"),
	("20191213","Friday"),
	("20191216","Monday"),
]

for day in days_table:
	weekday = day[1]
	for period in period_list:
		k = period+'-on-'+weekday
		if k in period_dict:
			courses = course_by_period[period_list.index(period)]
			for c in courses:
				start = period_dict[k][0]
				end = period_dict[k][1]
				cid = c[0]				
				cperiod=c[1]
				ctitle = c[2]
				cteacher = c[3]
				croom = c[4]
				rightnow = datetime.now().strftime("%Y%m%d%H%M%S%f")
				timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
				uid = cid+rightnow
				##This writes the room file
				icsfile = croom+".ics"
				if not os.path.exists(icsfile):
					f=open(icsfile , 'a')
					## the prodid is a field for ics that describes what made the ics file.
					print ("BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:<jpu_python_Sept_2015>", file=f)
					##Set for your timezone.
					print ("CALSCALE:GREGORIAN\nX-WR-TIMEZONE:America/Denver", file=f)
					f.close()
				f=open(icsfile , 'a')
				print ("BEGIN:VEVENT", file=f)
				print ("UID:",uid, file=f)
				print ("DTSTART:",day[0]+"T"+start+"00", file=f)
				print ("DTEND:",day[0]+"T"+end+"00", file=f)
				print ("DTSTAMP:",timestamp, file=f)
				print ("CREATED:",timestamp, file=f)
				print ("DESCRIPTION:",ctitle,"during Period",cperiod,"with:",cteacher,", Section:",cid, file=f)
				print ("LOCATION:",croom, file=f)
				print ("SUMMARY:",ctitle,"period",cperiod, file=f)
				print ("ORGANIZER: CN="+cteacher, file=f)
				print ("STATUS:CONFIRMED", file=f)
				print ("TRANSP:OPAQUE", file=f)
				print ("END:VEVENT", file=f)
				f.close()


				##This writes the teacher file
					
				icsfile= cteacher+".ics"
				if not os.path.exists(icsfile):
					f=open(icsfile , 'a')
					print ("BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:<jpu_python_Aug_2019>", file=f)
					##Set for your timezone.
					print ("CALSCALE:GREGORIAN\nX-WR-TIMEZONE:America/Denver", file=f)
					f.close()				
				f=open(icsfile , 'a')
				print ("BEGIN:VEVENT", file=f)
				print ("UID:",uid, file=f)
				print ("DTSTART:",day[0]+"T"+start+"00", file=f)
				print ("DTEND:",day[0]+"T"+end+"00", file=f)
				print ("DTSTAMP:",timestamp, file=f)
				print ("CREATED:",timestamp, file=f)
				print ("DESCRIPTION:",ctitle,"during Period",cperiod,"with:",cteacher,", Section:",cid, file=f)
				print ("LOCATION:",croom, file=f)
				print ("SUMMARY:",ctitle,"period",cperiod, file=f)
				print ("ORGANIZER: CN="+cteacher, file=f)
				print ("STATUS:CONFIRMED", file=f)
				print ("TRANSP:OPAQUE", file=f)
				print ("END:VEVENT", file=f)
				f.close()
