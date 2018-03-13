import os
import sqlite3

def getImages():
	conn = sqlite3.connect('DobbleImages.sqlite')
	cursor = conn.cursor()
	cursor.execute("""SELECT id FROM images""")
	images = cursor.fetchall()
	retour = len(images) * ['']
	for i in range(len(images)):
		retour[i] = images[i][0]
	conn.close()
	return retour
