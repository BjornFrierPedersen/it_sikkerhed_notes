# Windows Access Controls

## Source:
- [A video about Windows Access Controls](https://www.youtube.com/watch?v=NXFelU9lZGM)

## Overview
Windows Access Controls are mechanisms that manage how users and processes interact with resources in the Windows operating system. They form the foundation of Windows security by controlling who can access what and what actions they can perform.

## Core Components

### Access Control Models
- **[[_content/dictionary#D|DAC]]** (Discretionary Access Control)
  - The owner of a resource determines who can access it and what permissions they have
  - Primary model used in Windows systems
  - Implemented through Access Control Lists ([[_content/dictionary#A|ACL]]s)

- **[[_content/dictionary#M|MAC]]** (Mandatory Access Control)
  - System enforces access based on security labels
  - Less prominent in standard Windows, but elements appear in Windows features like [[_content/dictionary#A|AppLocker]]

- **[[_content/dictionary#R|RBAC]]** (Role-Based Access Control)
  - Access determined by user's assigned role in the organization
  - Implemented through Active Directory groups and roles

### Key Concepts

- **Security Principals**
  - Entities that can be authenticated (users, groups, services, computers)
  - Identified by unique Security Identifiers ([[_content/dictionary#S|SID]]s)
  - Cannot be reused or transferred between entities

- **Security Descriptors**
  - Data structures containing security information for securable objects
  - Components include:
    - Owner [[_content/dictionary#S|SID]]
    - Primary Group SID
    - Discretionary Access Control List ([[_content/dictionary#D|DACL]])
    - System Access Control List ([[_content/dictionary#S|SACL]])

- **Access Control Lists (ACLs)**
  - **[[_content/dictionary#D|DACL]]** (Discretionary Access Control List)
    - Defines which security principals are granted or denied access
    - Contains Access Control Entries (ACEs) in priority order
    - If no DACL is present, full access is granted to everyone
    - If DACL is empty, all access is denied

  - **[[_content/dictionary#S|SACL]]** (System Access Control List)
    - Controls auditing of access attempts
    - Specifies which access attempts should be logged
    - Important for security monitoring and compliance

- **Access Control Entries ([[_content/dictionary#A|ACE]]s)**
  - Building blocks of [[_content/dictionary#A|ACL]]s
  - Each entry contains:
    - [[_content/dictionary#S|SID]] of a security principal
    - Access mask (specific permissions)
    - Flags (inheritance settings)
    - Type (Allow, Deny, Audit)

## [[_content/dictionary#N|NTFS]] Permissions

### Standard Permissions
- **Full Control**: Complete control over files and folders
- **Modify**: Read, write, and delete files
- **Read & Execute**: View contents and execute programs
- **List Folder Contents**: View folder contents (folders only)
- **Read**: View file/folder attributes and contents
- **Write**: Create new files and write to existing ones

### Advanced Permissions
- More granular control with 14 specific permissions
- Examples:
  - **Traverse Folder/Execute File**
  - **List Folder/Read Data**
  - **Create Files/Write Data**
  - **Create Folders/Append Data**
  - **Delete Subfolders and Files**
  - **Delete**
  - **Read Attributes**
  - **Write Attributes**
  - **Read Extended Attributes**
  - **Write Extended Attributes**
  - **Read Permissions**
  - **Change Permissions**
  - **Take Ownership**

### Permission Inheritance
- Permissions can be inherited from parent objects
- Can be configured to:
  - Apply to this folder, subfolders, and files
  - Apply to this folder only
  - Apply to this folder and subfolders
  - Apply to this folder and files
  - Apply to subfolders only
  - Apply to files only

### Permission Conflicts
- **Explicit** permissions override **inherited** permissions
- **Deny** permissions override **Allow** permissions
- Permissions are cumulative across all groups a user belongs to

## User Account Control ([[_content/dictionary#U|UAC]])

- Introduced in Windows Vista
- Reduces the attack surface by:
  - Running most applications with standard user privileges
  - Prompting for consent/credentials for administrative actions
  - Isolating user and administrator access tokens
  - Using virtualization to redirect system writes to user-specific locations

## Registry Access Controls
- Similar [[_content/dictionary#A|ACL]]-based system as files
- Controls who can read, write, create, or delete registry keys
- Critical for system security and application settings protection

## Using Access Controls Effectively

### Best Practices
- **Principle of Least Privilege**: Grant only necessary permissions
- **Role-Based Access**: Assign permissions to groups rather than individual users
- **Regular Auditing**: Review permissions and access logs periodically
- **Inheritance Planning**: Design folder hierarchies with permission inheritance in mind
- **Administrative Separation**: Use dedicated administrative accounts

### Common Tools for Management
- **File Explorer Properties → Security tab**
- **icacls.exe** command-line tool
- **Windows [[_content/dictionary#P|PowerShell]]** cmdlets (Get-Acl, Set-Acl)
- **Active Directory Users and Computers**
- **Local Security Policy** (secpol.msc)
- **Group Policy Management Console** ([[_content/dictionary#G|GPMC]])

## Advanced Security Features

### [[_content/dictionary#A|AppLocker]] and Windows Defender Application Control ([[_content/dictionary#W|WDAC]])
- Control which applications can run on systems
- Create rules based on attributes like publisher, path, or file hash

### Windows Defender Credential Guard
- Isolates credential information using virtualization-based security
- Protects against Pass-the-Hash and other credential theft attacks

### Just Enough Administration ([[_content/dictionary#J|JEA]])
- Role-based administration through [[_content/dictionary#P|PowerShell]]
- Limits administrative access to only what's needed for specific tasks
