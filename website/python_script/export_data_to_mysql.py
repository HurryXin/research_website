# -*- coding = utf-8 -*-
import csv
import MySQLdb

# connect mysql
db = MySQLdb.connect("localhost", "ruixin", "123", "caesar")
# use cursor()
cursor = db.cursor()

# open csv file
file = csv.reader(open('result.csv'))
i = 0
for row in file:
	i = i + 1
	# delete the first row
	if i > 1:
		id = int(row[0]) + 1;
		trade_id = row[1]
		module = row[2]
		predict = row[3]
		result = row[4]
		cursor.execute("insert into caesar_brainmodule value("+str(id)+","+predict+","+result+","+trade_id+","+module+");")
		db.commit()
		# print "insert into caesar_brainmodule value("+str(id)+","+predict+","+result+","+trade_id+","+module+")"
		print row

# close mysql connection    
db.close()