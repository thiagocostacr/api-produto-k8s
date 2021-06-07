import MySQLdb
from models import *
from config import os

conn = MySQLdb.connect(user=os.getenv('MYSQL_USER'), passwd=os.getenv('MYSQL_PASSWORD'), host=os.getenv('MYSQL_HOST'), port=int(os.environ.get('MYSQL_PORT')))

criar_database = '''CREATE DATABASE produtos;'''

conn.cursor().execute(criar_database)

db.create_all()
