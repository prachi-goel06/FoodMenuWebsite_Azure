from pymongo import MongoClient
import pymongo
import os,base64
dirlist = os.listdir("/home/prachi/flaskapp/Images")
client = MongoClient('mongodb://hello1:5J7YzXwob8Zkz7hHwjEBM4iKggAvCkxRhZ89v8nNkbJzVEOXla8dEmadEuasLiJCM6YqOzrNBmMQofXe5K0Dfw==@hello1.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')
mgdb = client['mongodb-1']
for file in dirlist:
	filepath='/home/prachi/flaskapp/Images/'+file
	with open(filepath,"r") as f:
		content=f.read()
	file=file.split('.')[0]
	print file
	encoded_content = base64.b64encode(content)
	data = {"FileName": file,
			"contents": encoded_content}
	data1 = mgdb.data
	data1_id = data1.insert_one(data).inserted_id