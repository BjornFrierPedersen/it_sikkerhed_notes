---
title: "Mass Assignment Cheat Sheet"
source: "OWASP Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html"
created: "1741872882.0007052"
tags: [owasp, cheatsheet, security]
---
# Mass Assignment

## Mass Assignment Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#references-and-future-reading)](#flexjson-json-object-mapper)](#json-lib-json-object-mapper)](#gson-json-object-mapper)](#jackson-json-object-mapper)](#play)](#grails)](#block-listing_2)](#allow-listing_2)](#php-laravel-eloquent)](#asp-net)](#django)](#ruby-on-rails)](#block-listing_1)](#allow-listing_1)](#nodejs-mongoose)](#block-listing)](#allow-listing)](#spring-mvc)](#language-framework-specific-solutions)](#general-solutions)](#solutions)](#github-case-study)](#exploitability)](#example)](#alternative-names)](#definition)](#introduction)](#mass-assignment-cheat-sheet)
### Introduction¶
#### Definition¶
Software frameworks sometimes allow developers to automatically bind HTTP request parameters into program code variables or objects to make using that framework easier on developers. This can sometimes cause harm.
Attackers can sometimes use this methodology to create new parameters that the developer never intended which in turn creates or overwrites new variable or objects in program code that was not intended.
This is called a Mass Assignment vulnerability.
#### Alternative Names¶
Depending on the language/framework in question, this vulnerability can have several [alternative names](https://cwe.mitre.org/data/definitions/915.html):

- Mass Assignment: Ruby on Rails, NodeJS.
- Autobinding: Spring MVC, ASP NET MVC.
- Object injection: PHP.

#### Example¶
Suppose t[[[[[[[[[[[[[[[[[here](http://flexjson.sourceforge.net/#Serialization)](http://json-lib.sourceforge.net/advanced.html)](https://stackoverflow.com/a/27986860)](https://sites.google.com/site/gson/gson-user-guide#TOC-Excluding-Fields-From-Serialization-and-Deserialization)](http://lifelongprogrammer.blogspot.com/2015/09/using-jackson-view-to-protect-mass-assignment.html)](https://www.baeldung.com/jackson-field-serializable-deserializable-or-not)](https://www.playframework.com/documentation/1.4.x/controllers#nobinding)](http://spring.io/blog/2012/03/28/secure-data-binding-with-grails/)](https://laravel.com/docs/5.2/eloquent#mass-assignment)](https://laravel.com/docs/5.2/eloquent#mass-assignment)](https://odetocode.com/Blogs/scott/archive/2012/03/11/complete-guide-to-mass-assignment-in-asp-net-mvc.aspx)](https://coffeeonthekeyboard.com/mass-assignment-security-part-10-855/)](https://guides.rubyonrails.org/v3.2.9/security.html#mass-assignment)](https://www.npmjs.com/package/mongoose-mass-assign)](http://underscorejs.org/#pick)](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/validation/DataBinder.html#setDisallowedFields-java.lang.String...-)](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/validation/DataBinder.html#setAllowedFields-java.lang.String...-) is a form for editing a user's account information:
<form>
     <input name="userid" type="text">
     <input name="password" type="text">
     <input name="email" text="text">
     <input type="submit">
</form>  

Here is the object that the form is binding to:
public class User {
   private String userid;
   private String password;
   private String email;
   private boolean isAdmin;

   //Getters & Setters
}

Here is the controller handling the request:
@RequestMapping(value = "/addUser", method = RequestMethod.POST)
public String submit(User user) {
   userService.add(user);
   return "successPage";
}

Here is the typical request:
POST /addUser
...
userid=bobbytables&password=hashedpass&email=bobby@tables.com

And here is the exploit in which we set the value of the attribute isAdmin of the instance of the class User:
POST /addUser
...
userid=bobbytables&password=hashedpass&email=bobby@tables.com&isAdmin=true

#### Exploitability¶
This functionality becomes exploitable when:

- Attacker can guess common sensitive fields.
- Attacker has access to source code and can review the models for sensitive fields.
- AND the object with sensitive fields has an empty constructor.

#### GitHub case study¶
In 2012, GitHub was hacked using mass assignment. A user was able to upload his public key to any organization and thus make any subsequent changes in their repositories. [GitHub's Blog Post](https://blog.github.com/2012-03-04-public-key-security-vulnerability-and-mitigation/).
#### Solutions¶

- Allow-list the bindable, non-sensitive fields.
- Block-list the non-bindable, sensitive fields.
Use [Data Transfer Objects](https://martinfowler.com/eaaCatalog/dataTransferObject.html) (DTOs).

### General Solutions¶
An architectural approach is to create Data Transfer Objects and avoid binding input directly to domain objects. Only the fields that are meant to be editable by the user are included in the DTO.
public class UserRegistrationFormDTO {
 private String userid;
 private String password;
 private String email;

 //NOTE: isAdmin field is not present

 //Getters & Setters
}

### Language & Framework specific solutions¶
#### Spring MVC¶
##### ##### ##### Allow-listing¶
@Controller
public class UserController
{
    @InitBinder
    public void initBinder(WebDataBinder binder, WebRequest request)
    {
        binder.setAllowedFields(["userid","password","email"]);
    }
...
}

Take a look here for the documentation.
##### ##### ##### Block-listing¶
@Controller
public class UserController
{
   @InitBinder
   public void initBinder(WebDataBinder binder, WebRequest request)
   {
      binder.setDisallowedFields(["isAdmin"]);
   }
...
}

Take a look here for the documentation.
#### NodeJS + Mongoose¶
Allow-listing¶
var UserSchema = new mongoose.Schema({
    userid: String,
    password: String,
    email : String,
    isAdmin : Boolean,
});

UserSchema.statics = {
    User.userCreateSafeFields: ['userid', 'password', 'email']
};

var User = mongoose.model('User', UserSchema);

_ = require('underscore');
var user = new User(_.pick(req.body, User.userCreateSafeFields));

Take a look here for the documentation.
Block-listing¶
var massAssign = require('mongoose-mass-assign');

var UserSchema = new mongoose.Schema({
    userid: String,
    password: String,
    email : String,
    isAdmin : { type: Boolean, protect: true, default: false }
});

UserSchema.plugin(massAssign);

var User = mongoose.model('User', UserSchema);

/** Static method, useful for creation **/
var user = User.massAssign(req.body);

/** Instance method, useful for updating**/
var user = new User;
user.massAssign(req.body);

/** Static massUpdate method **/
var input = { userid: 'bhelx', isAdmin: 'true' };
User.update({ '_id': someId }, { $set: User.massUpdate(input) }, console.log);

Take a look here for the documentation.
#### Ruby On Rails¶
Take a look here for the documentation.
#### Django¶
Take a look here for the documentation.
#### ASP NET¶
Take a look here for the documentation.
#### PHP Laravel + Eloquent¶
Allow-listing¶
<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    private $userid;
    private $password;
    private $email;
    private $isAdmin;

    protected $fillable = array('userid','password','email');
}

Take a look here for the documentation.
Block-listing¶
<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    private $userid;
    private $password;
    private $email;
    private $isAdmin;

    protected $guarded = array('isAdmin');
}

Take a look here for the documentation.
#### Grails¶
Take a look here for the documentation.
#### Play¶
Take a look here for the documentation.
#### Jackson (JSON Object Mapper)¶
Take a look here and here for the documentation.
#### GSON (JSON Object Mapper)¶
Take a look here and here for the document.
#### JSON-Lib (JSON Object Mapper)¶
Take a look here for the documentation.
#### Flexjson (JSON Object Mapper)¶
Take a look here for the documentation.
### References and future reading¶

[- Mass Assignment, Rails and You](https://code.tutsplus.com/tutorials/mass-assignment-rails-and-you--net-31695)