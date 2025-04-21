ADDUSER.CONF(5)							      File Formats Manual						       ADDUSER.CONF(5)

NAME
       /etc/adduser.conf - configuration file for adduser(8) and addgroup(8)

DESCRIPTION
       The file /etc/adduser.conf contains defaults for the programs adduser(8), addgroup(8), deluser(8) and delgroup(8).  Each line holds a single value pair
       in  the form option = value.  Double or single quotes are allowed around the value, as is whitespace around the equals sign.  Comment lines must have a
       hash sign (#) in the first column.

       The valid configuration options are:

       STDERRMSGLEVEL ,	 STDOUTMSGLEVEL , and  LOGMSGLEVEL
	      Minimum priority for messages logged to syslog/journal and the console, respectively.  Values are trace, debug,  info,  warn,  err,  and	fatal.
	      Messages	with  the  priority  set  here or higher get printed to the respective medium.	Messages printed to stderr are not repeated on stdout.
	      That allows the local admin to control addusers chattiness on the console and in the log independently, keeping probably	confusing  information
	      to itself while still leaving helpful information in the log.  Defaults to info for STDOUTMSGLEVEL and LOGMSGLEVEL and warn for STDERRMSGLEVEL.

       ADD_EXTRA_GROUPS
	      Setting  this  to	 something other than 0 will cause adduser to add newly created non-system users to the list of groups defined by EXTRA_GROUPS
	      (below).	Defaults to 0.

       DIR_MODE
	      The permissions mode for home directories of non-system users that are created by adduser(8).  Defaults to 0700.	Note that there are  potential
	      configurations (such as /~user web services, or in-home mail delivery) which will require changes to the default.	 See also SYS_DIR_MODE.

       DHOME  The directory in which new home directories should be created.  Defaults to /home.

       DSHELL The login shell to be used for all new users.  Defaults to /bin/bash.

       EXTRA_GROUPS
	      This is the space-separated list of groups that new non-system users will be added to.  Defaults to users.

       FIRST_SYSTEM_GID	 and  LAST_SYSTEM_GID
	      specify an inclusive range of GIDs from which GIDs for system groups can be dynamically allocated.  Defaults to 100 - 999.

       FIRST_GID  and  LAST_GID
	      specify an inclusive range of GIDs from which GIDs for non-system groups can be dynamically allocated.  Defaults to 1000 - 59999.

       FIRST_SYSTEM_UID	 and  LAST_SYSTEM_UID
	      specify an inclusive range of UIDs from which UIDs for system users can be dynamically allocated.	 Defaults to 100 - 999.	 Please note that sys‐
	      tem software, such as the users allocated by the base-passwd package, may assume that UIDs less than 100 are unallocated.

       FIRST_UID  and  LAST_UID
	      specify an inclusive range of UIDs from which UIDs for non-system users can be dynamically allocated.  Defaults to 1000 - 59999.

       GID_POOL
	      See UID_POOL.

       GROUPHOMES
	      If  this is set to yes, the home directories will be created as /home/groupname/user.  Defaults to no. This option is deprecated and will be re‐
	      moved.

       LAST_GID
       LAST_SYSTEM_GID
       LAST_UID
       LAST_SYSTEM_UID
	      See the FIRST_ variants of the option.

       LETTERHOMES
	      If this is set to yes, then the home directories created will have an extra directory inserted which is the first letter of the loginname.   For
	      example: /home/u/user.  Defaults to no. This option is deprecated and will be removed.

       NAME_REGEX
	      Non-system  user- and groupnames are checked against this regular expression.  If the name doesn't match this regexp, user and group creation in
	      adduser(8) is refused unless --allow-bad-names is set.  With --allow-bad-names set, weaker checks are performed.	Defaults to the most conserva‐
	      tive ^[a-z][-a-z0-9_]*$.	See SYS_NAME_REGXEX and Valid names, below, for more information.

       QUOTAUSER
	      If set to a nonempty value, new users will have quotas copied from that user using edquota -p QUOTAUSER newuser.	Defaults to the empty string.

       SETGID_HOME
	      If this is set to yes, then home directories for users with their own group (USERGROUPS = yes) will have the set-group-ID bit  set.   Note  that
	      this feature is deprecated and will be removed in a future version of adduser(8).	 Please use DIR_MODE instead.  Defaults to no.

       SKEL   The directory from which skeletal user configuration files will be copied.  Defaults to /etc/skel.

       SKEL_IGNORE_REGEX
	      When  populating	the  newly  created  home  directory  of  a non-system user, files in SKEL matching this regex are not copied.	Defaults to to
	      (.(dpkg|ucf)-(old|new|dist)$), the regular expression matching files left over from unmerged config files.

       SYS_DIR_MODE
	      The permissions mode for home directories of system users that are created by adduser(8).	 Defaults to 0755.  Note  that	changing  the  default
	      permissions for system users may cause some packages to behave unreliably, if the program relies on the default setting.	See also DIR_MODE.

       SYS_NAME_REGEX
	      System  user- and groupnames are checked against this regular expression.	 If the name doesn't match this regexp, system user and group creation
	      in adduser is refused unless --allow-bad-names is set.  With --allow-bad-names set, weaker checks are performed.	Defaults to the most conserva‐
	      tive ^[a-z_][-a-z0-9_]*$.	 See NAME_REGEX, above, and Valid names, below, for more information.

       UID_POOL	 and  GID_POOL
	      specify a file or a directory containing UID and GID pool files.	See UID and GID POOLS in the NOTES section.  Both default to empty.

       USERGROUPS
	      Specify whether each created non-system user will be given their own group to use.  Defaults to yes.

       USERS_GID  and  USERS_GROUP
	      Defines the groupname or GID of the group all newly-created non-system users are placed into.  If USERGROUPS is yes, the group will be added  as
	      a	 supplementary	group;	if  USERGROUPS	is  no,, it will be the primary group.	If you don't want all your users to be in one group, set USER‐
	      GROUPS=yes, leave USERS_GROUP empty and set USERS_GID to "-1".  USERS_GROUP defaults to users, which has GID 100 on  all	Debian	systems	 since
	      it's defined statically by the base-passwd package.  It is a configuration error to define both variables even if the values are consistent.

NOTES
   VALID NAMES
       Historically,  adduser(8)  and  addgroup(8) enforced conformity to IEEE Std 1003.1-2001, which allows only the following characters to appear in group-
       and usernames: letters, digits, underscores, periods, at signs (@) and dashes.  The name may not start with a dash or @.	 The "$" sign  is  allowed  at
       the end of usernames to allow typical Samba machine accounts.

       The  default settings for NAME_REGEX and SYS_NAME_REGEX allow usernames to contain lowercase letters and numbers, plus dash (-) and underscore (_); the
       name must begin with a letter (or an underscore for system users).

       The least restrictive policy, available by using the --allow-all-names option, simply makes the same checks as useradd(8): cannot start	with  a	 dash,
       plus sign, or tilde; and cannot contain a colon, comma, slash, or whitespace.

       This option can be used to create confusing or misleading names; use it with caution.

       Please  note that regardless of the regular expressions used to evaluate the username, it may be a maximum of 32 bytes; this may be less than 32 visual
       characters when using Unicode glyphs in the username.

   UID AND GID POOLS
       Some installations desire that a non-system account gets preconfigured properties when it is generated.	Commonly, the local admin wants to  make  sure
       that even without using a directory service, an account or a group with a certain name has the same numeric UID/GID on all systems where it exists.

       To  enable  this feature, define configuration variables UID_POOL (for user accounts) and/or GID_POOL (for groups) in /etc/adduser.conf and install the
       respective files in the configured places.  The value is either a file or a directory.  In the latter case all files named *.conf in that directory are
       considered.

       The file format is similar to /etc/passwd: Text lines, fields separated by a colon.  The values are  username/groupname	(mandatory),  UID/GID  (manda‐
       tory), comment field (optional, useful for user IDs only), home directory (ditto), shell (ditto).

       It is possible to use the same file/directory for UID_POOL and GID_POOL.

       If  an account / group is created, adduser(8) searches in all UID/GID pool files for a line matching the name of the newly created account and uses the
       data found there to initialize the new account instead of using the defaults.  Settings may be overridden from the command line.

FILES
       /etc/adduser.conf

SEE ALSO
       deluser.conf(5), addgroup(8), adduser(8), delgroup(8), deluser(8)

Debian GNU/Linux															       ADDUSER.CONF(5)
