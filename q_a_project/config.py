HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flask_db1'
USERNAME = 'root'
PASSWORD = '19950724'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '1233'