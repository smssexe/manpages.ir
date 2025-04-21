USERADD(8)							  System Management Commands							    USERADD(8)

NAME
       useradd - create a new user or update default new user information

SYNOPSIS

       useradd [options] LOGIN

       useradd -D

       useradd -D [options]

DESCRIPTION
       useradd is a low level utility for adding users. On Debian, administrators should usually use adduser(8) instead.

       When invoked without the -D option, the useradd command creates a new user account using the values specified on the command line plus the default
       values from the system. Depending on command line options, the useradd command will update system files and may also create the new user's home
       directory and copy initial files.

       By default, a group will also be created for the new user (see -g, -N, -U, and USERGROUPS_ENAB).

OPTIONS
       The options which apply to the useradd command are:

       --badname
	   Allow names that do not conform to standards.

       -b, --base-dir BASE_DIR
	   The default base directory for the system if -d HOME_DIR is not specified.  BASE_DIR is concatenated with the account name to define the home
	   directory.

	   If this option is not specified, useradd will use the base directory specified by the HOME variable in /etc/default/useradd, or /home by default.

       -c, --comment COMMENT
	   Any text string. It is generally a short description of the account, and is currently used as the field for the user's full name.

       -d, --home-dir HOME_DIR
	   The new user will be created using HOME_DIR as the value for the user's login directory. The default is to append the LOGIN name to BASE_DIR and
	   use that as the login directory name. If the directory HOME_DIR does not exist, then it will be created unless the -M option is specified.

       -D, --defaults
	   See below, the subsection "Changing the default values".

       -e, --expiredate EXPIRE_DATE
	   The date on which the user account will be disabled. The date is specified in the format YYYY-MM-DD.

	   If not specified, useradd will use the default expiry date specified by the EXPIRE variable in /etc/default/useradd, or an empty string (no expiry)
	   by default.

       -f, --inactive INACTIVE
	   defines the number of days after the password exceeded its maximum age where the user is expected to replace this password. The value is stored in
	   the shadow password file. An input of 0 will disable an expired password with no delay. An input of -1 will blank the respective field in the
	   shadow password file. See shadow(5)for more information.

	   If not specified, useradd will use the default inactivity period specified by the INACTIVE variable in /etc/default/useradd, or -1 by default.

       -F, --add-subids-for-system
	   Update /etc/subuid and /etc/subgid even when creating a system account with -r option.

       -g, --gid GROUP
	   The name or the number of the user's primary group. The group name must exist. A group number must refer to an already existing group.

	   If not specified, the behavior of useradd will depend on the USERGROUPS_ENAB variable in /etc/login.defs. If this variable is set to yes (or
	   -U/--user-group is specified on the command line), a group will be created for the user, with the same name as her loginname. If the variable is
	   set to no (or -N/--no-user-group is specified on the command line), useradd will set the primary group of the new user to the value specified by
	   the GROUP variable in /etc/default/useradd, or 100 by default.

       -G, --groups GROUP1[,GROUP2,...[,GROUPN]]]
	   A list of supplementary groups which the user is also a member of. Each group is separated from the next by a comma, with no intervening
	   whitespace. The groups are subject to the same restrictions as the group given with the -g option. The default is for the user to belong only to
	   the initial group.

       -h, --help
	   Display help message and exit.

       -k, --skel SKEL_DIR
	   The skeleton directory, which contains files and directories to be copied in the user's home directory, when the home directory is created by
	   useradd.

	   This option is only valid if the -m (or --create-home) option is specified.

	   If this option is not set, the skeleton directory is defined by the SKEL variable in /etc/default/useradd or, by default, /etc/skel.

	   If possible, the ACLs and extended attributes are copied.

       -K, --key KEY=VALUE
	   Overrides /etc/login.defs defaults (UID_MIN, UID_MAX, UMASK, PASS_MAX_DAYS and others).

	   Example: -K PASS_MAX_DAYS =-1 can be used when creating an account to turn off password aging. Multiple -K options can be specified, e.g.:
	   -K UID_MIN =100 -K  UID_MAX=499

	   For the compatibility with previous Debian's useradd, the -O option is also supported.

       -l, --no-log-init
	   Do not add the user to the lastlog and faillog databases.

	   By default, the user's entries in the lastlog and faillog databases are reset to avoid reusing the entry from a previously deleted user.

	   If this option is not specified, useradd will also consult the variable LOG_INIT in the /etc/default/useradd if set to no the user will not be
	   added to the lastlog and faillog databases.

       -m, --create-home
	   Create the user's home directory if it does not exist. The files and directories contained in the skeleton directory (which can be defined with the
	   -k option) will be copied to the home directory.

	   By default, if this option is not specified and CREATE_HOME is not enabled, no home directories are created.

	   The directory where the user's home directory is created must exist and have proper SELinux context and permissions. Otherwise the user's home
	   directory cannot be created or accessed.

       -M, --no-create-home
	   Do not create the user's home directory, even if the system wide setting from /etc/login.defs (CREATE_HOME) is set to yes.

       -N, --no-user-group
	   Do not create a group with the same name as the user, but add the user to the group specified by the -g option or by the GROUP variable in
	   /etc/default/useradd.

	   The default behavior (if the -g, -N, and -U options are not specified) is defined by the USERGROUPS_ENAB variable in /etc/login.defs.

       -o, --non-unique
	   allows the creation of an account with an already existing UID.

	   This option is only valid in combination with the -u option. As a user identity serves as key to map between users on one hand and permissions,
	   file ownerships and other aspects that determine the system's behavior on the other hand, more than one login name will access the account of the
	   given UID.

       -p, --password PASSWORD
	   defines an initial password for the account. PASSWORD is expected to be encrypted, as returned by crypt (3). Within a shell script, this option
	   allows to create efficiently batches of users.

	   Without this option, the new account will be locked and with no password defined, i.e. a single exclamation mark in the respective field of
	   /etc/shadow. This is a state where the user won't be able to access the account or to define a password himself.

	   Note:Avoid this option on the command line because the password (or encrypted password) will be visible by users listing the processes.

	   You should make sure the password respects the system's password policy.

       -r, --system
	   Create a system account.

	   System users will be created with no aging information in /etc/shadow, and their numeric identifiers are chosen in the SYS_UID_MIN-SYS_UID_MAX
	   range, defined in /etc/login.defs, instead of UID_MIN-UID_MAX (and their GID counterparts for the creation of groups).

	   Note that useradd will not create a home directory for such a user, regardless of the default setting in /etc/login.defs (CREATE_HOME). You have to
	   specify the -m options if you want a home directory for a system account to be created.

	   Note that this option will not update /etc/subuid and /etc/subgid. You have to specify the -F options if you want to update the files for a system
	   account to be created.

       -R, --root CHROOT_DIR
	   Apply changes in the CHROOT_DIR directory and use the configuration files from the CHROOT_DIR directory. Only absolute paths are supported.

       -P, --prefix PREFIX_DIR
	   Apply changes to configuration files under the root filesystem found under the directory PREFIX_DIR. This option does not chroot and is intended
	   for preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM authentication is using the host files.
	   No SELINUX support.

       -s, --shell SHELL
	   sets the path to the user's login shell. Without this option, the system will use the SHELL variable specified in /etc/default/useradd, or, if that
	   is as well not set, the field for the login shell in /etc/passwd remains empty.

       -u, --uid UID
	   The numerical value of the user's ID. This value must be unique, unless the -o option is used. The value must be non-negative. The default is to
	   use the smallest ID value greater than or equal to UID_MIN and greater than every other user.

	   See also the -r option and the UID_MAX description.

       -U, --user-group
	   Create a group with the same name as the user, and add the user to this group.

	   The default behavior (if the -g, -N, and -U options are not specified) is defined by the USERGROUPS_ENAB variable in /etc/login.defs.

       -Z, --selinux-user SEUSER
	   defines the SELinux user for the new account. Without this option, a SELinux uses the default user. Note that the shadow system doesn't store the
	   selinux-user, it uses semanage(8) for that.

   Changing the default values
       When invoked with only the -D option, useradd will display the current default values. When invoked with -D plus other options, useradd will update the
       default values for the specified options. Valid default-changing options are:

       -b, --base-dir BASE_DIR
	   sets the path prefix for a new user's home directory. The user's name will be affixed to the end of BASE_DIR to form the new user's home directory
	   name, if the -d option is not used when creating a new account.

	   This option sets the HOME variable in /etc/default/useradd.

       -e, --expiredate EXPIRE_DATE
	   sets the date on which newly created user accounts are disabled.

	   This option sets the EXPIRE variable in /etc/default/useradd.

       -f, --inactive INACTIVE
	   defines the number of days after the password exceeded its maximum age where the user is expected to replace this password. See shadow(5)for more
	   information.

	   This option sets the INACTIVE variable in /etc/default/useradd.

       -g, --gid GROUP
	   sets the default primary group for newly created users, accepting group names or a numerical group ID. The named group must exist, and the GID must
	   have an existing entry.

	   This option sets the GROUP variable in /etc/default/useradd.

       -s, --shell SHELL
	   defines the default login shell for new users.

	   This option sets the SHELL variable in /etc/default/useradd.

NOTES
       The system administrator is responsible for placing the default user files in the /etc/skel/ directory (or any other skeleton directory specified in
       /etc/default/useradd or on the command line).

CAVEATS
       You may not add a user to a NIS or LDAP group. This must be performed on the corresponding server.

       Similarly, if the username already exists in an external user database such as NIS or LDAP, useradd will deny the user account creation request.

       Usernames may contain only lower and upper case letters, digits, underscores, or dashes. They can end with a dollar sign. Dashes are not allowed at the
       beginning of the username. Fully numeric usernames and usernames . or .. are also disallowed. It is not recommended to use usernames beginning with .
       character as their home directories will be hidden in the ls output.

       On Debian, the only constraints are that usernames must neither start with a dash ('-') nor plus ('+') nor tilde ('~') nor contain a colon (':'), a
       comma (','), or a whitespace (space: ' ', end of line: '\n', tabulation: '\t', etc.). Note that using a slash ('/') may break the default algorithm for
       the definition of the user's home directory.

       On Ubuntu, the same constraints as Debian are in place, with the additional constraint that the username cannot be fully numeric. This includes octal
       and hexadecimal syntax.

       Usernames may only be up to 32 characters long.

CONFIGURATION
       The following configuration variables in /etc/login.defs change the behavior of this tool:

       CREATE_HOME (boolean)
	   Indicate if a home directory should be created by default for new users.

	   This setting does not apply to system users, and can be overridden on the command line.

       GID_MAX (number), GID_MIN (number)
	   Range of group IDs used for the creation of regular groups by useradd, groupadd, or newusers.

	   The default value for GID_MIN (resp.	 GID_MAX) is 1000 (resp. 60000).

       HOME_MODE (number)
	   The mode for new home directories. If not specified, the UMASK is used to create the mode.

	   useradd and newusers use this to set the mode of the home directory they create.

       LASTLOG_UID_MAX (number)
	   Highest user ID number for which the lastlog entries should be updated. As higher user IDs are usually tracked by remote user identity and
	   authentication services there is no need to create a huge sparse lastlog file for them.

	   No LASTLOG_UID_MAX option present in the configuration means that there is no user ID limit for writing lastlog entries.

       MAIL_DIR (string)
	   The mail spool directory. This is needed to manipulate the mailbox when its corresponding user account is modified or deleted. If not specified, a
	   compile-time default is used. The parameter CREATE_MAIL_SPOOL in /etc/default/useradd determines whether the mail spool should be created.

       MAIL_FILE (string)
	   Defines the location of the users mail spool files relatively to their home directory.

       The MAIL_DIR and MAIL_FILE variables are used by useradd, usermod, and userdel to create, move, or delete the user's mail spool.

       MAX_MEMBERS_PER_GROUP (number)
	   Maximum members per group entry. When the maximum is reached, a new group entry (line) is started in /etc/group (with the same name, same password,
	   and same GID).

	   The default value is 0, meaning that there are no limits in the number of members in a group.

	   This feature (split group) permits to limit the length of lines in the group file. This is useful to make sure that lines for NIS groups are not
	   larger than 1024 characters.

	   If you need to enforce such limit, you can use 25.

	   Note: split groups may not be supported by all tools (even in the Shadow toolsuite). You should not use this variable unless you really need it.

       PASS_MAX_DAYS (number)
	   The maximum number of days a password may be used. If the password is older than this, a password change will be forced. If not specified, -1 will
	   be assumed (which disables the restriction).

       PASS_MIN_DAYS (number)
	   The minimum number of days allowed between password changes. Any password changes attempted sooner than this will be rejected. If not specified, 0
	   will be assumed (which disables the restriction).

       PASS_WARN_AGE (number)
	   The number of days warning given before a password expires. A zero means warning is given only upon the day of expiration, a negative value means
	   no warning is given. If not specified, no warning will be provided.

       SUB_GID_MIN (number), SUB_GID_MAX (number), SUB_GID_COUNT (number)
	   If /etc/subuid exists, the commands useradd and newusers (unless the user already have subordinate group IDs) allocate SUB_GID_COUNT unused group
	   IDs from the range SUB_GID_MIN to SUB_GID_MAX for each new user.

	   The default values for SUB_GID_MIN, SUB_GID_MAX, SUB_GID_COUNT are respectively 100000, 600100000 and 65536.

       SUB_UID_MIN (number), SUB_UID_MAX (number), SUB_UID_COUNT (number)
	   If /etc/subuid exists, the commands useradd and newusers (unless the user already have subordinate user IDs) allocate SUB_UID_COUNT unused user IDs
	   from the range SUB_UID_MIN to SUB_UID_MAX for each new user.

	   The default values for SUB_UID_MIN, SUB_UID_MAX, SUB_UID_COUNT are respectively 100000, 600100000 and 65536.

       SYS_GID_MAX (number), SYS_GID_MIN (number)
	   Range of group IDs used for the creation of system groups by useradd, groupadd, or newusers.

	   The default value for SYS_GID_MIN (resp.  SYS_GID_MAX) is 101 (resp.	 GID_MIN-1).

       SYS_UID_MAX (number), SYS_UID_MIN (number)
	   Range of user IDs used for the creation of system users by useradd or newusers.

	   The default value for SYS_UID_MIN (resp.  SYS_UID_MAX) is 101 (resp.	 UID_MIN-1).

       UID_MAX (number), UID_MIN (number)
	   Range of user IDs used for the creation of regular users by useradd or newusers.

	   The default value for UID_MIN (resp.	 UID_MAX) is 1000 (resp. 60000).

       UMASK (number)
	   The file mode creation mask is initialized to this value. If not specified, the mask will be initialized to 022.

	   useradd and newusers use this mask to set the mode of the home directory they create if HOME_MODE is not set.

	   It is also used by pam_umask as the default umask value.

       USERGROUPS_ENAB (boolean)
	   If set to yes, userdel will remove the user's group if it contains no more members, and useradd will create by default a group with the name of the
	   user.

FILES
       /etc/passwd
	   User account information.

       /etc/shadow
	   Secure user account information.

       /etc/group
	   Group account information.

       /etc/gshadow
	   Secure group account information.

       /etc/default/useradd
	   Default values for account creation.

       /etc/shadow-maint/useradd-pre.d/*, /etc/shadow-maint/useradd-post.d/*
	   Run-part files to execute during user addition. The environment variable ACTION will be populated with useradd and SUBJECT with the username.
	   useradd-pre.d will be executed prior to any user addition.  useradd-post.d will execute after user addition. If a script exits non-zero then
	   execution will terminate.

       /etc/skel/
	   Directory containing default files.

       /etc/subgid
	   Per user subordinate group IDs.

       /etc/subuid
	   Per user subordinate user IDs.

       /etc/login.defs
	   Shadow password suite configuration.

EXIT VALUES
       The useradd command exits with the following values:

       0
	   success

       1
	   can't update password file

       2
	   invalid command syntax

       3
	   invalid argument to option

       4
	   UID already in use (and no -o)

       6
	   specified group doesn't exist

       9
	   username or group name already in use

       10
	   can't update group file

       12
	   can't create home directory

       14
	   can't update SELinux user mapping

SEE ALSO
       chfn(1), chsh(1), passwd(1), crypt(3), groupadd(8), groupdel(8), groupmod(8), login.defs(5), newusers(8), subgid(5), subuid(5), userdel(8), usermod(8).

shadow-utils 4.13							  05/30/2024								    USERADD(8)
