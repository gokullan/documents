# PostgreSQL

-   `sudo -i -u postgres`
-   `\psql` for Postgres shell
-   `\password` to change password
-   Default port: 5432
-   `\conninfo`
-   `IN`: The IN operator is a good early demonstrator of the elegance of the relational model. The argument it takes is not just a list of values - it's actually a table with a single column. Since queries also return tables, if you create a query that returns a single column, you can feed those results into an IN operator. To give a toy example: 
```
SELECT CASE expression
    WHEN value THEN result2
    [WHEN ...]
    [ELSE result2]
    END
```

## Date
-   `yyyy-mm-dd hh:mm:ss` format
