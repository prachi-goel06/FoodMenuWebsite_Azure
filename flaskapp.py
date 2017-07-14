from flask import Flask, render_template, request, make_response
from pymongo import MongoClient
import MySQLdb
import pymongo
import base64

app = Flask(__name__)

host = 'prachiserver.mysql.database.azure.com'
user = 'serveradminlogin@prachiserver'
password = 'RanjanaGoel07'
dbname = 'food'
sqldb = MySQLdb.connect(host=host,user=user,passwd=password,db=dbname)
cur = sqldb.cursor()

client = MongoClient('mongodb://hello1:5J7YzXwob8Zkz7hHwjEBM4iKggAvCkxRhZ89v8nNkbJzVEOXla8dEmadEuasLiJCM6YqOzrNBmMQofXe5K0Dfw==@hello1.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')
mgdb = client['mongodb-1']
newcur=mgdb.data

#render the index page on web 
@app.route('/')
def hello_world():
	return render_template('index.html',msg="success")

#action to be taken after the user press the submit button for form with id: query_form1
@app.route('/query1', methods=['GET','POST'])
def query1():
  instruction="select ItemName,column3,TypeFood from foodlist;"
  cur.execute(instruction)
  data=cur.fetchall()
  img=[]
  for item in data:
	print item
	picture=newcur.find_one({"FileName": item[0]})
	img.append(picture['contents'])
  length=len(data)
  return render_template("query1.html", msg=data,img=img,l=length)


@app.route('/query2', methods=['GET','POST'])
def query2():
  value1=request.form['query2_1']
  value2=request.form['query2_2']
  instruction="select ItemName,column3,TypeFood from foodlist where column3>="+value1+" and column3<="+value2+";"
  cur.execute(instruction)
  data=cur.fetchall()
  img=[]
  for item in data:
	print item
	picture=newcur.find_one({"FileName": item[0]})
	img.append(picture['contents'])
  length=len(data)
  return render_template("query1.html", msg=data,img=img,l=length)  

@app.route('/query3', methods=['GET','POST'])
def query3():
  value1=request.form['query3_1']
  instruction="UPDATE foodlist SET counter=counter+1 WHERE column3='"+value1+"';"
  cur.execute(instruction)
  cur.execute("commit;")
  instruction="select ItemName,column3,TypeFood from foodlist where column3>='"+value1+"';"
  print instruction
  cur.execute(instruction)
  data=cur.fetchall()
  img=[]
  for item in data:
	print item[0]
	picture=newcur.find_one({"FileName": item[0]})
	img.append(picture['contents'])
  length=len(data)
  return render_template("query1.html", msg=data,img=img,l=length)

@app.route('/query4', methods=['GET','POST'])
def query4():
  value1=request.form['query4_1']
  value2=request.form['query4_2']
  instruction="UPDATE ingredients SET ingredients='"+value2+"' WHERE ingredients='"+value1+"';"
  cur.execute(instruction)
  cur.execute('commit;')
  instruction="select ItemName,column3,TypeFood from foodlist natural join ingredients where ingredients='"+value2+"';"
  cur.execute(instruction)
  data=cur.fetchall()
  img=[]
  for item in data:
	print item[0]
	picture=newcur.find_one({"FileName": item[0]})
	img.append(picture['contents'])
  length=len(data)
  return render_template("query1.html", msg=data,img=img,l=length)

@app.route('/query5', methods=['GET','POST'])
def query5():
  value1=request.form['query5_1']
  value2=request.form['query5_2']
  instruction="select ItemName,column3,TypeFood from foodlist where column2>="+value1+" and column1<='"+value2+"';"
  cur.execute(instruction)
  data=cur.fetchall()
  img=[]
  for item in data:
	print item[0]
	picture=newcur.find_one({"FileName": item[0]})
	img.append(picture['contents'])
  length=len(data)
  for item in data:
	instruction="SET foreign_key_checks = 0;"
	cur.execute(instruction)
	instruction="SET SQL_SAFE_UPDATES=0;"
	cur.execute(instruction)
  	instruction="delete from ingredients where ItemName='"+item[0]+"';"
	print instruction
	cur.execute(instruction)
	cur.execute("commit;")	
	instruction="delete from foodlist where ItemName='"+item[0]+"';"
	print instruction
	cur.execute(instruction)
	cur.execute("commit;")	
  return render_template("query1.html", msg=data,img=img,l=length)

@app.route('/query6', methods=['GET','POST'])
def query6():
  instruction="select distinct column3 from foodlist order by counter desc limit 3;"
  cur.execute(instruction)
  data=cur.fetchall()
  length=len(data)
  return render_template("query6.html", msg=data,l=length)

@app.route('/query7', methods=['GET','POST'])
def query7():
  value1=request.form['query7_1']
  value2=request.form['query7_2']
  value3=request.form['query7_3']
  if value1!="":
  	instruction="select ItemName,column3,TypeFood from foodlist where column1>="+value1+";"
	print instruction
  	cur.execute(instruction)
  	data=cur.fetchall()
  elif value2!="":
	instruction="select ItemName,column3,TypeFood from foodlist where column3>="+value2+";"
  	cur.execute(instruction)
  	data=cur.fetchall()
  elif value3!="":
	instruction="select ItemName,column3,TypeFood from foodlist where TypeFood>='"+value3+"';"
	print instruction
  	cur.execute(instruction)
  	data=cur.fetchall()
  else:
	return render_template('index.html',msg="success")
  img=[]
  for item in data:
	print item[0]
	picture=newcur.find_one({"FileName": item[0]})
	img.append(picture['contents'])
  length=len(data)
  for item in data:
	instruction="SET foreign_key_checks = 0;"
	cur.execute(instruction)
	instruction="SET SQL_SAFE_UPDATES=0;"
	cur.execute(instruction)
  	instruction="delete from ingredients where ItemName='"+item[0]+"';"
	print instruction
	cur.execute(instruction)
	cur.execute("commit;")	
	instruction="delete from foodlist where ItemName='"+item[0]+"';"
	print instruction
	cur.execute(instruction)
	cur.execute("commit;")	
  return render_template("query1.html", msg=data,img=img,l=length)


if __name__ == '__main__':
  app.run()