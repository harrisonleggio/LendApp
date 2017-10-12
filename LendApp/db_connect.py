import pyodbc

def db_execute(sql_query):
    cnxn = pyodbc.connect(
        Driver='{SQL Server}',
        host='HARRISONS-THINK',
        database='LendApp',
        trusted_connection='yes'
    )
    cursor = cnxn.cursor()
    cursor.execute(sql_query)
    cursor.commit()
    cnxn.close()

    return 'Insert Completed'

