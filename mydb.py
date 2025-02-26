import psycopg2

dataBase=psycopg2.connect(
    host='localhost',
    user='postgres',
    password='0000'

)
dataBase.autocommit=True
cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE project1")


