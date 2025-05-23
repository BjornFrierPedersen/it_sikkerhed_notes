---
title: "OS Command Injection Defense Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html"
created: "1741872882.0590117"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#O|OS]] Command Injection Defense

## [[_content/dictionary#O|OS]] [Command Injection](https://owasp.org/www-community/attacks/Command_Injection) Defense Cheat Sheet[[[[[[[[[[[[[[[[[[[[¶](#external-references)](#how-to-test)](#how-to-review-code)](#how-to-avoid-vulnerabilities)](#description-of-command-injection-vulnerability)](#related-articles)](#php)](#net)](#java)](#code-examples)](#additional-defenses)](#layer-2)](#layer-1)](#defense-option-3-parameterization-in-conjunction-with-input-validation)](#defense-option-2-escape-values-added-to-os-commands-specific-to-each-os)](#defense-option-1-avoid-calling-os-commands-directly)](#primary-defenses)](#argument-injection)](#introduction)](#os-command-injection-defense-cheat-sheet)
### Introduction¶
Command injection (or OS Command Injection) is a type of injection where software that constructs a system command using externally influenced input does not correctly neutralize the input from special elements that can modify the initially intended command.
For example, if the supplied value is:
calc

when typed in a Windows command prompt, the application Calculator is displayed.
However, if the supplied value has been tampered with, and now it is:
calc & echo "test"

when executed, it changes the meaning of the initial intended value.
Now, both the Calculator application and the value test are displayed:

The problem is exacerbated if the compromised process does not follow the principle of least privileges and attacker-controlled commands end up running with special system privileges that increase the amount of damage.
#### Argument Injection¶
Every [[_content/dictionary#O|OS]] Command Injection is also an Argument Injection. In this type of attacks, user input can be passed as arguments while executing a specific command.
For example, if the user input is passed through an escape function to escape certain characters like &, |, ;, etc.
system("curl " . escape($url));

which will prevent an attacker to run other commands.
However, if the attacker controlled string contains an additional argument of the curl command:
system("curl " . escape("--help"))

Now when the above code is executed, it will show the output of curl --help.
Depending upon the system command used, the impact of an Argument injection attack can range from Information Disclosure to critical Remote Code Execution.
### Primary Defenses¶
#### Defense Option 1: Avoid calling [[_content/dictionary#O|OS]] commands directly¶
The primary defense is to avoid calling OS commands directly. Built-in library functions are a very good alternative to OS Commands, as they cannot be manipulated to perform tasks other than those it is intended to do.
For example use mkdir() instead of system("mkdir /dir_name").
If there are available libraries or APIs for the language you use, this is the preferred method.
#### Defense option 2: Escape values added to [[_content/dictionary#O|OS]] commands specific to each OS¶
[[_content/dictionary#T|TODO]]: To enhance.
For examples, see [[escapeshellarg()](https://www.php.net/manual/en/function.escapeshellarg.php)](https://www.php.net/manual/en/function.escapeshellarg.php) in [[_content/dictionary#P|PHP]].
The escapeshellarg() surrounds the user input in single quotes, so if the malformed user input is something like & echo "hello", the final output will be like calc '& echo "hello"' which will be parsed as a single argument to the command calc.
Even though escapeshellarg() prevents OS Command Injection, an attacker can still pass a single argument to the command.
#### Defense option 3: Parameterization in conjunction with Input Validation¶
If calling a system command that incorporates user-supplied cannot be avoided, the following two layers of defense should be used within software to prevent attacks:
##### Layer 1¶
Parameterization: If available, use structured mechanisms that automatically enforce the separation between data and command. These mechanisms can help provide the relevant quoting and encoding.
##### Layer 2¶
Input validation: The values for commands and the relevant arguments should be both validated. There are different degrees of validation for the actual command and its arguments:

- When it comes to the commands used, these must be validated against a list of allowed commands.
- In regards to the arguments used for these commands, they should be validated using the following options:
- - Positive or allowlist input validation: Where are the arguments allowed explicitly defined.
- - Allowlist Regular Expression: Where a list of good, allowed characters and the maximum length of the string are defined. Ensure that metacharacters like ones specified in Note A and whitespaces are not part of the Regular Expression. For example, the following regular expression only allows lowercase letters and numbers and does not contain metacharacters. The length is also being limited to 3-10 characters: ^[a-z0-9]{3,10}$

According to Guideline 10 of this [[[_content/dictionary#P|POSIX]]](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html), The first -- argument that is not an option-argument should be accepted as a delimiter indicating the end of options. Any following arguments should be treated as operands, even if they begin with the '-' character. For example, curl -- $url will prevent an argument injection even if the $url is malformed and contains an additional argument.

Note A:
& |  ; $ > < ` \ ! ' " ( )

### Additional Defenses¶
On top of primary defenses, parameterizations, and input validation, we also recommend adopting all of these additional defenses to provide defense in depth.
These additional defenses are:

- Applications should run using the lowest privileges that are required to accomplish the necessary tasks.
- If possible, create isolated accounts with limited privileges that are only used for a single task.

### Code examples¶
#### Java¶
In Java, use [[[_content/dictionary#P|ProcessBuilder]]](https://docs.oracle.com/javase/8/docs/api/java/lang/ProcessBuilder.html) and the command must be separated from its arguments.
Note about the Java's Runtime.exec method behavior:
There are many sites that will tell you that Java's Runtime.exec is exactly the same as C's system function. This is not true. Both allow you to invoke a new program/process.
However, C's system function passes its arguments to the shell (/bin/sh) to be parsed, whereas Runtime.exec tries to split the string into an array of words, then executes the first word in the array with the rest of the words as parameters.
Runtime.exec does [[_content/dictionary#N|NOT]] try to invoke the shell at any point and does not support shell metacharacters.
The key difference is that much of the functionality provided by the shell that could be used for mischief (chaining commands using  &, &&, |, ||, etc,  redirecting input and output) would simply end up as a parameter being passed to the first command, likely causing a syntax error or being thrown out as an invalid parameter.
Code to test the note above:
String[] specialChars = new String[]{"&", "&&", "|", "||"};
String payload = "cmd /c whoami";
String cmdTemplate = "java -version %s " + payload;
String cmd;
Process p;
int returnCode;
for (String specialChar : specialChars) {
    cmd = String.format(cmdTemplate, specialChar);
    System.out.printf("#### [[_content/dictionary#T|TEST]] [[_content/dictionary#C|CMD]]: %s\n", cmd);
    p = Runtime.getRuntime().exec(cmd);
    returnCode = p.waitFor();
    System.out.printf("[[_content/dictionary#R|RC]]    : %s\n", returnCode);
    System.out.printf("[[_content/dictionary#O|OUT]]   :\n%s\n", IOUtils.toString(p.getInputStream(),
                      "utf-8"));
    System.out.printf("[[_content/dictionary#E|ERROR]] :\n%s\n", IOUtils.toString(p.getErrorStream(),
                      "utf-8"));
}
System.out.printf("#### TEST [[_content/dictionary#P|PAYLOAD]] [[_content/dictionary#O|ONLY]]: %s\n", payload);
p = Runtime.getRuntime().exec(payload);
returnCode = p.waitFor();
System.out.printf("RC    : %s\n", returnCode);
System.out.printf("OUT   :\n%s\n", IOUtils.toString(p.getInputStream(),
                  "utf-8"));
System.out.printf("ERROR :\n%s\n", IOUtils.toString(p.getErrorStream(),
                  "utf-8"));

Result of the test:
##### [[_content/dictionary#T|TEST]] [[_content/dictionary#C|CMD]]: java -version & cmd /c whoami
[[_content/dictionary#R|RC]]    : 0
[[_content/dictionary#O|OUT]]   :

[[_content/dictionary#E|ERROR]] :
java version "1.8.0_31"

##### [[_content/dictionary#T|TEST]] [[_content/dictionary#C|CMD]]: java -version && cmd /c whoami
[[_content/dictionary#R|RC]]    : 0
[[_content/dictionary#O|OUT]]   :

[[_content/dictionary#E|ERROR]] :
java version "1.8.0_31"

##### [[_content/dictionary#T|TEST]] [[_content/dictionary#C|CMD]]: java -version | cmd /c whoami
[[_content/dictionary#R|RC]]    : 0
[[_content/dictionary#O|OUT]]   :

[[_content/dictionary#E|ERROR]] :
java version "1.8.0_31"

##### [[_content/dictionary#T|TEST]] [[_content/dictionary#C|CMD]]: java -version || cmd /c whoami
[[_content/dictionary#R|RC]]    : 0
[[_content/dictionary#O|OUT]]   :

[[_content/dictionary#E|ERROR]] :
java version "1.8.0_31"

##### [[_content/dictionary#T|TEST]] [[_content/dictionary#P|PAYLOAD]] [[_content/dictionary#O|ONLY]]: cmd /c whoami
[[_content/dictionary#R|RC]]    : 0
[[_content/dictionary#O|OUT]]   :
mydomain\simpleuser

[[_content/dictionary#E|ERROR]] :

Incorrect usage:
[[_content/dictionary#P|ProcessBuilder]] b = new ProcessBuilder("C:\[[_content/dictionary#D|DoStuff]].exe -arg1 -arg2");

In this example, the command together with the arguments are passed as a one string, making it easy to manipulate that expression and inject malicious strings.
Correct Usage:
Here is an example that starts a process with a modified working directory. The command and each of the arguments are passed separately. This makes it easy to validate each term and reduces the risk of malicious strings being inserted.
[[_content/dictionary#P|ProcessBuilder]] pb = new ProcessBuilder("[[_content/dictionary#T|TrustedCmd]]", "TrustedArg1", "TrustedArg2");

Map<String, String> env = pb.environment();

pb.directory(new File("[[_content/dictionary#T|TrustedDir]]"));

Process p = pb.start();

#### .Net¶
See relevant details in the [[[_content/dictionary#D|DotNet]] Security Cheat Sheet](DotNet_Security_Cheat_Sheet.html#os-injection)
#### [[_content/dictionary#P|PHP]]¶
In PHP use escapeshellarg() or [escapeshellcmd()](https://www.php.net/manual/en/function.escapeshellcmd.php) rather than [exec()](https://www.php.net/manual/en/function.exec.php), [system()](https://www.php.net/manual/en/function.system.php), [passthru()](https://www.php.net/manual/en/function.passthru.php).
### Related articles¶
#### Description of Command Injection Vulnerability¶

- [[_content/dictionary#O|OWASP]] Command Injection.

#### How to Avoid Vulnerabilities¶

C Coding: [Do not call system()](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152177).

#### How to Review Code¶

[[_content/dictionary#O|OWASP]] [Reviewing Code for [[_content/dictionary#O|OS]] Injection](https://wiki.owasp.org/index.php/Reviewing_Code_for_OS_Injection).

#### How to Test¶

[[[_content/dictionary#O|OWASP]] Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) article on [Testing for Command Injection](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection.html).

#### External References¶

[[[_content/dictionary#C|CWE]] Entry 77 on Command Injection](https://cwe.mitre.org/data/definitions/77.html).