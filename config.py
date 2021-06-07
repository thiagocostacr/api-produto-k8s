from dotenv import load_dotenv
import os
load_dotenv()

JSON_SORT_KEYS = os.environ.get('JSON_SORT_KEYS')

SQLALCHEMY_DATABASE_URI = 'mysql://'+ os.getenv('MYSQL_USER') + ':' + os.getenv('MYSQL_PASSWORD') + '@' + os.getenv('MYSQL_HOST') + '/' + os.getenv('MYSQL_DB')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() in ('true')
