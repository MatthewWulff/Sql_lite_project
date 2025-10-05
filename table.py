import sqlite3
# Create connection
conn = sqlite3.connect("first.db") 
#Create cursor
c = conn.cursor()


many_customers = [
                    ("matt", "jay", "value@fff.com"),
                    ("stephaine" , " john", "stuff@333.com"),
                    ("jack", "slater", "viction@ddd.com")
                 ]



c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers )
#commit command
conn.commit()

conn.close()


