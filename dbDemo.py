from utilities.configurations import *

conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchall()

print(row)
print(type(row))
for rows in row:
    print(rows[2])

query = "update customerInfo set Location = %s where CourseName =%s"
data = ("UK", "JMETER")
cursor.execute(query,data)
conn.commit()
conn.close()
