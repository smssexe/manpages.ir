ADDUSER(8)							    System Manager's Manual							    ADDUSER(8)

NAME
       adduser, addgroup - add or manipulate users or groups

SYNOPSIS
       adduser [--add-extra-groups] [--allow-all-names] [--allow-bad-names] [--comment comment] [--conf file] [--debug] [--disabled-login]
	       [--disabled-password] [--encrypt-home] [--firstgid id] [--firstuid id] [--gid id] [--home dir] [--ingroup group] [--lastgid id] [--lastuid id]
	       [--no-create-home] [--shell shell] [--quiet] [--uid id] [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio] [--logmsglevel prio] user

       adduser --system [--comment comment] [--conf file] [--debug] [--gid id] [--group] [--home dir] [--ingroup group] [--no-create-home] [--shell shell]
	       [--uid id] [--quiet] [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio] [--logmsglevel prio] user

       adduser --group [--conf file] [--debug] [--firstgid id] [--gid ID] [--lastgid id] [--quiet] [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio]
	       [--logmsglevel prio] group

       addgroup [--conf file] [--debug] [--firstgid id] [--gid ID] [--lastgid id] [--quiet] [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio]
		[--logmsglevel prio] group

       addgroup --system [--gid id] [--conf file] [--quiet] [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio] [--logmsglevel prio] group

       adduser [--conf file] [--debug] [--quiet] [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio] [--logmsglevel prio] user group

       adduser --help

       adduser --version

DESCRIPTION
       adduser and addgroup add users and groups to the system according to command line options and configuration information in /etc/adduser.conf.  They are
       friendlier front ends to the low level tools like useradd, groupadd and usermod programs, by default choosing Debian policy conformant UID and GID val‐
       ues, creating a home directory with skeletal configuration, running a custom script, and other features.

       adduser	and addgroup are intended as a policy layer, making it easier for package maintainers and local administrators to create local system accounts
       in the way Debian expects them to be created, taking the burden to adapt to the probably changing specifications of Debian  policy.   adduser  --system
       takes  special  attention  on just needing a single call in the package maintainer scripts without any conditional wrappers, error suppression or other
       scaffolding.

       adduser honors the distinction between dynamically allocated system users and groups and dynamically allocated user accounts that is documented in  De‐
       bian Policy, Chapter 9.2.2.

       For a full list and explanations of all options, see the OPTIONS section.

       adduser and addgroup can be run in one of five modes:

   Add a normal user
       If called with one non-option argument and without the --system or --group  options, adduser will add a normal user, that means a dynamically allocated
       user account in the sense of Debian Policy.  This is commonly referred to in adduser as a non-system user.

       adduser	will choose the first available UID from the range specified by FIRST_UID and LAST_UID in the configuration file.  The range may be overridden
       with the --firstuid and --lastuid options.  Finally, the UID can be set fully manually with the --uid option.

       By default, each user is given a corresponding group with the same name.	 This is commonly called Usergroups and allows group writable  directories  to
       be  easily maintained by placing the appropriate users in the new group, setting the set-group-ID bit in the directory, and ensuring that all users use
       a umask of 002.

       For a usergroup, adduser will choose the first available GID from the range specified by FIRST_GID and LAST_GID in the configuration file.   The	 range
       may be overridden with the --firstgid and --lastgid options.  Finally, the GID can be set fully manually with the --gid option.

       The interaction between USERS_GID, USERS_GROUP, and USERGROUPS is explained in detail in adduser.conf(5).

       Users'  primary	groups can also be overridden from the command line with the --gid  or --ingroup options to set the group by id or name, respectively.
       Also, users can be added to one or more supplemental groups defined as EXTRA_GROUPS in the configuration file either by setting ADD_EXTRA_GROUPS	 to  1
       in the configuration file, or by passing --add-extra-groups on the command line.

       adduser	will copy files from /etc/skel into the home directory and prompt for the comment field and a password if those functions have not been turned
       off / overridden from the command line.

       UID, comment, home directory and shell might be pre-determined with the UID_POOL and GID_POOL option, documented in adduser.conf(5).

       To set up an encrypted home directory for the new user, add the --encrypt-home option.  For more information, refer to the -b option of ecryptfs-setup-
       private(1).

   Add a system user
       If called with one non-option argument and the --system option, adduser will add a dynamically allocated system user, often abbreviated as system  user
       in the context of the adduser package.

       adduser	will  choose  the first available UID from the range specified by FIRST_SYSTEM_UID and LAST_SYSTEM_UID in the configuration file.  This can be
       overridden with the --uid option.

       By default, system users are placed in the nogroup group.  To place the new system user in an already existing group, use the --gid  or	--ingroup  op‐
       tions.  If the --group is given and the identically named group does not already exist, it is created with the same ID.

       If  no  home directory is specified, the default home directory for a new system user is /nonexistent.  This directory should never exist on any Debian
       system, and adduser will never create it automatically.

       Unless a shell is explicitly set with the --shell option, the new system user will have the shell set to /usr/sbin/nologin.  adduser --system does  not
       set a password for the new account.  Skeletal configuration files are not copied.

       Other options will behave as for the creation of a normal user.	The files referenced by UID_POOL and GID_POOL do also work.

   Add a group
       If adduser is called with the --group option and without the --system option, or addgroup is called respectively, a user group will be added.

       A  dynamically  allocated  system  group, often abbreviated as system group in the context of the adduser package, will be created if adduser is called
       with the --system option.

       A GID will be chosen from the respective range specified for GIDs in the configuration file (FIRST_GID, LAST_GID,  FIRST_SYSTEM_GID,  LAST_SYSTEM_GID).
       To override that mechanism, you can give the GID using the --gid option.

       For non-system groups, the range specified in the configuration file may be overridden with the --firstgid and --lastgid options.

       The group is created with no members.

   Add an existing user to an existing group
       If called with two non-option arguments, adduser will add an existing user to an existing group.

OPTIONS
       Different modes of adduser allow different options.  If no valid modes are listed for a option, it is accepted in all modes.

       Short  versions for certain options may exist for historical reasons.  They are going to stay supported, but are removed from the documentation.	 Users
       are advised to migrate to the long version of options.

       --add-extra-groups
	      Add new user to extra groups defined in the configuration files' EXTRA_GROUPS setting.  The old spelling --add_extra_groups  is  deprecated  and
	      will be supported in Debian bookworm only.  Valid Modes: adduser, adduser --system.

       --allow-all-names
	      Allow any user- and groupname which is supported by the underlying useradd(8), including names containing non-ASCII characters.  See VALID NAMES
	      in adduser.conf(5).  Valid Modes: adduser, adduser --system, addgroup, addgroup --system.

       --allow-bad-names
	      Disable  NAME_REGEX  and	SYS_NAME_REGEX	check  of  names.   Only  a  weaker check for validity of the name is applied.	See VALID NAMES in ad‐
	      duser.conf(5).  Valid Modes: adduser, adduser --system, addgroup, addgroup --system.

       --comment comment
	      Set the comment field for the new entry generated.  adduser will not ask for the information if this option is given.  This field is also	 known
	      under  the name GECOS field and contains information that is used by the finger(1) command.  This used to be the --gecos option, which is depre‐
	      cated and will be removed after Debian bookworm.	Valid Modes: adduser, adduser --system.

       --conf file
	      Use file instead of /etc/adduser.conf.  Multiple --conf options can be given.

       --debug
	      Synonymous to --stdoutmsglevel=debug. Deprecated.

       --disabled-login
       --disabled-password
	      Do not run passwd(1) to set a password.  In most situations, logins are still possible though (for example using SSH keys or  through  PAM)  for
	      reasons that are beyond adduser's scope.	--disabled-login will additionally set the shell to /usr/sbin/nologin.	Valid Mode: adduser.

       --firstuid ID
       --lastuid ID
       --firstgid ID
       --lastgid ID
	      Override	the first UID / last UID / first GID / last GID in the range that the uid is chosen from (FIRST_UID, LAST_UID, FIRST_GID and LAST_GID,
	      FIRST_SYSTEM_UID, LAST_SYSTEM_UID, FIRST_SYSTEM_GID and LAST_SYSTEM_GID in the configuration file).  If a	 group	is  created  as	 a  usergroup,
	      --firstgid  and  --lastgid  are  ignored.	  The  group gets the same ID as the user.  Valid Modes: adduser, adduser --system, for --firstgid and
	      --lastgid also addgroup.

       --force-badname
       --allow-badname
	      These are the deprecated forms of --allow-bad-names.  It will be removed during the release cycle of the Debian release after bookworm.

       --extrausers
	      Uses extra users as the database.

       --gid ID
	      When creating a group, this option sets the group ID number of the new group to GID.  When creating a user, this option sets the	primary	 group
	      ID number of the new user to GID.	 Valid Modes: adduser, adduser --system, addgroup, addgroup --system.

       --group
	      Using  this  option in adduser --system indicates that the new user should get an identically named group as its primary group.  If that identi‐
	      cally named group is not already present, it is created.	If not combined with --system, a group with the given name is created.	The latter  is
	      the default action if the program is invoked as addgroup.	 Valid Modes: adduser --system, addgroup, addgroup --system.

       --help Display brief instructions.

       --home dir
	      Use dir as the user's home directory, rather than the default specified by the configuration file (or /nonexistent if adduser --system is used).
	      If the directory does not exist, it is created.  Valid Modes: adduser, adduser --system.

       --ingroup GROUP
	      When creating a user, this option sets the primary group ID number of the new user to the GID of the named group.	 Unlike with the --gid option,
	      the group is specified here by name rather than by numeric ID number.  The group must already exist.  Valid Modes: adduser, adduser --system.

       --lastuid ID
       --lastgid ID
	      Override the last UID / last GID.	 See --firstuid.

       --no-create-home
	      Do  not  create a home directory for the new user.  Note that the pathname for the new user's home directory will still be entered in the appro‐
	      priate field in the /etc/passwd file.  The use of this option does not imply that this field should be empty.  Rather, it indicates  to  adduser
	      that some other mechanism will be responsible for initializing the new user's home directory.  Valid Modes: adduser, adduser --system.

       --quiet
	      Synonymous to --stdoutmsglevel=warn. Deprecated.

       --shell shell
	      Use  shell  as  the user's login shell, rather than the default specified by the configuration file (or /usr/sbin/nologin if adduser --system is
	      used).  Valid Modes: adduser, adduser --system.

       --system
	      Nomally, adduser creates dynamically allocated user accounts and groups as defined in Debian Policy, Chapter 9.2.2.  With this  option,  adduser
	      creates a dynamically allocated system user and group and changes its mode respectively.	Valid Modes: adduser, addgroup.

       --uid ID
	      Force the new userid to be the given number.  adduser will fail if the userid is already taken.  Valid Modes: adduser, adduser --system.

       --verbose
	      Synonymous to --stdoutmsglevel=info. Deprecated.

       --stdoutmsglevel prio
       --stderrmsglevel prio
       --logmsglevel prio
	      Minimum  priority	 for  messages	logged	to syslog/journal and the console, respectively.  Values are trace, debug, info, warn, err, and fatal.
	      Messages with the priority set here or higher get printed to the respective medium.  Messages printed to stderr  are  not	 repeated  on  stdout.
	      That  allows the local admin to control adduser's chattiness on the console and in the log independently, keeping probably confusing information
	      to itself while still leaving helpful information in the log.

       -v , --version
	      Display version and copyright information.

EXIT VALUES
       0      Success: The user or group exists as specified.  This can have 2 causes: The user or group was created by this call to adduser or	 the  user  or
	      group  was  already  present  on the system as specified before adduser was invoked.  If adduser --system is invoked for a user already existing
	      with the requested or compatible attributes, it will also return 0.

       11     The object that adduser was asked to create does already exist.

       12     The object that adduser or deluser was asked to operate on does not exist.

       13     The object that adduser or deluser was asked to operate on does ont have the properties that are required to complete the operation: A  user  (a
	      group) that was requested to be created as a system user (group) does already exist and is not a system user (group), or A user (group) that was
	      requested	 to  be created with a certain UID (GID) does already exist and has a different UID (GID), or A system user (group) that was requested
	      to be deleted does exist, but is not a system user (group).

       21     The UID (GID) that was explicitly requested for a new user (group) is already in use.

       22     There is no available UID (GID) in the requested range.

       23     There is no group with the requested GID for the primary group for a new user.

       31     The chosen name for a new user or a new group does not conform to the selected naming rules.

       32     The home directory of a new user must be an absolute path.

       41     The group that was requested to be deleted is not empty.

       42     The user that was requested to be removed from a group is not a member in the first place.

       43     It is not possible to remove a user from its primary group, or no primary group selected for a new user by any method.

       51     Incorrect number or order of command line parameters detected.

       52     Incompatible options set in configuration file.

       53     Mutually incompatible command line options detected.

       54     adduser and deluser invoked as non-root and thus cannot work.

       55     deluser will refuse to delete the root account.

       56     A function was requested that needs more packages to be installed.  See Recommends: and Suggests: of the adduser package.

       61     Adduser was aborted for some reason and tried to roll back the changes that were done during execution.

       62     Internal adduser error.  This should not happen.	Please try to reproduce the issue and file a bug report.

       71     Error creating and handling the lock.

       72     Error accessing the configuration file(s).

       73     Error accessing a pool file.

       74     Error reading a pool file, syntax error in file.

       75     Error accessing auxiliary files.

       81     An executable that is needed by adduser or deluser cannot be found. Check your installation and dependencies.

       82     Executing an external command returned some unexpected error.

       83     An external command was terminated with a signal.

       84     A syscall terminated with unexpected error.

       Or for many other yet undocumented reasons which are printed to console then.  You may then consider to remove --quiet to make adduser more verbose.

SECURITY
       adduser needs root privileges and offers, via the --conf command line option to use different configuration files.  Do not use sudo(8) or similar tools
       to give partial privileges to adduser with restricted command line parameters.  This is easy to circumvent and might allow users	 to  create  arbitrary
       accounts.  If you want this, consider writing your own wrapper script and giving privileges to execute that script.

FILES
       /etc/adduser.conf
	      Default configuration file for adduser(8) and addgroup(8)

       /usr/local/sbin/adduser.local
	      Optional custom add-ons, see adduser.local(8)

NOTES
       Unfortunately, the term system account suffers from double use in Debian.  It both means an account for the actual Debian system, distinguishing itself
       from  an application account which might exist in the user database of some application running on Debian.  A system account in this definition has the
       potential to log in to the actual system, has a UID, can be member in system groups, can own files and processes.  Debian Policy, au contraire, in  its
       Chapter	9.2.2, makes a distinguishment of dynamically allocated system users and groups and dynamically allocated user accounts, meaning in both cases
       special instances of system accounts.  Care must be taken to not confuse this terminology.  Since adduser and deluser(8) never address application  ac‐
       counts  and  everything in this package concerns system accounts here, the usage of the terms user account and system account is actually not ambiguous
       in the context of this package.	For clarity, this document uses the definition local system account or group if the  distinction  to  application  ac‐
       counts or accounts managed in a directory service is needed.

       adduser	used  to  have	the vision to be the universal front end to the various directory services for creation and deletion of regular and system ac‐
       counts in Debian since the 1990ies.  This vision has been abandoned as of 2022.	The rationale behind this includes: that in practice, a	 small	server
       system  is  not going to have write access to an enterprise-wide directory service anyway, that locally installed packages are hard to manage with cen‐
       trally controlled system accounts, that enterprise directory services have their own management processes anyway and that the personpower  of  the  ad‐
       duser team is unlikely to be ever strong enough to write and maintain support for the plethora of directory services that need support.

       adduser	will  constrict	 itself to being a policy layer for the management of local system accounts, using the tools from the password package for the
       actual work.

BUGS
       Inconsistent use of terminology around the term system account in docs and code is a bug.  Please report this and allow us to improve our docs.

       adduser takes special attention to be directly usable in Debian maintainer scripts without conditional wrappers, error suppression and other  scaffold‐
       ing.   The  only thing that the package maintainer should need to code is a check for the presence of the executable in the postrm script.  The adduser
       maintainers consider the need for additional scaffolding a bug and encourage their fellow Debian package maintainers to file bugs against  the  adduser
       package in this case.

SEE ALSO
       adduser.conf(5), deluser(8), groupadd(8), useradd(8), usermod(8), Debian Policy 9.2.2.

Debian GNU/Linux																    ADDUSER(8)
