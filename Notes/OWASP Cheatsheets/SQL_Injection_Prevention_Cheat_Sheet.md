---
title: "SQL Injection Prevention Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html"
created: "1741872882.1561644"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#S|SQL]] Injection Prevention

## [[[[_content/dictionary#S|SQL]] Injection](https://owasp.org/www-community/attacks/SQL_Injection)](https://owasp.org/www-community/attacks/SQL_Injection) Prevention Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#related-articles)](#allow-list-input-validation)](#enhancing-least-privilege-with-sql-views)](#least-admin-privileges-for-multiple-dbs)](#details-of-least-privilege-when-developing)](#minimizing-application-and-os-privileges)](#least-privilege)](#additional-defenses)](#defense-option-4-strongly-discouraged-escaping-all-user-supplied-input)](#sample-of-safer-dynamic-query-generation-discouraged)](#safest-use-of-dynamic-sql-generation-discouraged)](#sample-of-safe-table-name-validation)](#defense-option-3-allow-list-input-validation)](#safe-vb-net-stored-procedure-example)](#safe-java-stored-procedure-example)](#when-stored-procedures-can-increase-risk)](#safe-approach-to-stored-procedures)](#defense-option-2-stored-procedures)](#other-examples-of-safe-prepared-statements)](#hibernate-query-language-hql-prepared-statement-named-parameters-example)](#safe-c-net-prepared-statement-example)](#safe-java-prepared-statement-example)](#defense-option-1-prepared-statements-with-parameterized-queries)](#primary-defenses)](#anatomy-of-a-typical-sql-injection-vulnerability)](#what-is-a-sql-injection-attack)](#introduction)](#sql-injection-prevention-cheat-sheet)
### Introduction¶
This cheat sheet will help you prevent SQL injection flaws in your applications. It will define what SQL injection is, explain where those flaws occur, and provide four options for defending against SQL injection attacks. SQL Injection attacks are common because:

1. [[_content/dictionary#S|SQL]] Injection vulnerabilities are very common, and
2. The application's database is a frequent target for attackers because it typically contains interesting/critical data.

### What Is a [[_content/dictionary#S|SQL]] Injection Attack?¶
Attackers can use SQL injection on an application if it has dynamic database queries that use string concatenation and user supplied input. To avoid SQL injection flaws, developers need to:

1. Stop writing dynamic queries with string concatenation or
2. Prevent malicious [[_content/dictionary#S|SQL]] input from being included in executed queries.

There are simple techniques for preventing SQL injection vulnerabilities and they can be used with practically any kind of programming language and any type of database. While [[_content/dictionary#X|XML]] databases can have similar problems (e.g., [[_content/dictionary#X|XPath]] and XQuery injection), these techniques can be used to protect them as well.
### Anatomy of A Typical [[_content/dictionary#S|SQL]] Injection Vulnerability¶
A common SQL injection flaw in Java is below. Because its unvalidated "customerName" parameter is simply appended to the query, an attacker can enter SQL code into that query and the application would take the attacker's code and execute it on the database.
String query = "[[_content/dictionary#S|SELECT]] account_balance [[_content/dictionary#F|FROM]] user_data [[_content/dictionary#W|WHERE]] user_name = "
             + request.getParameter("customerName");
try {
    Statement statement = connection.createStatement( ... );
    [[_content/dictionary#R|ResultSet]] results = statement.executeQuery( query );
}

...

### Primary Defenses¶

- Option 1: Use of Prepared Statements (with Parameterized Queries)
- Option 2: Use of Properly Constructed Stored Procedures
- Option 3: - Allow-list Input Validation
- Option 4: [[_content/dictionary#S|STRONGLY]] [[_content/dictionary#D|DISCOURAGED]]: Escaping All User Supplied Input

#### Defense Option 1: Prepared Statements (with Parameterized Queries)¶
When developers are taught how to write database queries, they should be told to use prepared statements with variable binding (aka parameterized queries). Prepared statements are simple to write and easier to understand than dynamic queries, and parameterized queries force the developer to define all [[_content/dictionary#S|SQL]] code first and pass in each parameter to the query later.
If database queries use this coding style, the database will always distinguish between code and data, regardless of what user input is supplied. Also, prepared statements ensure that an attacker cannot change the intent of a query, even if SQL commands are inserted by an attacker.
##### Safe Java Prepared Statement Example¶
In the safe Java example below, if an attacker were to enter the userID as tom' or '1'='1, the parameterized query would look for a username that literally matches the entire string tom' or '1'='1. Thus, the database would be protected against injections of malicious SQL code.
The following code example uses a [[_content/dictionary#P|PreparedStatement]], Java's implementation of a parameterized query, to execute the same database query.
// This should [[_content/dictionary#R|REALLY]] be validated too
String custname = request.getParameter("customerName");
// Perform input validation to detect attacks
String query = "[[_content/dictionary#S|SELECT]] account_balance [[_content/dictionary#F|FROM]] user_data [[_content/dictionary#W|WHERE]] user_name = ? ";
PreparedStatement pstmt = connection.prepareStatement( query );
pstmt.setString( 1, custname);
[[_content/dictionary#R|ResultSet]] results = pstmt.executeQuery( );

##### Safe C# .[[_content/dictionary#N|NET]] Prepared Statement Example¶
In .NET, the creation and execution of the query doesn't change. Just pass the parameters to the query using the Parameters.Add() call as shown below.
String query = "[[_content/dictionary#S|SELECT]] account_balance [[_content/dictionary#F|FROM]] user_data [[_content/dictionary#W|WHERE]] user_name = ?";
try {
  [[_content/dictionary#O|OleDbCommand]] command = new OleDbCommand(query, connection);
  command.Parameters.Add(new [[_content/dictionary#O|OleDbParameter]]("customerName", [[_content/dictionary#C|CustomerName]] Name.Text));
  [[_content/dictionary#O|OleDbDataReader]] reader = command.[[_content/dictionary#E|ExecuteReader]]();
  // …
} catch ([[_content/dictionary#O|OleDbException]] se) {
  // error handling
}

While we have shown examples in Java and .[[_content/dictionary#N|NET]], practically all other languages (including Cold Fusion and Classic [[_content/dictionary#A|ASP]]) support parameterized query interfaces. Even [[_content/dictionary#S|SQL]] abstraction layers, like the [Hibernate Query Language](http://hibernate.org/) (HQL) with the same type of injection problems (called [HQL Injection](http://cwe.mitre.org/data/definitions/564.html))  support parameterized queries as well:
##### Hibernate Query Language ([[_content/dictionary#H|HQL]]) Prepared Statement (Named Parameters) Example¶
// This is an unsafe HQL statement
Query unsafeHQLQuery = session.createQuery("from Inventory where productID='"+userSuppliedParameter+"'");
// Here is a safe version of the same query using named parameters
Query safeHQLQuery = session.createQuery("from Inventory where productID=:productid");
safeHQLQuery.setParameter("productid", userSuppliedParameter);

##### Other Examples of Safe Prepared Statements¶
If you need examples of prepared queries/parameterized languages, including Ruby, [[_content/dictionary#P|PHP]], Cold Fusion, Perl, and Rust, see the [[Query_Parameterization_Cheat_Sheet|Query Parameterization Cheat Sheet]] or this [site](http://bobby-tables.com/).
Generally, developers like prepared statements because all the [[_content/dictionary#S|SQL]] code stays within the application, which makes applications relatively database independent.
#### Defense Option 2: Stored Procedures¶
Though stored procedures are not always safe from SQL injection, developers can use certain standard stored procedure programming constructs. This approach has the same effect as using parameterized queries, as long as the stored procedures are implemented safely (which is the norm for most stored procedure languages).
##### Safe Approach to Stored Procedures¶
If stored procedures are needed, the safest approach to using them requires the developer to build SQL statements with parameters that are automatically parameterized, unless the developer does something largely out of the norm. The difference between prepared statements and stored procedures is that the SQL code for a stored procedure is defined and stored in the database itself, then called from the application. Since prepared statements and safe stored procedures are equally effective in preventing SQL injection, your organization should choose the approach that makes the most sense for you.
##### When Stored Procedures Can Increase Risk¶
Occasionally, stored procedures can increase risk when a system is attacked. For example, on [[_content/dictionary#M|MS]] SQL Server, you have three main default roles: db_datareader, db_datawriter and db_owner. Before stored procedures came into use, DBAs would give db_datareader or db_datawriter rights to the webservice's user, depending on the requirements.
However, stored procedures require execute rights, a role not available by default. In some setups where user management has been centralized, but is limited to those 3 roles, web apps would have to run as db_owner so stored procedures could work. Naturally, that means that if a server is breached, the attacker has full rights to the database, where previously, they might only have had read-access.
##### Safe Java Stored Procedure Example¶
The following code example uses Java's implementation of the stored procedure interface ([[_content/dictionary#C|CallableStatement]]) to execute the same database query. The sp_getAccountBalance stored procedure has to be predefined in the database and use the same functionality as the query above.
// This should [[_content/dictionary#R|REALLY]] be validated
String custname = request.getParameter("customerName");
try {
  CallableStatement cs = connection.prepareCall("{call sp_getAccountBalance(?)}");
  cs.setString(1, custname);
  [[_content/dictionary#R|ResultSet]] results = cs.executeQuery();
  // … result set handling
} catch (SQLException se) {
  // … logging and error handling
}

##### Safe [[_content/dictionary#V|VB]] .[[_content/dictionary#N|NET]] Stored Procedure Example¶
The following code example uses a [[_content/dictionary#S|SqlCommand]], .NET's implementation of the stored procedure interface, to execute the same database query. The sp_getAccountBalance stored procedure must be predefined in the database and use the same functionality as the query defined above.
 Try
   Dim command As SqlCommand = new SqlCommand("sp_getAccountBalance", connection)
   command.[[_content/dictionary#C|CommandType]] = CommandType.[[_content/dictionary#S|StoredProcedure]]
   command.Parameters.Add(new [[_content/dictionary#S|SqlParameter]]("@[[_content/dictionary#C|CustomerName]]", CustomerName.Text))
   Dim reader As [[_content/dictionary#S|SqlDataReader]] = command.[[_content/dictionary#E|ExecuteReader]]()
   '...
 Catch se As [[_content/dictionary#S|SqlException]]
   'error handling
 End Try

#### Defense Option 3: #### Allow-list Input Validation¶
If you are faced with parts of [[_content/dictionary#S|SQL]] queries that can't use bind variables, such as table names, column names, or sort order indicators ([[_content/dictionary#A|ASC]] or [[_content/dictionary#D|DESC]]), input validation or query redesign is the most appropriate defense. When table or column names are needed, ideally those values come from the code and not from user parameters.
##### Sample Of Safe Table Name Validation¶
[[_content/dictionary#W|WARNING]]: Using user parameter values to target table or column names is a symptom of poor design and a full rewrite should be considered if time allows. If that is not possible, developers should map the parameter values to the legal/expected table or column names to make sure unvalidated user input doesn't end up in the query.
In the example below, since tableName is identified as one of the legal and expected values for a table name in this query, it can be directly appended to the SQL query. Keep in mind that generic table validation functions can lead to data loss if table names are used in queries where they are not expected.
String tableName;
switch([[_content/dictionary#P|PARAM]]):
  case "Value1": tableName = "fooTable";
                 break;
  case "Value2": tableName = "barTable";
                 break;
  ...
  default      : throw new [[_content/dictionary#I|InputValidationException]]("unexpected value provided"
                                                  + " for table name");

##### Safest Use Of Dynamic [[_content/dictionary#S|SQL]] Generation ([[_content/dictionary#D|DISCOURAGED]])¶
When we say a stored procedure is "implemented safely," that means it does not include any unsafe dynamic SQL generation. Developers do not usually generate dynamic SQL inside stored procedures. However, it can be done, but should be avoided.
If it can't be avoided, the stored procedure must use input validation or proper escaping, as described in this article, to make sure that all user supplied input to the stored procedure can't be used to inject SQL code into the dynamically generated query. Auditors should always look for uses of sp_execute, execute or exec within SQL Server stored procedures. Similar audit guidelines are necessary for similar functions for other vendors.
##### Sample of Safer Dynamic Query Generation ([[_content/dictionary#D|DISCOURAGED]])¶
For something simple like a sort order, it is best if the user supplied input is converted to a boolean, and then that boolean is used to select the safe value to append to the query. This is a very standard need in dynamic query creation.
For example:
public String someMethod(boolean sortOrder) {
 String SQLquery = "some SQL ... order by Salary " + (sortOrder ? "[[_content/dictionary#A|ASC]]" : "[[_content/dictionary#D|DESC]]");`
 ...

Any time user input can be converted to a non-String, like a date, numeric, boolean, enumerated type, etc. before it is appended to a query, or used to select a value to append to the query, this ensures it is safe to do so.
Input validation is also recommended as a secondary defense in [[_content/dictionary#A|ALL]] cases, even when using bind variables as discussed earlier in this article. More techniques on how to implement strong input validation is described in the [[Input_Validation_Cheat_Sheet|[Input Validation Cheat Sheet]]](Input_Validation_Cheat_Sheet.html).
#### Defense Option 4: [[_content/dictionary#S|STRONGLY]] [[_content/dictionary#D|DISCOURAGED]]: Escaping All User-Supplied Input¶
In this approach, the developer will escape all user input before putting it in a query. It is very database specific in its implementation.  This methodology is frail compared to other defenses, and we [[_content/dictionary#C|CANNOT]] guarantee that this option will prevent all [[_content/dictionary#S|SQL]] injections in all situations.
If an application is built from scratch or requires low risk tolerance, it should be built or re-written using parameterized queries, stored procedures, or some kind of Object Relational Mapper ([[_content/dictionary#O|ORM]]) that builds your queries for you.
### Additional Defenses¶
Beyond adopting one of the four primary defenses, we also recommend adopting all of these additional defenses to provide defense in depth. These additional defenses are:

- Least Privilege
Allow-list Input Validation

#### Least Privilege¶
To minimize the potential damage of a successful SQL injection attack, you should minimize the privileges assigned to every database account in your environment. Start from the ground up to determine what access rights your application accounts require, rather than trying to figure out what access rights you need to take away.
Make sure that accounts that only need read access are only granted read access to the tables they need access to. [[_content/dictionary#D|DO]] [[_content/dictionary#N|NOT]] [[_content/dictionary#A|ASSIGN]] [[_content/dictionary#D|DBA]] [[_content/dictionary#O|OR]] [[_content/dictionary#A|ADMIN]] [[_content/dictionary#T|TYPE]] [[_content/dictionary#A|ACCESS]] [[_content/dictionary#T|TO]] [[_content/dictionary#Y|YOUR]] [[_content/dictionary#A|APPLICATION]] [[_content/dictionary#A|ACCOUNTS]]. We understand that this is easy, and everything just "works" when you do it this way, but it is very dangerous.
##### Minimizing Application and [[_content/dictionary#O|OS]] Privileges¶
SQL injection is not the only threat to your database data. Attackers can simply change the parameter values from one of the legal values they are presented with, to a value that is unauthorized for them, but the application itself might be authorized to access. As such, minimizing the privileges granted to your application will reduce the likelihood of such unauthorized access attempts, even when an attacker is not trying to use SQL injection as part of their exploit.
While you are at it, you should minimize the privileges of the operating system account that the [[_content/dictionary#D|DBMS]] runs under. Don't run your DBMS as root or system! Most DBMSs run out of the box with a very powerful system account. For example, MySQL runs as system on Windows by default! Change the DBMS's OS account to something more appropriate, with restricted privileges.
##### Details Of Least Privilege When Developing¶
If an account only needs access to portions of a table, consider creating a view that limits access to that portion of the data and assigning the account access to the view instead of the underlying table. Rarely, if ever, grant create or delete access to database accounts.
If you adopt a policy where you use stored procedures everywhere, and don't allow application accounts to directly execute their own queries, then restrict those accounts to only be able to execute the stored procedures they need. Don't grant them any rights directly to the tables in the database.
##### Least Admin Privileges For Multiple DBs¶
The designers of web applications should avoid using the same owner/admin account in the web applications to connect to the database. Different [[_content/dictionary#D|DB]] users should be used for different web applications.
In general, each separate web application that requires access to the database should have a designated database user account that the application will use to connect to the DB. That way, the designer of the application can have good granularity in the access control, thus reducing the privileges as much as possible. Each DB user will then have select access to only what it needs, and write-access as needed.
As an example, a login page requires read access to the username and password fields of a table, but no write access of any form (no insert, update, or delete). However, the sign-up page certainly requires insert privilege to that table; this restriction can only be enforced if these web apps use different DB users to connect to the database.
##### Enhancing Least Privilege with [[_content/dictionary#S|SQL]] Views¶
You can use SQL views to further increase the granularity of access by limiting the read access to specific fields of a table or joins of tables. It could have additional benefits.
For example, if the system is required (perhaps due to some specific legal requirements) to store the passwords of the users, instead of salted-hashed passwords, the designer could use views to compensate for this limitation. They could revoke all access to the table (from all DB users except the owner/admin) and create a view that outputs the hash of the password field and not the field itself.
Any SQL injection attack that succeeds in stealing DB information will be restricted to stealing the hash of the passwords (could even be a keyed hash), since no DB user for any of the web applications has access to the table itself.
Allow-list Input Validation¶
In addition to being a primary defense when nothing else is possible (e.g., when a bind variable isn't legal), input validation can also be a secondary defense used to detect unauthorized input before it is passed to the SQL query. For more information please see the Input Validation Cheat Sheet. Proceed with caution here. Validated data is not necessarily safe to insert into SQL queries via string building.
### Related Articles¶
SQL Injection Attack Cheat Sheets:
The following articles describe how to exploit different kinds of SQL injection vulnerabilities on various platforms (that this article was created to help you avoid):

[- [[_content/dictionary#S|SQL]] Injection Cheat Sheet](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/)
Bypassing [[_content/dictionary#W|WAF]]'s with SQLi - [SQL Injection Bypassing WAF](https://owasp.org/www-community/attacks/SQL_Injection_Bypassing_WAF)

Description of [[_content/dictionary#S|SQL]] Injection Vulnerabilities:

- [[_content/dictionary#O|OWASP]] article on [[_content/dictionary#S|SQL]] Injection Vulnerabilities
OWASP article on [Blind_SQL_Injection](https://owasp.org/www-community/attacks/Blind_SQL_Injection) Vulnerabilities

How to Avoid [[_content/dictionary#S|SQL]] Injection Vulnerabilities:

[[[_content/dictionary#O|OWASP]] Developers Guide](https://github.com/OWASP/[[_content/dictionary#D|DevGuide]]) article on how to avoid [[_content/dictionary#S|SQL]] injection vulnerabilities
OWASP Cheat Sheet that provides [[Query_Parameterization_Cheat_Sheet|numerous language specific examples of parameterized queries using both Prepared Statements and Stored Procedures]]
[- The Bobby Tables site (inspired by the [[_content/dictionary#X|XKCD]] webcomic) has numerous examples in different languages of parameterized Prepared Statements and Stored Procedures](http://bobby-tables.com/)

How to [Review Code for [[_content/dictionary#S|SQL]] Injection](https://wiki.owasp.org/index.php/Reviewing_Code_for_SQL_Injection) Vulnerabilities:

[[[_content/dictionary#O|OWASP]] Code Review Guide](https://wiki.owasp.org/index.php/Category:OWASP_Code_Review_Project) article on how to Review Code for [[_content/dictionary#S|SQL]] Injection Vulnerabilities

How to [Test for [[_content/dictionary#S|SQL]] Injection](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection.html) Vulnerabilities:

[[[_content/dictionary#O|OWASP]] Testing Guide](https://owasp.org/www-project-web-security-testing-guide) article on how to Test for [[_content/dictionary#S|SQL]] Injection Vulnerabilities