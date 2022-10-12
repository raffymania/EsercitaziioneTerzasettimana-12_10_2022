import mysql.connector

conn = mysql.connector.connect(user='root', password='Pinam0nt01', host='127.0.0.1', database='discografia')
cursor = conn.cursor()
sql = 'SELECT * FROM autore;'
cursor.execute(sql)
result = cursor.fetchone()
print(result)
conn.close()

conn = mysql.connector.connect(user='root', password='Pinam0nt01', host='127.0.0.1', database='discografia')
cursor = conn.cursor()
sql = "insert into autore (nome, TitoloCanzone) values (%s, %s)"
valori = ("RAF", "infinito")
valori1 = ("Mengoni", "NoStress")
valori2 = ("Mina", "SeTelefonando")
try:
    print(sql, valori)
    cursor.execute(sql, valori2)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

conn.close()
#inserisco dati in esecuzione

conn = mysql.connector.connect(user='root', password='Pinam0nt01', host='127.0.0.1', database='discografia')
cursor = conn.cursor()
sql = "insert into esecuzione (CodiceReg, TitoloCanzone, Anno) values (%s, %s)"
valori = ("RAF", "infinito")
valori1 = ("Mengoni", "NoStress")
valori2 = ("Mina", "SeTelefonando")
try:
    print(sql, valori)
    cursor.execute(sql, valori2)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

conn.close()