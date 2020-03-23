def createDatabase():
    import sqlite3

    conn = sqlite3.connect("dbpokemon.sqlite3")
    cur = conn.cursor()

    # Creating a table for list of pokemon.
    cur.execute("""
        create table if not exists pokemon(
        id int primary key,
        Name varchar(20) not null,
        type int not null,
        attack1 varchar(20),
        attack2 varchar(20),
        attack3 varchar(20),
        attack4 varchar(20)
        ) ;
        """)
