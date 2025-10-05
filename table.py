import sqlite3
# Create connection
conn = sqlite3.connect("first.db") 
#Create cursor
c = conn.cursor()



c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@GMEM.com')")
#commit command
conn.commit()

conn.close()


