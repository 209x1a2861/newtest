import psycopg2
def connect():
    try:
        conn=psycopg2.connect(host="db-test.c3ifm9isoxne.eu-north-1.rds.amazonaws.com",
                              port="5432",dbname="postgres",user="sai9999",password="sai12077"
            
        )
        cursor=conn.cursor()
        data=cursor.execute("SELECT * FROM pg_catalog.pg_tables")
        cursor.fetchall()
        print("db connected!")
    except Exception as e:
        print("error occured",e)
connect()

        