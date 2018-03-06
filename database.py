import sqlite3
import glob


def creerSchema(conn):
	conn.execute('''
    create table if not exists IMAGES (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	IMAGE BLOB)''')
	
def insert_picture(conn, picture_file):
	with open(picture_file, 'rb') as input_file:
		ablob = input_file.read()
		sql = '''INSERT INTO IMAGES
		(IMAGE)
		VALUES(?);'''
		conn.execute(sql,[sqlite3.Binary(ablob)]) 
		conn.commit()


def peuplerBase(conn):
	conn.execute("DELETE FROM IMAGES")
	images = glob.glob("./images/*.png")
	for image in images:
		picture_file = image
		insert_picture(conn, picture_file)
		
def afficherContenu(conn):
	for r in conn.execute("SELECT ID FROM IMAGES"):
		print r[0]
	
conn = sqlite3.connect('DobbleImages.sqlite')

afficherContenu(conn)