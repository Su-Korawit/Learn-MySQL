import mysql.connector
from openpyxl import Workbook
# Database

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'root64495',
    database = 'goft_want_to_but'
)

cursor = db.cursor()
sql = '''
    SELECT p.id AS id, p.title AS title, p.price AS price, c.title AS category
    FROM products AS p
    LEFT JOIN categories AS c
    ON p.category_id = c.id;
'''
cursor.execute(sql)
products = cursor.fetchall() # รับเข้ามา

# Excel

workbook = Workbook()
sheet = workbook.active
sheet.append(['id', 'ชื่อสินค้า', 'ราคา', 'กลุ่มสิ่งของ'])

for p in products:
    print(p)
    sheet.append(p)

workbook.save(filename = "exported.xlsx")

cursor.close()
db.close()