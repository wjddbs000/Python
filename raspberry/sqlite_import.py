from sys import argv
import csv
import sqlite3

conn = sqlite3.connect('sample.db')
c = conn.cursor()

if len(argv)<2: #아규먼트 에러
    print("error")
    exit(1)
else:
    csvfile = argv[1]
    print(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS student ( id INTEGER PRIMARY KEY AUTOINCREMENT,\
        name TEXT, birth DATE, gender CHAR )")
    student =csv.reader(open(csvfile,'r'),delimiter=',',quotechar='"')

index = 0

for row in student:
    index = index +1
    print("%s" % (row))
    c.execute("INSERT INTO student (name,birth,gender) VALUES (?,?,?)",(row[0],row[1],row[2]))

conn.commit()
conn.close()
exit()