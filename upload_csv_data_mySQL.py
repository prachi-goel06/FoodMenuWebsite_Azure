import MySQLdb
import os
dirlist = os.listdir("/home/prachi/flaskapp/CSV")
host = 'prachiserver.mysql.database.azure.com'
user = 'serveradminlogin@prachiserver'
password = 'RanjanaGoel07'
dbname = 'food'
sqldb = MySQLdb.connect(host=host,user=user,passwd=password,db=dbname)
cur = sqldb.cursor()
for file in dirlist:
	filepath='/home/prachi/flaskapp/CSV/'+file
	with open(filepath,'r') as f:
		Column1=f.readlines()
		print Column1
	file=file.split('.')[0]
	calories=Column1[0].split(',')
	instruction1="insert into Foodlist values ('"+file+"',"+calories[0]+","+calories[1]+","+calories[2].split('\r')[0]+",'"+Column1[2].split(',')[0]+"',0);"
	cur.execute(instruction1)
	cur.execute('commit;')
	ingrednts=Column1[1].split(',')
	print ingrednts
	for i in range (0,len(ingrednts)):
		print ingrednts[i]
		instruction2="insert into ingredients values ('"+file+"','"+ingrednts[i]+"',0);"
		print instruction2
		cur.execute(instruction2)
		cur.execute('commit;')


