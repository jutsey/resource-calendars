# resource-calendars
Python script that generates ics files for calendar import.
This is a work in progress. It requires some fiddling but it handles our problem of needing to produce ics files for teacher 
and room schedules.

TODO: Make it take input from csv files.
TODO: Make it write directly to google calendars via GAM.

There are three tables in the code. 
Period_table -- this will probably stay static, unless you add a new special schedule for a day.
course_table -- this will change when you change teachers, rooms, periods. I just reload it from scratch, except for my lunch calendar
                which is the same every year.
days_table   -- this is where you say on what day what schedule your school is using. If you are on a 7 day block, then you'll use day1,
                day2 versus Monday,Tuesday.  I use Excel to create this table.  I put in the first 2 or 3 dates in the column and then
                "fill" "series" to the end of the school year. you have to use YYYYMMDD as it is required by ics.  Then I put in Monday,
                Tuesday, Wednesday and fill series in the second column. I sort day of week alphabetically and delete the weekends, then 
                sort by day and remove Winter break, spring break etc.  Then for special schedules I change the day of week to the name 
                of the special day. "Open" for open house or "Grandparents" for Grandparents Day. I take that and format it into the 
                table in python.


When you are done you have to close the ics file with END:VCALENDAR
So the close-all.py file just appends that to the end of every ics file in the directory.
To use, after you have updated the tables. open a command prompt or shell and run 
python semester1.py
python semester2.py
python close-all.py

Of course I only included a Semester1.py file here. you'll copy it to make a semester2, and populate it with your semester 2 courses.

Now use your gamdin account with write access to all calndars, and start the import process.


