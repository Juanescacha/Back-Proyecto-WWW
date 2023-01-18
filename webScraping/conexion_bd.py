import psycopg2

def getConexion():
    conn = psycopg2.connect(
        host = "containers-us-west-34.railway.app",
        database ="railway",
        user ="postgres",
        password="F1x0iW0NauU9s28cEJlg",
        port=7371,
    )
    return conn

def inserData(railway, tableName):
    conn = getConexion()
    cur = conn.cursor()

    insertSql = f"""
                     insert into public.scraping_celular(nombre, precio, url_celular, url_imagen)
                     values('{railway[0]}', '{railway[1]}', '{railway[2]}', '{railway[3]}');

                 """

    cur.execute(insertSql)
    conn.commit()
    cur.close()
    conn.close()



def truncateTable(tableName):
   conn = getConexion()
   cur = conn.cursor()

   truncateql = f"""
        truncate table {tableName}      
   """

   cur.execute(truncateql)
   conn.commit()
   cur.close()
   conn.close()