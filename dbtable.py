import mysql.connector
database = mysql.connector.connect(
    host='localhost',
    username='root',
    password='123456',
)
connection = database.cursor()
selectdb ='use bus_booking'
connection.execute(selectdb)
tableCreationQuery = """
create table passengers(id int primary key auto_increment, 
                        name varchar(255),
                        age int,
                        destination varchar(255));
"""

connection.execute(tableCreationQuery)
connection = database.cursor()
describeTableQuery = 'DESC passengers';
connection.execute(describeTableQuery)
for descriptions in connection:
    print(descriptions)
database.close()
