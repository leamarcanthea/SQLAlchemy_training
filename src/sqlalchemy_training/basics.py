from sqlalchemy import create_engine, text


engine = create_engine('sqlite+pysqlite:///mydatabase.db', echo=True) #echo = True to see what is going on exactly
#1> what type of db we are communicating with? here: sqlite
#2> what DBAPI: here pysqlite, but by default it is this driver for sqlite so falcutative
#3> URL of where is the base of interest
#####For now: no data loading, no connexion established.
conn = engine.connect()
conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))
conn.commit()