import pymysql
# import pymysql.cursors
def connect():
    return pymysql.connect(host= "localhost", user= "root", password= "", database= "dbbimbel", cursorclass=pymysql.cursors.DictCursor)

def format_biaya(biaya):
    return f"Rp {biaya:,.0f}".replace(",", ".")

def fetch_all_items():
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM programs")
            rows = cursor.fetchall()

            for row in rows:
                row['biaya'] = format_biaya(row['biaya'])
            return rows
    finally:
        connection.close()

def insert_item(namaProgram,kelas,durasi,biaya):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO programs (nama_program, kelas, durasi, biaya) VALUES (%s, %s, %s, %s)",(namaProgram,kelas,durasi,biaya))
            connection.commit()
            return 1
    finally:
        connection.close()

def fetch_item_by_id(item_id):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM programs WHERE id = %s", (item_id,))
            rows = cursor.fetchone()
            return rows
    finally:
        connection.close()

def update_item(item_id, namaProgram,kelas,durasi,biaya):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE programs SET nama_program = %s, kelas = %s, durasi = %s, biaya = %s WHERE id = %s",
                           (namaProgram,kelas,durasi,biaya,item_id))
            connection.commit()
            return 1
    finally:
        connection.close()

def delete_item(item_id):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM programs WHERE id = %s", (item_id))
            connection.commit()
            return 1
    finally:
        connection.close()
