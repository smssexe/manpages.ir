DELUSER(8)							    System Manager's Manual							    DELUSER(8)

NAME
       deluser, delgroup - remove a user or group from the system

SYNOPSIS
       deluser [--backup] [--backup-suffix str] [--backup-to dir] [--conf file] [--debug] [--remove-all-files] [--remove-home] [--quiet] [--verbose]
	       [--stdoutmsglevel prio] [--stderrmsglevel prio] [--logmsglevel prio] user

       deluser [--system] [--backup] [--backup-suffix str] [--backup-to dir] [--conf file] [--debug] [--remove-all-files] [--remove-home] [--quiet]
	       [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio] [--logmsglevel prio] user

       deluser --group [--conf file] [--debug] [--only-if-empty] [--quiet] [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio] [--logmsglevel prio]
	       group
       delgroup [--system] [--conf file] [--debug] [--only-if-empty] [--quiet] [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio]
		[--logmsglevel prio] group

       deluser [--conf file] [--debug] [--quiet] [--verbose] [--stdoutmsglevel prio] [--stderrmsglevel prio] [--logmsglevel prio] user group

       deluser --help

       deluser --version

DESCRIPTION
       deluser	and  delgroup remove users and groups from the system according to command line options and configuration information in /etc/deluser.conf and
       /etc/adduser.conf.

       They are friendlier front ends to the userdel and groupdel programs, removing the home directory as option or even all files on the system owned by the
       user to be removed, running a custom script, and other features.

       For a full list and explanations of all options, see the OPTIONS section.

       deluser and delgroup can be run in one of three modes:

   Remove a user
       If called with one non-option argument and without the --group option, deluser will remove a non-system user.

       By default, deluser will remove the user without removing the home directory, the mail spool or any other files on the system owned by the  user.   Re‐
       moving the home directory and mail spool can be achieved using the --remove-home option.

       The   --remove-all-files	 option	 removes all files on the system owned by the user.  Note that if you activate both options --remove-home will have no
       additional effect because all files including the home directory and mail spool are already covered by the --remove-all-files option.

       If you want to backup all files before deleting them you can activate the --backup option which will create a file username.tar(.gz|.bz2) in the direc‐
       tory specified by the --backup-to option.

       By default, the backup archive is compressed with gzip(1).  To change this, the --backup-suffix option can be  set  to  any  suffix  supported  by  tar
       --auto-compress (e.g. .gz, .bz2, .xz).

       deluser will refuse to remove the root account.

       If the --system option is given on the command line, the delete operation is actually executed only if the user is a system user.  This avoids acciden‐
       tally deleting non-system users.	 Additionally, if the user does not exist, no error value is returned.	Debian package maintainer scripts may use this
       flag to remove system users or groups while ignoring the case where the removal already occurred.

   Remove a group
       If  deluser  is	called	with the --group  option, or delgroup is called, a group will be removed.  The primary group of an existing user cannot be re‐
       moved.  If the option --only-if-empty is given, the group won't be removed if it has any members left.

       The --system option adds the same functionality as for users, respectively.

   Remove a user from a specific group
       If called with two non-option arguments, deluser will remove a user from a specific group.

OPTIONS
       Different modes of deluser allow different options.  If no valid modes are listed for a option, it is accepted in all modes.

       Short versions for certain options may exist for historical reasons.  They are going to stay supported, but are removed from the documentation.	 Users
       are advised to migrate to the long version of options.

       --backup
	      Backup  all  files  contained in the userhome and the mailspool file to a file named username.tar.bz2 or username.tar.gz.	 Valid Modes: deluser,
	      deluser --system,

       --backup-suffix str
	      Select compression algorithm for a home directory backup.	 Can be set to any suffix recognized by tar --auto-compress.  Defaults to .gz.	 Valid
	      Modes: deluser, deluser --system,

       --backup-to dir
	      Place  the backup files not in the current directory but in dir.	This implicitly sets --backup also.  (defaulting to the current working direc‐
	      tory).  Valid Modes: deluser, deluser --system,

       --conf file
	      Use file instead of the default files /etc/deluser.conf and /etc/adduser.conf.  Multiple --conf options may be given.

       --debug
	      Synonymous to --stdoutmsglevel=debug. Deprecated.

       --group
	      Remove a group.  This is the default action if the program is invoked as delgroup.  Valid Mode: deluser.

       --help Display brief instructions.

       --only-if-empty
	      Only remove if no members are left.  Valid Modes: deluser --group, delgroup,

       --quiet
	      Synonymous to --stdoutmsglevel=warn. Deprecated.

       --remove-all-files
	      Remove all files from the system owned by this user.  Note: --remove-home does not have an effect any more.  If --backup is specified, the files
	      are deleted after having performed the backup.  Valid Modes: deluser, deluser --system,

       --remove-home
	      Remove the home directory of the user and its mailspool.	If --backup is specified, the files are deleted after  having  performed  the  backup.
	      Valid Modes: deluser, deluser --system,

       --system
	      Only delete if user/group is a system user/group.	 If the user does not exist, no error value is returned.  Valid Modes: deluser, deluser --sys‐
	      tem,

       --verbose
	      Synonymous to --stdoutmsglevel=info. Deprecated.

       --stdoutmsglevel prio
       --stderrmsglevel prio
       --logmsglevel prio
	      Minimum  priority	 for  messages	logged	to syslog/journal and the console, respectively.  Values are trace, debug, info, warn, err, and fatal.
	      Messages with the priority set here or higher get printed to the respective medium.  Messages printed to stderr  are  not	 repeated  on  stdout.
	      That  allows the local admin to control adduser's chattiness on the console and in the log independently, keeping probably confusing information
	      to itself while still leaving helpful information in the log.

       --version
	      Display version and copyright information.

EXIT VALUES
       The exit values documented in adduser(8) also apply for deluser.

SECURITY
       deluser needs root privileges and offers, via the --conf command line option to use different configuration files.  Do not use sudo(8) or similar tools
       to give partial privileges to deluser with restricted command line parameters.  This is easy to circumvent and might allow users	 to  create  arbitrary
       accounts.  If you want this, consider writing your own wrapper script and giving privileges to execute that script.

FILES
       /etc/deluser.conf Default configuration file for deluser(8) and delgroup(8)

       /usr/local/sbin/deluser.local
	      Optional custom add-ons, see deluser.local(8)

SEE ALSO
       adduser(8), deluser.conf(5), deluser.local.conf(8), groupdel(8), userdel(8)

Debian GNU/Linux																    DELUSER(8)
