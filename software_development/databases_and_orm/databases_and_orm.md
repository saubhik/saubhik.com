# Databases and ORM

There are 2 types of data:
1. Transient data
2. Persistent data

Persistent data is stored in a database and transient data are the logical data used in programming
logic.

The database system consists of:
1. Application program / queries: consists of the application logic and queries interact with
the DBMS for data storage/retrieval.
2. DBMS software: performs the queries of the application and performs storage/retrieval.
3. Stored data: place where the data is stored.

Commands in SQL are categorised into:
1. Data Definition Language: create a new schema (showing relations between tables) or modify
the existing schema, eg `create`, `alter`, `drop`.
2. Data Manipulation Language: eg `select`, `insert`, `update`, `delete` queries.

`select * from employee where fname like %ee%;` command will select those employees whose name
contains 'ee'. Th `%` character replaces any number of preceding or trailing characters.

`select sex, count(*) as "no of employees"
from employee
group by sex;` finds the number of male and female employees in a company.

`having` clause is used to apply filter based on aggregated value. `where` is applied before the
aggregation takes place.

`select dno, avg(salary)
from employee
group by dno
having avg(salary) > 30000;` to find all departments whose average salary is greater than 30k.

### ORMs
ORMs come when trying to understand how object oriented Java program interacts with the RDBMS.
Object relational mapping(ORM) helps to translate the object-oriented data model to a relational 
database, such that it maps certain class with its corresponding table in the database, for 
example, Employee class in the java program is mapped to the employee table. 
1. One to many relationship - This relationship is established between the tables by adding 
the primary key of one table as a foreign key of the other table.
2. Many to many relationship - This relationship between two tables is established by creating a 
new table with the columns consists of the primary keys of both the tables

Database drivers are programs or files that help connect a generic interface (such as a Java 
program) to a specific database and translates the instructions and information in ways that 
both the program and the interface can understand. Often, these database drivers are JAR files, 
which when included in our Java programs, would enable a connection between the program and 
the database.

Java Database Connectivity (JDBC) is an API that defines how a user can access a database by making 
a connection to the database, then executing query on that database, and finally processing 
the results of the applied query.

Some of the disadvantages of using JDBC:
1. It supports only native SQL and developer needs to write the optimized query. So, if we 
change the database from MySql to Postgres, we might need to change the SQL query signatures. 
For example, LongText data type is in MySql but not in Postgres, so the same query might run 
well on MySql but not in Postgres
2. We are combining java code and SQL queries together and, thus, they become tightly coupled. 
So, if we change the data type of a particular column in a table, we have to modify the query 
everywhere in the code.
3. We need to manually take care of the conversion from a plain Java object (POJO) to RDBMS 
relations, and vice-versa. We have to manually decide the data type mapping. And during 
retrieval of data, we have to specifically mention the column name and data type for retrieval.
4. We as humans might not end up writing each SQL query correctly.
5. Since we may not write each SQL correctly, JDBC would throw SQL exceptions in case of errors, 
and you would have to write Try catch block in your code. This makes your job more difficult.
Secondly, you would have to write a separate query to add each entry in a table, so the amount 
of SQL code you need to write for building a large database becomes substantially huge and 
repetitive.

This is where the ORM comes in, which created this natural mapping. It automatically maps your 
classes to tables, class variables to columns, and instances variables to rows.

Frameworks that implement ORM concepts are —
Hibernate : Jboss, Ibatis : Apache, Toplink : Oracle, OJB : Apache, JDO : Adobe


