    
    data from database
    >>> import petl as etl
    >>> import sqlite3
    >>> connection = sqlite3.connect('example.db')
    >>> table = etl.fromdb(connection, 'SELECT * FROM example')

    data to database
    >>> import petl as etl
    >>> table = [['foo', 'bar'],
    ...          ['a', 1],
    ...          ['b', 2],
    ...          ['c', 2]]
    >>> # using sqlite3
    ... import sqlite3
    >>> connection = sqlite3.connect('example.db')
    >>> # assuming table "foobar" already exists in the database
    ... etl.todb(table, connection, 'foobar')