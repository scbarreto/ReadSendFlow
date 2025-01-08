import sqlite3
from sqlite3 import Error

#-------------------------------------------------------------------------------
#--------------- Data Base -----------------------------------------------------
def setupdb():

    database = "pythonsqlite.db"   
    sql_create_flux_table = """ CREATE TABLE IF NOT EXISTS fluxo (
                                        date text PRIMARY KEY,
                                        flux text,
                                        volum text
                                    );"""
                                

    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_flux_table)
        
       
    else:
        print("Error! cannot create the database connection.")


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn
    
    
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        

        
#---------------------------------------------------------------------------------------------
#-------------------- Inserting data into Table 1 - Flux Table -------------------------------
#---------------------------------------------------------------------------------------------

     
        
def insertVariableIntoTable1(date, flux, volum):
    try:
        sqliteConnection = sqlite3.connect('pythonsqlite.db')
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO 'fluxo'
                          ('date', 'flux', 'volum') 
                          VALUES (?, ?, ?);"""

        data_tuple = (date, flux, volum)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into fluxo table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)

