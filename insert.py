import mysql.connector
database = mysql.connector.connect(
    host='localhost',
    username='root',
    password='123456',
)
connection = database.cursor()
selectdb ='use bus_booking'
connection.execute(selectdb)
name = (input("passengers Name : "))
age = (int(input("passengers Age: ")))
destination = (input("passengers Destination: "))
insertQuery='''
insert into passengers(name,age,destination) values(%s,%s,%s)

'''
insertValues=[
    (name,age,destination)
]
connection.executemany(insertQuery,insertValues)
database.commit()
database.close()