MySQL

-   sudo -- u root -p
-   Ctrl + L to clear screen

Creating a new user for a database

-   CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
-   GRANT ALL PRIVILEGES ON dbName.tableName TO 'username'@'localhost'
    IDENTIFIED BY 'password';

Database

-   Collection of data stored and accessed electronically

Database Management System

-   Collection of interrelated data and set of programs to access them.
    The goal of DBMS is to store and retrive data in a manner that is
    convenient and efficient.

Transactions

DDL, DML, DCL and TCL

-   UPDATE tablename

    SET colname1='theChange1', colname2='theChange2'

    WHERE \<some-conditions\>

    (if where clause is not included, changes will be made to ALL rows
    of the table)

-   DELETE FROM tablename

    WHERE \<some-conditions\>

    (DELETE removes rows, not columns)

-   DROP vs. DELETE vs. TRUNCATE

    -   <https://youtu.be/_m1aJdD-oD8>

    -   DROP is a DDL command (i.e.), it deals with the schema structure

    -   *DROP table tablename* deletes the existence of the entire table

    -   Thus, only DBA will be authorized to use DROP

    -   DELETE is a DML command

    -   It is used to delete *rows* of a table *conditionally*

    -   TRUNCATE is a DDL command

    -   It is used to delete ALL rows of a table (no condition), but
        does not delete the table itself (i.e.), DESC tablename will
        output the schema structure (with 0 records)

    -   DELETE from tablename vs. TRUNCATE tablename

    -   Both delete all rows from the table, but do not delete the table
        itself

    -   Differences

        -   TRUNCATE is faster because it locks the table and deletes
            all the records in one go
        -   DELETE is slower because it makes use of log to store each
            record before deleting it
        -   Thus, rollback before commit is possible in DELETE, but not
            in TRUNCATE

-   How to rollback a query

    -   <https://stackoverflow.com/questions/2356566/how-can-i-roll-back-my-last-delete-command-in-mysql>

-   Create user and grant permissions

    -   <https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql>

-   Check if a column exists in multiple tables
    ```sql
    SELECT table_name
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE column_name = 'Your col'
    ```
Resources

-   <http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm>
-   <https://www.mysqltutorial.org/>

Table manipulation and basic SQL

-   CREATE

-   INSERT

    -   INSERT INTO table_name(col_1, col_2, \...) VALUES(val1, val2,
        \...)

-   UPDATE

    -   UPDATE table_name SET col1=val1, col2=val2, \... WHERE \...

-   ADD CONSTRAINT

    -   Primary key vs. unique constraint

-   show columns from \<table-name\>

-   Viewing meta-data (information_schema)

    -   <https://dev.mysql.com/doc/mysql-infoschema-excerpt/8.0/en/information-schema-table-reference.html>

    -   Eg:

        select COLUMN_NAME

        from information_schema.KEY_COLUMN_USAGE

-   RENAME TO

    -   ALTER TABLE table_name RENAME TO new_table_name

-   WHERE clause 'helpers'

    -   OR, AND, NOT

    -   IN

        -   \... where col_name IN (value1, value2, \...)

    -   BETWEEN

        -   \... where col_name BETWEEN x and y
        -   applicable to dates as well

    -   Wildcard characters: % (placeholder for any number of
        characters); \_ (placeholder for one character)

-   GROUP BY

    -   used when you have an aggregate function and a column to
        aggregate on (see below eg.), more specifically, when you have a
        HAVING clause or when you use an aggregate function on a column,
        use GROUP BY for that column

    -   Use GROUP BY between WHERE and HAVING

    -   Using non-aggregated columns in the SELECT statement of a GROUP
        BY query (Short answer: Use inner join between the GROUP BY
        result and the original table) --
        <https://stackoverflow.com/questions/3168042/can-i-use-non-aggregate-columns-with-group-by>

-   HAVING

    -   comes after GROUP BY (see below eg.)

-   ORDER BY

-   Aggregate functions (5)

    -   AVG, COUNT, MIN, MAX, SUM

    -   SELECT count(col_name) FROM table_name;

    -   Count distinct (entries in a column)

        SELECT count(\*) FROM

        (SELECT DISTINCT col_to_count FROM table_name) distinct_records;

        COUNT(DISTINCT col_name) is also allowed

        COUNT(ALL col_name) counts only non-null values

    -   **SELECT** country, count(\*) **FROM** **table_name**

        **GROUP** **BY** country

        **HAVING** count(\*) \> 1

        **ORDER** **BY** count(\*), country

-   LIMIT *x *(at the end) returns* x* records* *

    -   alternate: LIMIT offset, x (ONLY integer literals are allowed)

-   LIKE "%something"; RLIKE "\<regex\>"

-   DISTINCT

    -   SELECT DISTINCT column_1, column_2, \... FROM table_name

-   Relational Operators

    -   UNION, MINUS, INTERSECTION

    -   SELECT col_1, col_2, ..

        FROM table_1

        WHERE \...

        MINUS

        SELECT col_1, col_2, ..

        FROM table_2

        WHERE \... ;

-   Pivot - <https://youtu.be/WMllKTpn7WE>

-   Column Aliases can only be used in GROUP BY, ORDER BY or HAVING
    clauses (not WHERE

-   IF - select if(condition, \<value if condition is true\>, \<value if
    condition is falss\>)

Storing results of queries for future use

-   <https://stackoverflow.com/questions/2233013/sql-how-do-i-refer-to-the-result-of-a-previous-query>
    (as per MS SQL)

    -   SQL variables

        -   set \@var_name = value;

    -   Temp Table

        -   CREATE TEMPORARY TABLE table_name

            SELECT \....

        -   CREATE TEMPORARY TABLE table_name(

            \<typical table creation syntax\>

            )

    -   Sub-query

-   

```{=html}
<!-- -->
```
-   

String functions

-   <https://www.mysqltutorial.org/mysql-string-functions/>

-   concat(s1, s2, \...)

-   instr(str, substr)

    -   returns position of first match

-   lower(str)

-   substring(str, start, length)

-   \<\>

Math functions

-   abs()
-   ceil()
-   floor()
-   round()
-   truncate()
-   mod()

Date functions

-   month(), monthname()

-   day(), dayofweek(), dayname()

-   year()

-   date_add(start_date, interval expr unit)

    -   date_add('2020-10-31', interval 1 day)

Joins

![](Pictures/10000201000003C6000002F8B214961A490D6DD7.png){width="17cm"
height="13.374cm"}

Examples that can be used:

-   Customer and Order
-   Martian-visitor
-   User Invoice
-   Generic

Views

-   Virtual tables that make it easy to search (not in terms of speed!)

    -   A view is primarily a means of masking or rearranging
        information so that it appears in a different format
    -   Or in other words, it is a saved result of a (complicated) query

-   Views provide security. By giving engineers only access to views,
    confidential data in the original table (if any) can be protected

-   They also provide simplicity (UNION example)

-   **CREATE** **VIEW** viewname **AS**

    **SELECT** col1, col2, col3, \...

    **FROM** tablename;

-   Are views updateable? (Yes, under certain conditions) --
    <https://stackoverflow.com/questions/3777918/is-a-view-in-the-database-updatable>

    -   Some of the conditions --

        -   The view is based on 1 table
        -   The view has the primary key of the table
        -   The view has not been defined using aggregrates, \...

-   <https://stackoverflow.com/questions/42241871/how-do-i-update-mysql-views-when-a-column-is-added-deleted-from-the-table>

    -   If the table is updated, the views that depend on the table will
        not be updated (view has to be ALTERed or DROPped-and-CREATEd
        again)

-   Tables vs. Views

    -   What happens when you add an index to a view?

Sequences

Built-in functions

-   Arithmetic
-   String manipulation

Indices

-   Used to speed up the process of retrieving data (like index in a
    book)

-   Good naming convention: tablename_colname_idx

-   **CREATE** **INDEX** idxname

    **ON** tablename(colnames);

-   However building index takes time

-   A database can have more than 1 index; an index can be made for more
    than one column (ORDER MATTERS!)

-   Indexes require storage; they also need to be updated whenever new
    records are inserted/ deleted/ updated.

-   Clustered vs. non-clustered index

    -   clustered index : non-clustered index :: phone book sorted
        alphabetically by first name : index on last name at the back of
        the phone book (page# \~ pointer to row)

-   

Questions to try again

-   Query the two cities in **STATION** with the shortest and longest
    *CITY* names, as well as their respective lengths (i.e.: number of
    characters in the name). If there is more than one smallest or
    largest city, choose the one that comes first when ordered
    alphabetically.
-   Median of a column
-   Ollivander's Wand --

**select** w\_\_.id, w\_\_.age, w\_\_.coins_needed, w\_\_.power

**from** (

**select** w.id, non_evil.age, w.coins_needed, w.power

**from** wands w

**inner** **join** (**select** **code**, age

**from** wands_property

**where** is_evil=0) non_evil

**on** w.**code**=non_evil.**code**

) w\_\_

**inner** **join** (

**select** w\_.age, min(w\_.coins_needed) **as** mincoins, w\_.power

**from** (

**select** w.id, non_evil.age, w.coins_needed, w.power

**from** wands w

**inner** **join** (**select** **code**, age

**from** wands_property

**where** is_evil=0) non_evil

**on** w.**code**=non_evil.**code**

) w\_

**group** **by** w\_.power, w\_.age

) m

**on** m.age=w\_\_.age **and** m.power=w\_\_.power **and**
m.mincoins=w\_\_.coins_needed

**order** **by** power **desc**, age **desc**;

Procedural SQL

-   Cursors
-   Exceptions

ER Diagrams

-   Entity, attributes, entity set

-   Relationship, descriptive attributes, relationship set

-   Attributes

-   Relationship types

Keys

-   Superkey

    -   No of superkeys = 2^\#\ non-prime\ attributes^

-   Candidate key

-   Primary key

Constraints

-   Primary key vs. Unique

Functional dependency

-   Trivial functional dependencies are of the form
    ![](Pictures/10000000000001E00000004B5A646DB247B7BE2F.png "texmaths"){width="2.823cm"
    height="0.444cm"}

Closure of F

Normalization

-   Normal forms

    -   to avoid redundancy
    -   to have easy access

-   Prime attributes -- any attribute that is part of a candidate key

-   1NF

    -   Attribute domain should be atomic

        -   No composite attribute
        -   No multivalued attribute

-   2NF

    -   No non-prime attribute should be partially dependent on any
        candidate key

-   3NF

    -   Every non-prime attribute should

        -   depend on every candidate key (candidate key defn. ?)
        -   never depend on only a part of a candidate key
        -   should not depend on other non-prime attributes

    (2NF and 3NF specify table design with respect to non-prime
    attributes)

-   BCNF

    -   All functional dependencies satisfy either of the 2:

        -   ![](Pictures/10000000000000E40000004B3E91FEEBE2393BB2.png "texmaths"){width="1.341cm"
            height="0.444cm"} is a trivial dependency
        -   ![](Pictures/100000000000002F00000026A58A4BA23B6D0943.png "texmaths"){width="0.278cm"
            height="0.227cm"} is a superkey of r(R) (r-\> relation; R
            -\> schema)

    -   A relation with 2 attributes is always in BCNF

    -   Decomposing a relation not in BCNF

-   4NF -- The only multivalued dependencies allowed are those on the
    key (Makes sense only if there are more than 2 attributes ?)

-   5NF -- It should not be possible to obtain the table from joining
    other tables

-   Yet to study:

    -   lossless decomposition
    -   **dependency preserving** decomposition
    -   Construct closure set of functional dependencies --
        <https://www.nielit.gov.in/gorakhpur/sites/default/files/Gorakhpur/Alevel_1_DBMS_12May2020_AV.pdf>
    -   How to handle composite and multi-valued attributes
    -   Representation of many-many relationships
    -   multivalued-dependency
    -   cursors

![](Pictures/10000201000004F3000002D57F3CA841F760F09D.png){width="17cm"
height="9.728cm"}

Database Design

-   <https://youtu.be/zHEEKq6GJq0>

-   <https://youtu.be/zBZEz1vZdIQ>

    -   Not a good idea to enforce application logic in the database
    -   Combining tables (eg: likes entity)

Transactions

-   Collection of operations that perform a single logical function in
    the database

To go over:

-   JOINS

    -   Examples for join
    -   Left join to inner join optimization

-   Views vs. Tables

    -   Where are views used?
    -   Applications of views in monitoring

-   Indexes

    -   Where are clustered and non-clustered indices used respectively?
    -   Finish watching video

-   SQL

    -   Extracting records that do not have a match in left join
    -   Built-in functions (arithmetic, string, datetime)
    -   Insert queries
    -   constraints (primary key, foreign key, not null, unique, check)

-   Procedures vs. Functions

-   Normalization vs. denormalization

-   ACID properties

-   COMMIT, ROLLBACK, ABORT

-   "keep table"

-   varchar2
