# PostgreSQL

## Login
-   `sudo -i -u postgres` to go to PostgreSQL admin terminal
    -   `\psql` for Postgres shell
    -   Alternate: `sudo -u postgres psql`
-   `psql -U username -d dbname` to log in using a different username and access
    `dbname` 
    -   `-d dbname` if not provided, psql will try to access the default
        database (the same name as the username) which may not exist

## Access
```sql
CREATE USER [username] WITH PASSWORD '[password]';
CREATE DATABASE [dbname];
GRANT ALL PRIVILEGES ON DATABASE [dbname] to [username];
```
- [PEER Authentication Error](https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge)
  - Create a new entry in `pg_hba.conf` for the required user.

## Administration
-   Add `psql -U ... -f file.sql` to execute the file on a database

## `psql`
-   `\password` to change password
-   Default port: 5432
-   `\conninfo`
-   `\du` or `\du+` to list users
-   `\l` to list databases
-   `\c database_name` to use (/switch to) a database
-   `\dt` to show tables
-   UUID
    -   `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";` to install extension first
    -   `SELECT uuid_generate_v4()`
-   `IN`: The IN operator is a good early demonstrator of the elegance of the
    relational model. The argument it takes is not just a list of values - it's
    actually a table with a single column. Since queries also return tables, if
    you create a query that returns a single column, you can feed those results
    into an IN operator. To give a toy example: 
```
SELECT CASE expression
    WHEN value THEN result2
    [WHEN ...]
    [ELSE result2]
    END
```

## Date
-   `yyyy-mm-dd hh:mm:ss +0530` format

## `jsonb` 
- Update a `jsonb` field
```sql
update table_t set json_col=
jsonb_set(json_col,'{dict,org,employees,3}',
'{"name":"tom", "email": "tom@gmail.com" }')
```
where 3 refers to an index
- Checking boolean values
```sql
SELECT * FROM table
WHERE (data->>'bool_property')::boolean
```
- Check if property exists: `... WHERE (json->'attribute') IS NOT null`
- JSON Path Expressions: 
  - Example: `'$.line_items.*[*].status ? (@ == "Something")'`
  - `*` is a wildcard; `?` is used for text-return; `@` refers to the current value
- Operators
  - `@>` : To check if jsonb on the right as present as a top-level element on the jsonb present on the left
  - `@?`, `?`, `?|`, ...
  - [Documentation](https://www.postgresql.org/docs/16/functions-json.html#FUNCTIONS-JSONB-OP-TABLE)
- [jsonb indexing](https://youtu.be/p9RItyeKbLQ?si=YzFDNvW9c6F92hei)
- [GIN Indexing Questions](https://postgrespro.com/list/thread-id/2663248)

## Resources
-   [ntu.edu.sg](https://www3.ntu.edu.sg/home/ehchua/programming/sql/PostgreSQL_GetStarted.html)
