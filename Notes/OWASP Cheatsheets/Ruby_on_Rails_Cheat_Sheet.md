---
title: "Ruby on Rails Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Ruby_on_Rails_Cheat_Sheet.html"
created: "1741872882.105565"
tags: [owasp, cheatsheet, security]
---
# Ruby on Rails

## Ruby on [Rails](https://guides.rubyonrails.org/security.html#command-line-injection) Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[¶](#related-articles-and-references)](#tools)](#updating-rails-and-having-a-process-for-updating-dependencies)](#encryption)](#sensitive-files)](#attack-surface)](#business-logic-bugs)](#security-related-headers)](#cross-origin-resource-sharing)](#dynamic-render-paths)](#redirects-and-forwards)](#csrf-cross-site-request-forgery)](#insecure-direct-object-reference-or-forceful-browsing)](#token-authentication)](#authentication)](#sessions)](#cross-site-scripting-xss)](#sql-injection)](#command-injection)](#items)](#introduction)](#ruby-on-rails-cheat-sheet)
### Introduction¶
This Cheatsheet intends to provide quick basic Ruby on Rails security tips for developers. It complements, augments or emphasizes points brought up in the [Rails security guide](https://guides.rubyonrails.org/security.html) from rails core.
The Rails framework abstracts developers from quite a bit of tedious work and provides the means to accomplish complex tasks quickly and with ease. New developers, those unfamiliar with the inner-workings of Rails, likely need a basic set of guidelines to secure fundamental aspects of their application. The intended purpose of this doc is to be that guide.
### Items¶
#### Command Injection¶
Ruby offers a function called "eval" which will dynamically build new Ruby code based on Strings. It also has a number of ways to call system commands.
eval("ruby code [here](https://github.com/omniauth/omniauth#integrating-omniauth-into-your-application)")
system("os command here")
`ls -al /` # (backticks contain os command)
exec("os command here")
spawn("os command here")
open("| os command here")
Process.exec("os command here")
Process.spawn("os command here")
[[_content/dictionary#I|IO]].binread("| os command here")
IO.binwrite("| os command here", "foo")
IO.foreach("| os command here") {}
IO.popen("os command here")
IO.read("| os command here")
IO.readlines("| os command here")
IO.write("| os command here", "foo")

While the power of these commands is quite useful, extreme care should be taken when using them in a Rails based application. Usually, its just a bad idea. If need be, an allow-list of possible values should be used and any input should be validated as thoroughly as possible.
The guides from Rails and [[[_content/dictionary#O|OWASP]]](https://owasp.org/www-community/attacks/Command_Injection) contain further information on command injection.
#### [[[_content/dictionary#S|SQL]] Injection](https://owasp.org/www-community/attacks/SQL_Injection)¶
Ruby on Rails is often used with an [[_content/dictionary#O|ORM]] called [[_content/dictionary#A|ActiveRecord]], though it is flexible and can be used with other data sources. Typically very simple Rails applications use methods on the Rails models to query data. Many use cases protect for SQL Injection out of the box. However, it is possible to write code that allows for SQL Injection.
name = params[:name]
@projects = Project.where("name like '" + name + "'");

The statement is injectable because the name parameter is not escaped.
Here is the idiom for building this kind of statement:
@projects = Project.where("name like ?", "%#{[[_content/dictionary#A|ActiveRecord]]::Base.sanitize_sql_like(params[:name])}%")

Use caution not to build [[_content/dictionary#S|SQL]] statements based on user controlled input. A list of more realistic and detailed examples is here: [rails-sqli.org](https://rails-sqli.org). [[_content/dictionary#O|OWASP]] has extensive information about SQL Injection.
#### [Cross-site Scripting ([[_content/dictionary#X|XSS]])](https://owasp.org/www-community/attacks/xss/)¶
By default, protection against XSS comes as the default behavior. When string data is shown in views, it is escaped prior to being sent back to the browser. This goes a long way, but there are common cases where developers bypass this protection - for example to enable rich text editing. In the event that you want to pass variables to the front end with tags intact, it is tempting to do the following in your .erb file (ruby markup).
# Wrong! Do not do this!
<%= raw @product.name %>

# Wrong! Do not do this!
<%== @product.name %>

# Wrong! Do not do this!
<%= @product.name.html_safe %>

Unfortunately, any field that uses raw, html_safe or similar like this will be a potential [[_content/dictionary#X|XSS]] target. Note that there are also widespread misunderstandings about html_safe().
[This writeup](https://stackoverflow.com/questions/4251284/raw-vs-html-safe-vs-h-to-unescape-html) describes the underlying [[_content/dictionary#S|SafeBuffer]] mechanism in detail. Other tags that change the way strings are prepared for output can introduce similar issues.
The method html_safe of String is somewhat confusingly named. It means that we know for sure the content of the string is safe to include in [[_content/dictionary#H|HTML]] without escaping. This method itself is un-safe!
If you must accept HTML content from users, consider a markup language for rich text in an application (Examples include: Markdown and textile) and disallow HTML tags. This helps ensures that the input accepted doesn't include HTML content that could be malicious.
If you cannot restrict your users from entering HTML, consider implementing content security policy to disallow the execution of any [[_content/dictionary#J|JavaScript]]. And finally, consider using the #sanitize method that lets you list allowed tags. Be careful, this method has been shown to be flawed numerous times and will never be a complete solution.
An often overlooked XSS attack vector for older versions of rails is the href value of a link:
<%= link_to "Personal Website", @user.website %>

If @user.website contains a link that starts with javascript:, the content will execute when a user clicks the generated link:
<a href="javascript:alert('Haxored')">Personal Website</a>

Newer Rails versions escape such links in a better way.
link_to "Personal Website", 'javascript:alert(1);'.html_safe()
# Will generate:
# "<a href="javascript:alert(1);">Personal Website</a>"

Using [Content Security Policy](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/[[_content/dictionary#C|CSP]]) is one more security measure to forbid execution for links starting with javascript: .
[Brakeman scanner](https://github.com/presidentbeef/[brakeman](https://brakemanscanner.org/)) helps in finding [[_content/dictionary#X|XSS]] problems in Rails apps.
[[_content/dictionary#O|OWASP]] provides more general information about XSS in a top level page: Cross-site Scripting (XSS).
#### Sessions¶
By default, Ruby on Rails uses a Cookie based session store. What that means is that unless you change something, the session will not expire on the server. That means that some default applications may be vulnerable to replay attacks. It also means that sensitive information should never be put in the session.
The best practice is to use a database based session, which thankfully is very easy with Rails:
Project::Application.config.session_store :active_record_store

There is an [[Session_Management_Cheat_Sheet|Session Management Cheat Sheet]].
#### Authentication¶
As with all sensitive data, start securing your authentication with enabling [[_content/dictionary#T|TLS]] in your configuration:
# config/environments/production.rb
# Force all access to the app over [[_content/dictionary#S|SSL]], use Strict-Transport-Security,
# and use secure cookies
config.force_ssl = true

Uncomment the line 3 as above in your configuration.
Generally speaking, Rails does not provide authentication by itself. However, most developers using Rails leverage libraries such as Devise or [[_content/dictionary#A|AuthLogic]] to provide authentication.
To enable authentication it is possible to use Devise gem.
Install it using:
gem 'devise'

Then install it to the user model:
rails generate devise:install

Next, specify which resources (routes) require authenticated access in routes:
Rails.application.routes.draw do
  authenticate :user do
    resources :something do  # these resource require authentication
      ...
    end
  end

  devise_for :users # sign-up/-in/out routes

  root to: 'static#home' # no authentication required
end

To enforce password complexity, it is possible to use [zxcvbn gem](https://github.com/bitzesty/devise_zxcvbn). Configure your user model with it:
class User < [[_content/dictionary#A|ApplicationRecord]]
  devise :database_authenticatable,
    # other devise features, then
    :zxcvbnable
end

And configure the required password complexity:
# in config/initializers/devise.rb
Devise.setup do |config|
  # zxcvbn score for devise
  config.min_password_score = 4 # complexity score here.
  ...

You can try out [this PoC](https://github.com/qutorial/revise) to learn more about it.
Next, [omniauth gem](https://github.com/omniauth/omniauth) allows for multiple strategies for authentication. Using it one can configure secure authentication with Facebook, [[_content/dictionary#L|LDAP]] and many other providers. Read on here.
##### Token Authentication¶
Devise usually uses Cookies for authentication.
In the case token authentication is wished instead, it could be implemented with a gem [devise_token_auth](https://github.com/lynndylanhurley/devise_token_auth).
It supports multiple front end technologies, for example angular2-token.
This gem is configured similar to the devise gem itself. It also requires omniauth as a dependency.
# token-based authentication
gem 'devise_token_auth'
gem 'omniauth'

Then a route is defined:
mount_devise_token_auth_for 'User', at: 'auth'

And the User model is modified accordingly.
These actions can be done with one command:
rails g devise_token_auth:install [USER_CLASS] [MOUNT_PATH]

You may need to edit the generated migration to avoid unnecessary fields and/or field duplication depending on your use case.
Note: when you use only token authentication, there is no more need in [[CSRF](https://owasp.org/www-community/attacks/csrf)](https://owasp.org/www-community/attacks/csrf) protection in controllers. If you use both ways: cookies and tokens, the paths where cookies are used for authentication still must be protected from forgery!
There is an [[Authentication_Cheat_Sheet|Authentication Cheat Sheet]].
#### Insecure Direct Object Reference or Forceful Browsing¶
By default, Ruby on Rails apps use a RESTful [[_content/dictionary#U|URI]] structure. That means that paths are often intuitive and guessable. To protect against a user trying to access or modify data that belongs to another user, it is important to specifically control actions. Out of the gate on a vanilla Rails application, there is no such built-in protection. It is possible to do this by hand at the controller level.
It is also possible, and probably recommended, to consider resource-based access control libraries such as [cancancan](https://github.com/[[_content/dictionary#C|CanCanCommunity]]/cancancan) (cancan replacement) or [pundit](https://github.com/elabs/pundit) to do this. This ensures that all operations on a database object are authorized by the business logic of the application.
More general information about this class of vulnerability is in the [[[_content/dictionary#O|OWASP]] Top 10 Page](https://wiki.owasp.org/index.php/Top_10_2010-A4-Insecure_Direct_Object_References).
#### [[_content/dictionary#C|CSRF]] (Cross Site Request Forgery)¶
Ruby on Rails has specific, built-in support for CSRF tokens. To enable it, or ensure that it is enabled, find the base [[_content/dictionary#A|ApplicationController]] and look for a directive such as the following:
class ApplicationController < [[_content/dictionary#A|ActionController]]::Base
  protect_from_forgery

Note that the syntax for this type of control includes a way to add exceptions. Exceptions may be useful for APIs or other reasons - but should be reviewed and consciously included. In the example below, the Rails [[_content/dictionary#P|ProjectController]] will not provide [[_content/dictionary#C|CSRF]] protection for the show method.
class ProjectController < [[_content/dictionary#A|ApplicationController]]
  protect_from_forgery except: :show

Also note that by default Rails does not provide [[_content/dictionary#C|CSRF]] protection for any [[_content/dictionary#H|HTTP]] [[_content/dictionary#G|GET]] request.
Note: if you use token authentication only, there is no need to protect from CSRF in controllers like this. If cookie-based authentication is used on some paths, then the protections is still required on them.
There is a top level [[_content/dictionary#O|OWASP]] page for [Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf).
#### Redirects and Forwards¶
Web applications often require the ability to dynamically redirect users based on client-supplied data. To clarify, dynamic redirection usually entails the client including a [[_content/dictionary#U|URL]] in a parameter within a request to the application. Once received by the application, the user is redirected to the URL specified in the request.
For example:
http://www.example.com/redirect?url=http://www.example_commerce_site.com/checkout
The above request would redirect the user to http://www.example.com/checkout. The security concern associated with this functionality is leveraging an organization's trusted brand to phish users and trick them into visiting a malicious site, in our example, badhacker.com.
Example:
http://www.example.com/redirect?url=http://badhacker.com
The most basic, but restrictive protection is to use the :only_path option. Setting this to true will essentially strip out any host information. However, the :only_path option must be part of the first argument. If the first argument is not a hash table, then there is no way to pass in this option. In the absence of a custom helper or allowlist, this is one approach that can work:
begin
  if path = [[_content/dictionary#U|URI]].parse(params[:url]).path
    redirect_to path
  end
rescue URI::InvalidURIError
  redirect_to '/'
end

If matching user input against a list of approved sites or TLDs against regular expression is a must, it makes sense to leverage a library such as [[_content/dictionary#U|URI]].parse() to obtain the host and then take the host value and match it against regular expression patterns. Those regular expressions must, at a minimum, have anchors or there is a greater chance of an attacker bypassing the validation routine.
Example:
require 'uri'
host = URI.parse("#{params[:url]}").host
# this can be vulnerable to javascript://trusted.com/%0Aalert(0)
# so check .scheme and .port too
validation_routine(host) if host
def validation_routine(host)
  # Validation routine where we use  \A and \z as anchors *not* ^ and $
  # you could also check the host value against an allowlist
end

Also blind redirecting to user input parameter can lead to [[_content/dictionary#X|XSS]].
Example code:
redirect_to params[:to]

Will give this [[_content/dictionary#U|URL]]:
http://example.com/redirect?to[status]=200&to[protocol]=javascript:alert(0)//
The obvious fix for this type of vulnerability is to restrict to specific Top-Level Domains (TLDs), statically define specific sites, or map a key to it's value.
Example code:
ACCEPTABLE_URLS = {
  'our_app_1' => "https://www.example_commerce_site.com/checkout",
  'our_app_2' => "https://www.example_user_site.com/change_settings"
}

Will give this [[_content/dictionary#U|URL]]:
http://www.example.com/redirect?url=our_app_1
Redirection handling code:
def redirect
  url = ACCEPTABLE_URLS["#{params[:url]}"]
  redirect_to url if url
end

There is a more general [[_content/dictionary#O|OWASP]] resource about [[Unvalidated_Redirects_and_Forwards_Cheat_Sheet|unvalidated redirects and forwards]].
#### Dynamic Render Paths¶
In Rails, controller actions and views can dynamically determine which view or partial to render by calling the render method. If user input is used in or for the template name, an attacker could cause the application to render an arbitrary view, such as an administrative page.
Care should be taken when using user input to determine which view to render. If possible, avoid any user input in the name or path to the view.
#### Cross Origin Resource Sharing¶
Occasionally, a need arises to share resources with another domain. For example, a file-upload function that sends data via an [[_content/dictionary#A|AJAX]] request to another domain. In these cases, the same-origin rules followed by web browsers must be sent. Modern browsers, in compliance with HTML5 standards, will allow this to occur but in order to do this; a couple precautions must be taken.
When using a nonstandard [[_content/dictionary#H|HTTP]] construct, such as an atypical Content-Type header, for example, the following applies:
The receiving site should list only those domains allowed to make such requests as well as set the Access-Control-Allow-Origin header in both the response to the [[_content/dictionary#O|OPTIONS]] request and [[_content/dictionary#P|POST]] request. This is because the OPTIONS request is sent first, in order to determine if the remote or receiving site allows the requesting domain. Next, a second request, a POST request, is sent. Once again, the header must be set in order for the transaction to be shown as successful.
When standard HTTP constructs are used:
The request is sent and the browser, upon receiving a response, inspects the response headers in order to determine if the response can and should be processed.
Allowlist in Rails:
Gemfile:
gem 'rack-cors', :require => 'rack/cors'

config/application.rb:
module Sample
  class Application < Rails::Application
    config.middleware.use Rack::Cors do
      allow do
        origins 'someserver.example.com'
        resource %r{/users/\d+.json},
        :headers => ['Origin', 'Accept', 'Content-Type'],
        :methods => [:post, :get]
      end
    end
  end
end

#### Security-related headers¶
To set a header value, simply access the response.headers object as a hash inside your controller (often in a before/after_filter).
response.headers['X-header-name'] = 'value'

Rails provides the default_headers functionality that will automatically apply the values supplied. This works for most headers in almost all cases.
[[_content/dictionary#A|ActionDispatch]]::Response.default_headers = {
  'X-Frame-Options' => '[[_content/dictionary#S|SAMEORIGIN]]',
  'X-Content-Type-Options' => 'nosniff',
  'X-[[_content/dictionary#X|XSS]]-Protection' => '0'
}

[Strict transport security](https://owasp.org/www-project-secure-headers/#headers-link) is a special case, it is set in an environment file (e.g. production.rb)
config.force_ssl = true

For those not on the edge, there is a library ([secure_headers](https://github.com/twitter/secureheaders)) for the same behavior with content security policy abstraction provided. It will automatically apply logic based on the user agent to produce a concise set of headers.
#### Business Logic Bugs¶
Any application in any technology can contain business logic errors that result in security bugs. Business logic bugs are difficult to impossible to detect using automated tools. The best ways to prevent business logic security bugs are to do code review, pair program and write unit tests.
#### Attack Surface¶
Generally speaking, Rails avoids open redirect and path traversal types of vulnerabilities because of its /config/routes.rb file which dictates what URLs should be accessible and handled by which controllers. The routes file is a great place to look when thinking about the scope of the attack surface.
An example might be as follows:
# this is an example of what [[_content/dictionary#N|NOT]] to do
match ':controller(/:action(/:id(.:format)))'

In this case, this route allows any public method on any controller to be called as an action. As a developer, you want to make sure that users can only reach the controller methods intended and in the way intended.
#### Sensitive Files¶
Many Ruby on Rails apps are open source and hosted on publicly available source code repositories. Whether that is the case or the code is committed to a corporate source control system, there are certain files that should be either excluded or carefully managed.
/config/database.yml                 -  May contain production credentials.
/config/initializers/secret_token.rb -  Contains a secret used to hash session cookie.
/db/seeds.rb                         -  May contain seed data including bootstrap admin user.
/db/development.sqlite3              -  May contain real data.

#### Encryption¶
Rails uses [[_content/dictionary#O|OS]] encryption. Generally speaking, it is always a bad idea to write your own encryption.
Devise by default uses [[_content/dictionary#B|bcrypt]] for password hashing, which is an appropriate solution.
Typically, the following config causes the 10 stretches for production: /config/initializers/devise.rb
config.stretches = Rails.env.test? ? 1 : 10

### Updating Rails and Having a Process for Updating Dependencies¶
In early 2013, a number of critical vulnerabilities were identified in the Rails Framework. Organizations that had fallen behind current versions had more trouble updating and harder decisions along the way, including patching the source code for the framework itself.
An additional concern with Ruby applications in general is that most libraries (gems) are not signed by their authors. It is literally impossible to build a Rails based project with libraries that come from trusted sources. One good practice might be to audit the gems you are using.
In general, it is important to have a process for updating dependencies. An example process might define three mechanisms for triggering an update of response:

- Every month/quarter dependencies in general are updated.
- Every week important security vulnerabilities are taken into account and potentially trigger an update.
- In [[_content/dictionary#E|EXCEPTIONAL]] conditions, emergency updates may need to be applied.

### Tools¶
Use brakeman, an open source code analysis tool for Rails applications, to identify many potential issues. It will not necessarily produce comprehensive security findings, but it can find easily exposed issues. A great way to see potential issues in Rails is to review the brakeman documentation of warning types.
A newer alternative is [bearer](https://github.com/Bearer/bearer), an open source code security and privacy analysis tool for both Ruby and [[_content/dictionary#J|JavaScript]]/[[_content/dictionary#T|TypeScript]] code, in order to identify a broad range of [[_content/dictionary#O|OWASP]] Top 10 potential issues. It provides many configuration options and can easily integrate into your [[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]] pipeline.
There are emerging tools that can be used to track security issues in dependency sets, like automated scanning from [[[_content/dictionary#G|GitHub]]](https://github.blog/2017-11-16-introducing-security-alerts-on-github/) and [[[_content/dictionary#G|GitLab]]](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/).
Another area of tooling is the security testing tool [Gauntlt](http://gauntlt.org) which is built on cucumber and uses gherkin syntax to define attack files.
Launched in May 2013 and very similar to brakeman scanner, the [dawnscanner](https://github.com/thesp0nge/dawnscanner) rubygem is a static analyzer for security issues that work with Rails, Sinatra and Padrino web applications. Version 1.6.6 has more than 235 ruby specific [[_content/dictionary#C|CVE]] security checks.
### Related Articles and References¶

[- The Official Rails Security Guide](https://guides.rubyonrails.org/security.html)
[- [[_content/dictionary#O|OWASP]] Ruby on Rails Security Guide](https://owasp.org/www-pdf-archive/Rails_Security_2.pdf)
[- The Ruby Security Reviewers Guide](http://code.google.com/p/ruby-security/wiki/Guide)
[- The Ruby on Rails Security Mailing List](https://groups.google.com/forum/?fromgroups#!forum/rubyonrails-security)
[- Rails Insecure Defaults](https://codeclimate.com/blog/rails-insecure-defaults/)