---
title: "PHP Configuration Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/PHP_Configuration_Cheat_Sheet.html"
created: "1741872882.0712938"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#P|PHP]] Configuration

## [[_content/dictionary#P|PHP]] Configuration Cheat Sheet[[[[[[[[[[[¶](#snuffleupagus)](#some-more-security-paranoid-checks)](#php-session-handling)](#php-executable-handling)](#php-file-upload-handling)](#php-general-settings)](#php-error-handling)](#phpini)](#php-configuration-and-deployment)](#introduction)](#php-configuration-cheat-sheet)
### Introduction¶
This page is meant to help those configuring PHP and the web server it is running on to be very secure.
Below you will find information on the proper settings for the php.ini file and instructions on configuring Apache, Nginx, and Caddy web servers.
For general PHP codebase security please refer to the two following great guides:

[- Paragonie's 2018 [[_content/dictionary#P|PHP]] Security Guide](https://paragonie.com/blog/2017/12/2018-guide-building-secure-php-software)
[- Awesome PHP Security](https://github.com/guardrailsio/awesome-php-security)

### [[_content/dictionary#P|PHP]] Configuration and Deployment¶
#### php.ini¶
Some of following settings need to be adapted to your system, in particular session.save_path, session.cookie_path (e.g. /var/www/mysite), and session.cookie_domain (e.g. [[_content/dictionary#E|ExampleSite]].com).
You should be running a [supported version of PHP](https://www.php.net/supported-versions.php) (as of this writing, 8.1 is the oldest version receiving security support from PHP, though distribution vendors often provide extended support). Review the [core php.ini directives](https://www.php.net/manual/ini.core.php) in the PHP Manual for a complete reference on every value in the php.ini configuration file.
You can find a copy of the following values in a [ready-to-go php.ini file here](https://github.com/danehrlich1/very-secure-php-ini).
##### [[_content/dictionary#P|PHP]] error handling¶
expose_php              = Off
error_reporting         = E_ALL
display_errors          = Off
display_startup_errors  = Off
log_errors              = On
error_log               = /valid_path/PHP-logs/php_error.log
ignore_repeated_errors  = Off

Keep in mind that you need to have display_errors to Off on a production server and it's a good idea to frequently notice the logs.
##### [[_content/dictionary#P|PHP]] general settings¶
doc_root                = /path/[[_content/dictionary#D|DocumentRoot]]/PHP-scripts/
open_basedir            = /path/DocumentRoot/PHP-scripts/
include_path            = /path/PHP-pear/
extension_dir           = /path/PHP-extensions/
mime_magic.magicfile    = /path/PHP-magic.mime
allow_url_fopen         = Off
allow_url_include       = Off
variables_order         = "[[_content/dictionary#G|GPCS]]"
allow_webdav_methods    = Off
session.gc_maxlifetime  = 600

allow_url_* prevents [[[_content/dictionary#L|LFI]]](https://www.acunetix.com/blog/articles/local-file-inclusion-lfi/)s to be easily escalated to [[[_content/dictionary#R|RFI]]](https://www.acunetix.com/blog/articles/remote-file-inclusion-rfi/)s.
##### [[_content/dictionary#P|PHP]] file upload handling¶
file_uploads            = On
upload_tmp_dir          = /path/PHP-uploads/
upload_max_filesize     = 2M
max_file_uploads        = 2

If your application is not using file uploads, and say the only data the user will enter / upload is forms that do not require any document attachments, file_uploads should be turned Off.
##### [[_content/dictionary#P|PHP]] executable handling¶
enable_dl               = Off
disable_functions       = system, exec, shell_exec, passthru, phpinfo, show_source, highlight_file, popen, proc_open, fopen_with_path, dbmopen, dbase_open, putenv, move_uploaded_file, chdir, mkdir, rmdir, chmod, rename, filepro, filepro_rowcount, filepro_retrieve, posix_mkfifo
disable_classes         =

These are dangerous PHP functions. You should disable all that you don't use.
##### [[_content/dictionary#P|PHP]] session handling¶
Session settings are some of the [[_content/dictionary#M|MOST]] important values to concentrate on in configuring. It is a good practice to change session.name to something new.
 session.save_path                = /path/PHP-session/
 session.name                     = myPHPSESSID
 session.auto_start               = Off
 session.use_trans_sid            = 0
 session.cookie_domain            = full.qualified.domain.name
 #session.cookie_path             = /application/path/
 session.use_strict_mode          = 1
 session.use_cookies              = 1
 session.use_only_cookies         = 1
 session.cookie_lifetime          = 14400 # 4 hours
 session.cookie_secure            = 1
 session.cookie_httponly          = 1
 session.cookie_samesite          = Strict
 session.cache_expire             = 30
 session.sid_length               = 256
 session.sid_bits_per_character   = 6

##### Some more security paranoid checks¶
session.referer_check   = /application/path
memory_limit            = 50M
post_max_size           = 20M
max_execution_time      = 60
report_memleaks         = On
html_errors             = Off
zend.exception_ignore_args = On

#### [Snuffleupagus](https://snuffleupagus.readthedocs.io)¶
Snuffleupagus is the spiritual
descendent of Suhosin for [[_content/dictionary#P|PHP]] 7 and onwards, with [modern
features](https://snuffleupagus.readthedocs.io/features.html). It's considered
stable, and is usable in production.