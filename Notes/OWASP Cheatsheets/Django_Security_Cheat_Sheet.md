---
title: "Django Security Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Django_Security_Cheat_Sheet.html"
created: "1741872881.8366208"
tags: [owasp, cheatsheet, security]
---
# Django Security

## Django Security Cheat Sheet[[[[[[[[[[[[¶](#references)](#admin-panel-url)](#https)](#cross-site-scripting-xss)](#cross-site-request-forgery-csrf)](#cookies)](#headers)](#key-management)](#authentication)](#general-recommendations)](#introduction)](#django-security-cheat-sheet)
### Introduction¶
The Django framework is a powerful Python web framework, and it comes with built-in security features that can be used out-of-the-box to prevent common web vulnerabilities. This cheat sheet lists actions and security tips developers can take to develop secure Django applications. It aims to cover common vulnerabilities to increase the security posture of your Django application. Each item has a brief explanation and relevant code samples that are specific to the Django environment.
The Django framework provides some built-in security features that aim to be secure-by-default. These features are also flexible to empower a developer to re-use components for complex use-cases. This opens up scenarios where developers unfamiliar with the inner workings of the components can configure them in an insecure way. This cheat sheet aims to enumerate some such use cases.
### General Recommendations¶

- Always keep Django and your application's dependencies up-to-date to keep up with security vulnerabilities.
- Ensure that the application is never in [[_content/dictionary#D|DEBUG]] mode in a production environment. Never run DEBUG = True in production.
Use packages like [django_ratelimit](https://django-ratelimit.readthedocs.io/en/stable/) or [django-axes](https://django-axes.readthedocs.io/en/latest/index.html) to prevent brute-force attacks.

### Authentication¶

- Use django.contrib.auth app for views and forms for user authentication operations such as login, logout, password change, etc. Include the module and its dependencies django.contrib.contenttypes and django.contrib.sessions in the INSTALLED_APPS setting in the settings.py file.

INSTALLED_APPS = [
    # ...
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # ...
]

- Use the @login_required decorator to ensure that only authenticated users can access a view. The sample code below illustrates usage of @login_required.

from django.contrib.auth.decorators import login_required

# User is redirected to default login page if not authenticated.
@login_required
def my_view(request):
  # Your view logic

# User is redirected to custom '/login-page/' if not authenticated.
@login_required(login_url='/login-page/')
def my_view(request):
  # Your view logic

- Use password validators for enforcing password policies. Add or update the AUTH_PASSWORD_VALIDATORS setting in the settings.py file to include specific validators required by your application.

AUTH_PASSWORD_VALIDATORS = [
  {
    # Checks the similarity between the password and a set of attributes of the user.
    '[[_content/dictionary#N|NAME]]': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    '[[_content/dictionary#O|OPTIONS]]': {
      'user_attributes': ('username', 'email', 'first_name', 'last_name'),
      'max_similarity': 0.7,
    }
  },
  {
    # Checks whether the password meets a minimum length.
    'NAME': 'django.contrib.auth.password_validation.[[_content/dictionary#M|MinimumLengthValidator]]',
    'OPTIONS': {
      'min_length': 8,
    }
  },
  {
    # Checks whether the password occurs in a list of common passwords
    'NAME': 'django.contrib.auth.password_validation.[[_content/dictionary#C|CommonPasswordValidator]]',
  },
  {
    # Checks whether the password isn’t entirely numeric
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  }
]

- Store passwords using make-password utility function to hash a plain-text password.

from django.contrib.auth.hashers import make_password
#...
hashed_pwd = make_password('plaintext_password')

- Check a plaintext password against a hashed password by using the  check-password utility function.

from django.contrib.auth.hashers import check_password
#...
plain_pwd = 'plaintext_password'
hashed_pwd = 'hashed_password_from_database'

if check_password(plain_pwd, hashed_pwd):
  print("The password is correct.")
else:
  print("The password is incorrect.")

### Key Management¶
The SECRET_KEY parameter in settings.py is used for cryptographic signing and should be kept confidential. Consider the following recommendations:

- Generate a key at least 50 characters or more, containing a mix of letters, digits, and symbols.
- Ensure that the SECRET_KEY is generated using a strong random generator, such as get_random_secret_key() function in Django.
- Avoid hard coding the SECRET_KEY value in settings.py or any other location. Consider storing the key-value in environment variables or secrets managers.

import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

- Regularly rotate the key, keeping in mind that this action can invalidate sessions, password reset tokens, etc. Rotate the key immediately it if it ever gets exposed.

### Headers¶
Include the django.middleware.security.[[_content/dictionary#S|SecurityMiddleware]] module in the [[_content/dictionary#M|MIDDLEWARE]] setting in your project's settings.py to add security-related headers to your responses. This module is used to set the following parameters:

- SECURE_CONTENT_TYPE_NOSNIFF: Set this key to True. Protects against [[_content/dictionary#M|MIME]] type sniffing attacks by enabling the header X-Content-Type-Options: nosniff.
- SECURE_HSTS_SECONDS: Ensures the site is only accessible via [[_content/dictionary#H|HTTPS]].

Include the django.middleware.clickjacking.XFrameOptionsMiddleware module in the [[_content/dictionary#M|MIDDLEWARE]] setting in your project's settings.py (This module should be listed after the django.middleware.security.[[_content/dictionary#S|SecurityMiddleware]] module as ordering is important). This module is used to set the following parameters:

- X_FRAME_OPTIONS: Set this key to '[[_content/dictionary#D|DENY]]' or '[[_content/dictionary#S|SAMEORIGIN]]'. This setting adds the X-Frame-Options header to all [[_content/dictionary#H|HTTP]] responses. This protects against clickjacking attacks.

### Cookies¶

- SESSION_COOKIE_SECURE: Set this key to True in the settings.py file. This will send the session cookie over secure ([[_content/dictionary#H|HTTPS]]) connections only.
- CSRF_COOKIE_SECURE: Set this key to True in the settings.py file. This will ensure that the [[_content/dictionary#C|CSRF]] cookie is sent over secure connections only.
- Whenever you set a custom cookie in a view using the [[_content/dictionary#H|HttpResponse]].set_cookie() method, make sure to set its secure parameter to True.

response = [[_content/dictionary#H|HttpResponse]]("Some response")
response.set_cookie('my_cookie', 'cookie_value', secure=True)

### Cross Site Request Forgery ([[_content/dictionary#C|CSRF]])¶

- Include the django.middleware.csrf.[[_content/dictionary#C|CsrfViewMiddleware]] module in the [[_content/dictionary#M|MIDDLEWARE]] setting in your project's settings.py to add [[_content/dictionary#C|CSRF]] related headers to your responses.
- In forms use the {% csrf_token %} template tag to include the [[_content/dictionary#C|CSRF]] token. A sample is shown below.

<form method="post">
    {% csrf_token %}
    <!-- Your form fields here -->
</form>

- For [[_content/dictionary#A|AJAX]] calls, the [[_content/dictionary#C|CSRF]] token for the request has to be extracted prior to being used in the the AJAX call.  
Additional recommendations and controls can be found at Django's [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/3.2/ref/csrf/) documentation.

### Cross Site Scripting ([[_content/dictionary#X|XSS]])¶
The recommendations in this section are in addition to XSS recommendations already mentioned previously.

Use the built-in template system to render templates in Django. Refer to Django's [Automatic [[_content/dictionary#H|HTML]] escaping](https://docs.djangoproject.com/en/3.2/ref/templates/language/#automatic-html-escaping) documentation to learn more.
Avoid using safe, mark_safe, or [json_script](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#json-script0) filters for disabling Django's automatic template escaping. The equivalent function in Python is the make_safe() function. Refer to the json_script template filter documentation to learn more.
Refer to Django's [Cross Site Scripting ([[_content/dictionary#X|XSS]]) protection](https://docs.djangoproject.com/en/3.2/topics/security/#cross-site-scripting-xss-protection) documentation to learn more.

### [[_content/dictionary#H|HTTPS]]¶

- Include the django.middleware.security.[[_content/dictionary#S|SecurityMiddleware]] module in the [[_content/dictionary#M|MIDDLEWARE]] setting in your project's settings.py if not already added.
- Set the SECURE_SSL_REDIRECT = True in the settings.py file to ensure that all communication is over [[_content/dictionary#H|HTTPS]]. This will redirect any [[_content/dictionary#H|HTTP]] requests automatically to HTTPS. This is also a 301 (permanent) redirect, so your browser will remember the redirect for subsequent requests.
If your Django application is behind a proxy or load balancer, set the SECURE_PROXY_SSL_HEADER setting to [[_content/dictionary#T|TRUE]] so that Django can detect the original request's protocol. For further details refer to [SECURE_PROXY_SSL_HEADER documentation](https://docs.djangoproject.com/en/3.2/ref/settings/#secure-proxy-ssl-header).

### Admin panel [[_content/dictionary#U|URL]]¶
It is advisable to modify the default URL leading to the admin panel (example.com/admin/), in order to slightly increase the difficulty for automated attacks. Here’s how to do it:
In the default app folder within your project, locate the urls.py file managing the top-level URLs. Within the file, modify the urlpatterns variable, a list, so that the URL leading to admin.site.urls is different from "admin/". This approach adds an extra layer of security by obscuring the common endpoint used for administrative access.
### References¶
Additional documentation -

[- Clickjacking Protection](https://docs.djangoproject.com/en/3.2/topics/security/#clickjacking-protection)
[- Security Middleware](https://docs.djangoproject.com/en/3.2/topics/security/#module-django.middleware.security)