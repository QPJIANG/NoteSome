    >>> import petl as etl
    >>> cols = [[0, 1, 2], ['a', 'b', 'c']]
    >>> tbl = etl.fromcolumns(cols)
    >>> import petl as etl
    >>> import csv
    >>> # set up a CSV file to demonstrate with
    ... table1 = [['foo', 'bar'],
    ...           ['a', 1],
    ...           ['b', 2],
    ...           ['c', 2]]
    >>> with open('example.csv', 'w') as f:
    ...     writer = csv.writer(f)
    ...     writer.writerows(table1)
    ...
    >>> # now demonstrate the use of fromcsv()
    ... table2 = etl.fromcsv('example.csv')
    etl.tocsv(table1, 'example.csv')
