from itertools import product

import mysql.connector
from openpyxl import Workbook

from import_data import cursor

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
    SELECT *
    FROM products;
'''
cursor.execute(sql)
products = cursor.fetchall() # รับเข้ามา

# Excel
workbook = Workbook()
sheet = workbook.active
sheet.append(['id', 'ชื่อสินค้า', 'ราคา', 'ความต้องการ', 'วันที่บันทึก', 'กลุ่มสิ่งของ'])

for p in products:
    print(p)
    sheet.append(p)

workbook.save(filename = "exported.xlsx")