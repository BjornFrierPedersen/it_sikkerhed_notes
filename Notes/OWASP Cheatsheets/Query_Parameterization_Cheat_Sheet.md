---
title: "Query Parameterization Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html"
created: "1741872882.0882926"
tags: [owasp, cheatsheet, security]
---
# Query Parameterization

## Query Parameterization Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[¶](#references)](#stored-procedure-using-bind-variables-in-sql-run-with-exec)](#normal-stored-procedure_1)](#sql-server-using-transact-sql)](#stored-procedure-using-bind-variables-in-sql-run-with-execute)](#normal-stored-procedure)](#oracle-using-plsql)](#stored-procedure-examples)](#using-rust-with-sqlx)](#using-perl-with-database-independent-interface)](#using-cold-fusion-built-in-feature)](#using-php-with-php-data-objects)](#using-ruby-built-in-feature)](#using-ruby-with-activerecord)](#using-asp-net-built-in-feature)](#using-net-built-in-feature)](#using-java-with-hibernate)](#using-java-built-in-feature)](#prepared-statement-examples)](#parameterized-query-examples)](#introduction)](#query-parameterization-cheat-sheet)
### Introduction¶
[[[_content/dictionary#S|SQL]] Injection](https://owasp.org/www-community/attacks/SQL_Injection) is one of the most dangerous web vulnerabilities. So much so that it was the #1 item in both the [[[_content/dictionary#O|OWASP]] Top 10](https://owasp.org/Top10/A03_2021-Injection/) [2013 version](https://wiki.owasp.org/index.php/Top_10_2013-A1-Injection), and [2017 version](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection.html). As of 2021, it sits at #3 on the OWASP Top 10.
It represents a serious threat because SQL Injection allows evil attacker code to change the structure of a web application's SQL statement in a way that can steal data, modify data, or potentially facilitate command injection to the underlying [[_content/dictionary#O|OS]].
This cheat sheet is a derivative work of the [[SQL_Injection_Prevention_Cheat_Sheet|[SQL Injection Prevention Cheat Sheet]]](SQL_Injection_Prevention_Cheat_Sheet.html).
### Parameterized Query Examples¶
SQL Injection is best prevented through the use of [[SQL_Injection_Prevention_Cheat_Sheet|parameterized queries]]. The following chart demonstrates, with real-world code samples, how to build parameterized queries in most of the common web languages. The purpose of these code samples is to demonstrate to the web developer how to avoid SQL Injection when building database queries within a web application.
Please note, many client side frameworks and libraries offer client side query parameterization. These libraries often just build queries with string concatenation before sending raw queries to a server. Please ensure that query parameterization is done server-side!
#### Prepared Statement Examples¶
##### Using Java built-in feature¶
String custname = request.getParameter("customerName");
String query = "[[_content/dictionary#S|SELECT]] account_balance [[_content/dictionary#F|FROM]] user_data [[_content/dictionary#W|WHERE]] user_name = ? ";  
[[_content/dictionary#P|PreparedStatement]] pstmt = connection.prepareStatement( query );
pstmt.setString( 1, custname);
[[_content/dictionary#R|ResultSet]] results = pstmt.executeQuery( );

##### Using Java with Hibernate¶
// [[_content/dictionary#H|HQL]]
@Entity // declare as entity;
@[[_content/dictionary#N|NamedQuery]](
 name="findByDescription",
 query="[[_content/dictionary#F|FROM]] Inventory i [[_content/dictionary#W|WHERE]] i.productDescription = :productDescription"
)
public class Inventory implements Serializable {
 @Id
 private long id;
 private String productDescription;
}

// Use case
// This should [[_content/dictionary#R|REALLY]] be validated too
String userSuppliedParameter = request.getParameter("Product-Description");
// Perform input validation to detect attacks
List<Inventory> list =
 session.getNamedQuery("findByDescription")
 .setParameter("productDescription", userSuppliedParameter).list();

// Criteria [[_content/dictionary#A|API]]
// This should [[_content/dictionary#R|REALLY]] be validated too
String userSuppliedParameter = request.getParameter("Product-Description");
// Perform input validation to detect attacks
Inventory inv = (Inventory) session.createCriteria(Inventory.class).add
(Restrictions.eq("productDescription", userSuppliedParameter)).uniqueResult();

##### Using .[[_content/dictionary#N|NET]] built-in feature¶
String query = "[[_content/dictionary#S|SELECT]] account_balance [[_content/dictionary#F|FROM]] user_data [[_content/dictionary#W|WHERE]] user_name = ?";
try {
   [[_content/dictionary#O|OleDbCommand]] command = new OleDbCommand(query, connection);
   command.Parameters.Add(new [[_content/dictionary#O|OleDbParameter]]("customerName", [[_content/dictionary#C|CustomerName]] Name.Text));
   [[_content/dictionary#O|OleDbDataReader]] reader = command.[[_content/dictionary#E|ExecuteReader]]();
   // …
} catch ([[_content/dictionary#O|OleDbException]] se) {
   // error handling
}

##### Using [[_content/dictionary#A|ASP]] .[[_content/dictionary#N|NET]] built-in feature¶
string sql = "[[_content/dictionary#S|SELECT]] * [[_content/dictionary#F|FROM]] Customers [[_content/dictionary#W|WHERE]] [[_content/dictionary#C|CustomerId]] = @CustomerId";
[[_content/dictionary#S|SqlCommand]] command = new SqlCommand(sql);
command.Parameters.Add(new [[_content/dictionary#S|SqlParameter]]("@CustomerId", System.Data.[[_content/dictionary#S|SqlDbType]].Int));
command.Parameters["@CustomerId"].Value = 1;

##### Using Ruby with [[_content/dictionary#A|ActiveRecord]]¶
## Create
Project.create!(:name => 'owasp')
## Read
Project.all(:conditions => "name = ?", name)
Project.all(:conditions => { :name => name })
Project.where("name = :name", :name => name)
## Update
project.update_attributes(:name => 'owasp')
## Delete
Project.delete(:name => 'name')

##### Using Ruby built-in feature¶
insert_new_user = db.prepare "[[_content/dictionary#I|INSERT]] [[_content/dictionary#I|INTO]] users (name, age, gender) [[_content/dictionary#V|VALUES]] (?, ? ,?)"
insert_new_user.execute 'aizatto', '20', 'male'

##### Using [[_content/dictionary#P|PHP]] with PHP Data Objects¶
$stmt = $dbh->prepare("[[_content/dictionary#I|INSERT]] [[_content/dictionary#I|INTO]] [[_content/dictionary#R|REGISTRY]] (name, value) [[_content/dictionary#V|VALUES]] (:name, :value)");
$stmt->bindParam(':name', $name);
$stmt->bindParam(':value', $value);

##### Using Cold Fusion built-in feature¶
<cfquery name = "getFirst" dataSource = "cfsnippets">
    [[_content/dictionary#S|SELECT]] * [[_content/dictionary#F|FROM]] #strDatabasePrefix#_courses [[_content/dictionary#W|WHERE]] intCourseID =
    <cfqueryparam value = #intCourseID# CFSQLType = "CF_SQL_INTEGER">
</cfquery>

##### Using [[_content/dictionary#P|PERL]] with Database Independent Interface¶
my $sql = "[[_content/dictionary#I|INSERT]] [[_content/dictionary#I|INTO]] foo (bar, baz) [[_content/dictionary#V|VALUES]] ( ?, ? )";
my $sth = $dbh->prepare( $sql );
$sth->execute( $bar, $baz );

##### Using Rust with SQLx¶

// Input from [[_content/dictionary#C|CLI]] args but could be anything
let username = std::env::args().last().unwrap();

// Using build-in macros (compile time checks)
let users = sqlx::query_as!(
        User,
        "[[_content/dictionary#S|SELECT]] * [[_content/dictionary#F|FROM]] users [[_content/dictionary#W|WHERE]] name = ?",
        username
    )
    .fetch_all(&pool)
    .await 
    .unwrap();

// Using built-in functions
let users: Vec<User> = sqlx::query_as::<_, User>(
        "[[_content/dictionary#S|SELECT]] * [[_content/dictionary#F|FROM]] users [[_content/dictionary#W|WHERE]] name = ?"
    )
    .bind(&username)
    .fetch_all(&pool)
    .await
    .unwrap();

#### Stored Procedure Examples¶
The SQL you write in your web application isn't the only place that SQL injection vulnerabilities can be introduced. If you are using Stored Procedures, and you are dynamically constructing SQL inside them, you can also introduce SQL injection vulnerabilities.
Dynamic SQL can be parameterized using bind variables, to ensure the dynamically constructed SQL is secure.
Here are some examples of using bind variables in stored procedures in different databases.
##### Oracle using [[_content/dictionary#P|PL]]/[[_content/dictionary#S|SQL]]¶
###### ###### Normal Stored Procedure¶
No dynamic SQL being created. Parameters passed in to stored procedures are naturally bound to their location within the query without anything special being required:
[[_content/dictionary#P|PROCEDURE]] [[_content/dictionary#S|SafeGetBalanceQuery]](UserID varchar, Dept varchar) [[_content/dictionary#A|AS]] [[_content/dictionary#B|BEGIN]]
   [[_content/dictionary#S|SELECT]] balance [[_content/dictionary#F|FROM]] accounts_table [[_content/dictionary#W|WHERE]] user_ID = UserID [[_content/dictionary#A|AND]] department = Dept;
[[_content/dictionary#E|END]];

###### Stored Procedure Using Bind Variables in [[_content/dictionary#S|SQL]] Run with [[_content/dictionary#E|EXECUTE]]¶
Bind variables are used to tell the database that the inputs to this dynamic SQL are 'data' and not possibly code:
[[_content/dictionary#P|PROCEDURE]] [[_content/dictionary#A|AnotherSafeGetBalanceQuery]](UserID varchar, Dept varchar)
          [[_content/dictionary#A|AS]] stmt [[_content/dictionary#V|VARCHAR]](400); result [[_content/dictionary#N|NUMBER]];
[[_content/dictionary#B|BEGIN]]
   stmt := '[[_content/dictionary#S|SELECT]] balance [[_content/dictionary#F|FROM]] accounts_table [[_content/dictionary#W|WHERE]] user_ID = :1
            [[_content/dictionary#A|AND]] department = :2';
   EXECUTE [[_content/dictionary#I|IMMEDIATE]] stmt [[_content/dictionary#I|INTO]] result [[_content/dictionary#U|USING]] UserID, Dept;
   [[_content/dictionary#R|RETURN]] result;
[[_content/dictionary#E|END]];

##### [[_content/dictionary#S|SQL]] Server using Transact-SQL¶
Normal Stored Procedure¶
No dynamic SQL being created. Parameters passed in to stored procedures are naturally bound to their location within the query without anything special being required:
[[_content/dictionary#P|PROCEDURE]] [[_content/dictionary#S|SafeGetBalanceQuery]](@UserID varchar(20), @Dept varchar(10)) [[_content/dictionary#A|AS]] [[_content/dictionary#B|BEGIN]]
   [[_content/dictionary#S|SELECT]] balance [[_content/dictionary#F|FROM]] accounts_table [[_content/dictionary#W|WHERE]] user_ID = @UserID [[_content/dictionary#A|AND]] department = @Dept
[[_content/dictionary#E|END]]

###### Stored Procedure Using Bind Variables in [[_content/dictionary#S|SQL]] Run with [[_content/dictionary#E|EXEC]]¶
Bind variables are used to tell the database that the inputs to this dynamic SQL are 'data' and not possibly code:
[[_content/dictionary#P|PROCEDURE]] [[_content/dictionary#S|SafeGetBalanceQuery]](@UserID varchar(20), @Dept varchar(10)) [[_content/dictionary#A|AS]] [[_content/dictionary#B|BEGIN]]
   [[_content/dictionary#D|DECLARE]] @sql [[_content/dictionary#V|VARCHAR]](200)
   [[_content/dictionary#S|SELECT]] @sql = 'SELECT balance [[_content/dictionary#F|FROM]] accounts_table [[_content/dictionary#W|WHERE]] '
                 + 'user_ID = @[[_content/dictionary#U|UID]] [[_content/dictionary#A|AND]] department = @[[_content/dictionary#D|DPT]]'
   EXEC sp_executesql @sql,
                      '@UID VARCHAR(20), @DPT VARCHAR(10)',
                      @UID=@UserID, @DPT=@Dept
[[_content/dictionary#E|END]]

### References¶

[- The Bobby Tables site (inspired by the [[_content/dictionary#X|XKCD]] webcomic) has numerous examples in different languages of parameterized Prepared Statements and Stored Procedures](http://bobby-tables.com/)
- [[_content/dictionary#O|OWASP]] [[_content/dictionary#S|SQL]] Injection Prevention Cheat Sheet