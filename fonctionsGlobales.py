import os
import sqlite3

def getImages():
	conn = sqlite3.connect('DobbleImages.sqlite')
	cursor = conn.cursor()
	cursor.execute("""SELECT id FROM images""")
	images = cursor.fetchAll()
	conn.close()
	return images