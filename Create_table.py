import MySQLdb
host = 'prachiserver.mysql.database.azure.com'
user = 'serveradminlogin@prachiserver'
password = 'RanjanaGoel07'
dbname = 'food'
sqldb = MySQLdb.connect(host=host,user=user,passwd=password,db=dbname)
cur = sqldb.cursor()

instruction="create table Foodlist(ItemName varchar(20), column1 integer, column2 integer, column3 integer,TypeFood varchar(20),counter integer, PRIMARY KEY (ItemName));"
cur.execute(instruction)
instruction="create table Ingredients(ItemName varchar(20), ingredients varchar(40),counter integer,FOREIGN KEY (ItemName) REFERENCES Foodlist(ItemName));"
cur.execute(instruction)