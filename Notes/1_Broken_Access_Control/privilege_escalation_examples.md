# Privilege Escalation Types and Examples

Broken Authorization often leads to privilege escalation, which allows attackers to gain unauthorized access to systems or data. There are two main types of privilege escalation:

## Horizontal Privilege Escalation

Horizontal Privilege Escalation occurs when a user successfully accesses or updates resources belonging to another user with similar privileges.

### Example

User A updates their own password with this [[_content/dictionary#U|URL]]:
```
http://vulnerableapp.com/user/account?accountId=7800001
```

Then User A can also update User B's password by simply changing the accountId parameter:
```
http://vulnerableapp.com/user/account?accountId=7800002
```

This vulnerability happens because the system fails to check the ownership of the account after successful authentication. The system only verifies that the user is authenticated but does not validate whether they should have access to the specific resource identified by the accountId parameter.

## Vertical Privilege Escalation

Vertical Privilege Escalation occurs when a user gains more privileges than they should have, essentially elevating their access level.

### Example

User A accesses their own account here:
```
http://vulnerableapp.com/user/account
```

But then tries to access the admin panel by directly navigating to:
```
http://vulnerableapp.com/admin/panel
```

If the user successfully gains access to the admin panel, this represents a vertical privilege escalation, as they've elevated their privileges from a regular user to an administrator.

## Vulnerable Code Examples in .[[_content/dictionary#N|NET]]

### Vulnerable Example #1: Missing Authorization

The following [[_content/dictionary#A|ASP]].[[_content/dictionary#N|NET]] Core snippet shows a MVC controller that does not protect an administrative action:

```csharp
public class AccountController : Controller {
    public ActionResult AdminFunctionality() {
    }
}
```

Simple authentication and authorization controls can be enforced by adding the `[Authorize]` attribute either on the controller or on the specific action.

### Vulnerable Example #2: Incorrect Attribute Mix

The following [[_content/dictionary#A|ASP]].[[_content/dictionary#N|NET]] Core snippet shows an incorrect mix of `[AllowAnonymous]` and `[Authorize]` attributes, resulting in a non-protected action:

```csharp
[AllowAnonymous]
public class AccountController : Controller {
    [Authorize]
    public ActionResult AdminFunctionality() {
    }

    public ActionResult PublicFunctionality() { 
    }
}
```

The `[AllowAnonymous]` attribute at the controller level bypasses all authorization statements, hence the `[Authorize]` attribute on the AdminFunctionality action is ignored and does not protect the administrative functionality.

## Prevention Recommendations

1. **Validate Resource Ownership**: Always verify that the authenticated user has rights to the specific resource they're trying to access.
2. **Proper Authorization Attributes**: Apply authorization attributes correctly, understanding their hierarchy and precedence.
3. **Role-Based Access Control**: Implement proper [[_content/dictionary#R|RBAC]] checks for different functionality based on user roles.
4. **Avoid Direct Object References**: Use indirect references or verify authorization on direct references.
5. **Implement Access Control at Every Layer**: Don't rely solely on hiding functionality in the [[_content/dictionary#U|UI]]; enforce access controls on the server-side. 